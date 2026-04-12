from flask import Blueprint, request, jsonify
from db import get_db_connection

products_bp = Blueprint('products', __name__)

# GET PRODUCTS
@products_bp.route('/products', methods=['GET'])
def get_products():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    conn.close()
    return jsonify(products)

# ADD PRODUCT
@products_bp.route('/products', methods=['POST'])
def add_product():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO products (name, price, category, image) VALUES (%s,%s,%s,%s)",
        (data['name'], data['price'], data['category'], data['image'])
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Product added"})

# DELETE PRODUCT
@products_bp.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM products WHERE id=%s", (id,))
    conn.commit()

    conn.close()
    return jsonify({"message": "Deleted"})