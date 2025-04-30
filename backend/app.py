from flask import Flask, request, jsonify
import psycopg2
import redis
import json
from flask_cors import CORS  # Import CORS

app = Flask(__name__)

# Enable CORS for all domains (or specify a domain if necessary)
CORS(app)

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="bakery", user="admin", password="secret", host="db"
)
cursor = conn.cursor()

# Connect to Redis
redis_client = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route("/products", methods=["GET"])
def get_products():
    # Check Redis cache first
    cached = redis_client.get("products")
    if cached:
        print("Returning products from cache.")
        return jsonify(json.loads(cached))

    # Fetch from DB if not cached
    cursor.execute("SELECT * FROM products;")
    rows = cursor.fetchall()

    # Convert Decimal to float for JSON serialization
    products = [
        {"id": row[0], "name": row[1], "price": float(row[2]), "quantity": row[3]}
        for row in rows
    ]

    # Cache in Redis (expire in 30 seconds)
    redis_client.set("products", json.dumps(products), ex=30)
    
    return jsonify(products)


@app.route("/order", methods=["POST"])
def place_order():
    data = request.json
    cursor.execute("INSERT INTO orders (created_at) VALUES (CURRENT_TIMESTAMP) RETURNING id;")
    order_id = cursor.fetchone()[0]
    
    cursor.execute(
        "INSERT INTO order_items (order_id, product_id, quantity) VALUES (%s, %s, %s)",
        (order_id, data['product_id'], data['quantity'])
    )
    conn.commit()

    # Invalidate cached product list (optional)
    redis_client.delete("products")

    return jsonify({"message": "Order placed", "order_id": order_id}), 201

@app.route("/order/<int:order_id>", methods=["GET"])
def check_status(order_id):
    cursor.execute("SELECT status FROM orders WHERE id = %s;", (order_id,))
    result = cursor.fetchone()
    return jsonify({"status": result[0]}) if result else ("Not Found", 404)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
