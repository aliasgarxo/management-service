# Management Service
The Management Service is a backend service that integrates with RabbitMQ to retrieve order messages and exposes a REST API for the ```store-admin``` web app. This service is part of the Algonquin Pet Store microservices architecture, which includes various services like ```order-service``` and ```product-service```. The management-service is designed to handle requests from the ```store-admin``` app, providing access to customer orders stored in a RabbitMQ queue.

### Requirements
- Python 3.10 (with pip)
- RabbitMQ running Locally or on a VM
- Order service running locally or on a VM to send order request

## Setup Instructions

### Step 1: Clone the Repository
Clone the repository containing the management-service code:
```bash
git clone https://github.com/aliasgarxo/management-service.git
cd management-service
```

### Step 2: Install Dependencies
Use pip to install the required Python packages:
```bash
pip install -r requirements.txt
```

### Step 3: Configure Environment Variables

Create a .env file in the root directory of the project to define your environment variables.

Add the following content to your .env file:
```bash
# RabbitMQ connection string
RABBITMQ_CONNECTION_STRING=amqp://newuser:newpassword@localhost:5672/
PORT=2955  # Port for Flask app
```

### Step 4: Run RabbitMQ
Ensure that RabbitMQ is running either locally or on a VM. and is properly setup with username and password.

### Step 5: Run the Management Service
Once RabbitMQ is running, start the management service using the following command:
```bash
python3 main.py
```
By default, the service will run on ```http://localhost:2955```.

## To Run and Test the Service Locally

1. Ensure that RabbitMQ server is running locally or on a VM and oder_queue is created.
2. start the management service from your local terminal 
```bash
python3 main.py
```
the management service will be running locally ```http://localhost:2955/orders/```

3. Ensure order_service is running locally or on a VM and send a order request from the order service REST client or by using store_front page.
4. Test the API Endpoints
You can test the API Endpoint from test_management.http file which include the REST API request 
```bash 
GET http://localhost:2955/orders/
Accept: application/json
```

## API Endpoints

The management-service exposes the following API endpoint:
```GET /orders```
<br>
This service fetches the order message from RabbitMQ. If no orders are available, a 404 response is returned.
<br>
for Example the request will be made such as 
```bash 
GET http://localhost:2955/orders/
Accept: application/json
```
and based on the request if there are any orders present in order_queue it will send a response such as 
```bash
{
  "product": "Cat Food"
}
```
<br>
And if there are no orders available it give a response such as:
```bash
{
  "message": "No orders available"
}
```