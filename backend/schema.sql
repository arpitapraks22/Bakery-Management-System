CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price FLOAT NOT NULL,
    quantity INT NOT NULL
);

CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS order_items (
    id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(id),
    product_id INT REFERENCES products(id),
    quantity INT NOT NULL
);
INSERT INTO products (name, price, quantity) VALUES ('Chocolate Cake', 20.50, 10);
INSERT INTO products (name, price, quantity) VALUES ('Croissant', 5.00, 50);
