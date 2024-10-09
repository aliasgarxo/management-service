# management_service.py

import pika
import json
from flask import Flask, jsonify, request
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

# RabbitMQ connection details
RABBITMQ_CONNECTION_STRING = os.getenv('RABBITMQ_CONNECTION_STRING', 'amqp://localhost')
QUEUE_NAME = 'order_queue'

# Function to get orders from RabbitMQ
def get_orders_from_queue():
    try:
        # Connect to RabbitMQ server
        connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_CONNECTION_STRING))
        channel = connection.channel()

        # Declare the queue (must be the same as in order-service)
        channel.queue_declare(queue=QUEUE_NAME, durable=False)

        # Fetch all messages from the queue
        method_frame, header_frame, body = channel.basic_get(QUEUE_NAME, auto_ack=True)
        
        # If no message is in the queue
        if method_frame:
            # Convert byte message to dictionary
            order = json.loads(body.decode())
            return order
        else:
            return None
    except Exception as e:
        print(f"Error while connecting to RabbitMQ: {e}")
        return None

# Define route to get orders from RabbitMQ
@app.route('/orders', methods=['GET'])
def get_orders():
    order = get_orders_from_queue()
    if order:
        return jsonify(order), 200
    else:
        return jsonify({"message": "No orders available"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT', 2955))
