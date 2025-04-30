🧁 Bakery Management System

This project is a **Dockerized Bakery Management System** built with a Flask-based backend API, PostgreSQL for storage, Redis for caching, and a frontend served via Nginx. 
It demonstrates container orchestration and best practices in multi-service applications using Docker Compose.

🏗️ System Architecture Overview

The application is composed of the following services:

- 🔧 Backend API (Flask):  
  Handles product listing, order placement, and order status retrieval.

- 🖥️ Frontend (HTML + Nginx):  
  A simple web UI that interacts with the backend API to display products and place orders.

- 🗄️ PostgreSQL:
  Stores bakery product and order data.

- ⚡ Redis:  
  Caches product listings for 30 seconds to improve performance and reduce database load.

All services are containerized with **Docker** and orchestrated using **Docker Compose**, connected via a shared Docker network.

⚙️ Setup Instructions

📁 1. Create a `.env` File

Create a `.env` file in the root directory with the following content:

```env
POSTGRES_DB=bakery
POSTGRES_USER=admin
POSTGRES_PASSWORD=secret
```

 🐳 2. Build and Run the Project

To build and start all containers:

docker-compose up --build

To run in detached (background) mode:

docker-compose up -d

🌐 3. Access the Application

- Frontend: [http://localhost:8080](http://localhost:8080)  
- Backend API: [http://localhost:5000](http://localhost:5000)

📘 API Documentation

🔹 `GET /products`

- Description: Retrieve all bakery products.  
- Response: JSON array of product records.  
- Caching: Results cached in Redis for 30 seconds.


🔹 `POST /order`

- Description: Place a new bakery order.  
- Request Body:
  json
  {
    "product_id": 1,
    "quantity": 2
  }
  
- Response:
  json
  {
    "message": "Order placed"
  }

🔹 `GET /order/<order_id>`

- Description: Retrieve the status of an existing order.  
- Response:
  json
  {
    "status": "pending"
  }
  
 🧰 Tech Stack

| Component   | Technology        |
|-------------|-------------------|
| Backend     | Python (Flask)    |
| Database    | PostgreSQL        |
| Frontend    | HTML + Nginx      |
| Caching     | Redis             |
| DevOps      | Docker, Docker Compose |

