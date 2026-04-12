from flask import Blueprint, request, jsonify
from db import get_db_connection

admin_bp = Blueprint('admin', __name__)

# LOGIN
@admin_bp.route('/admin/login', methods=['POST'])
def login():
    data = request.json

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM admin WHERE username=%s AND password=%s",
        (data['username'], data['password'])
    )

    admin = cursor.fetchone()
    conn.close()

    if admin:
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})