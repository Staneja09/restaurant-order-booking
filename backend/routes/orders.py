from flask import Blueprint, request, jsonify
from db import get_db_connection

orders_bp = Blueprint('orders', __name__)

# CREATE ORDER
@orders_bp.route('/orders', methods=['POST'])
def create_order():
    data = request.json

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO orders (customer_name, phone, address, total) VALUES (%s,%s,%s,%s)",
        (data['name'], data['phone'], data['address'], data['total'])
    )

    order_id = cursor.lastrowid

    for item in data['items']:
        cursor.execute(
            "INSERT INTO order_items (order_id, product_id, quantity) VALUES (%s,%s,%s)",
            (order_id, item['id'], item['quantity'])
        )

    conn.commit()
    conn.close()

    return jsonify({"message": "Order placed successfully"})

@orders_bp.route('/orders', methods=['GET'])
def get_orders():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()

    conn.close()
    return jsonify(orders)

# UPDATE ORDERS
@orders_bp.route('/orders/<int:id>', methods=['PUT'])
def update_order(id):
    data = request.json

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE orders SET status=%s WHERE id=%s",
        (data['status'], id)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Status updated"})