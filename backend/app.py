from flask import Flask
from flask_cors import CORS

from routes.products import products_bp
from routes.orders import orders_bp
from routes.admin import admin_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(products_bp)
app.register_blueprint(orders_bp)
app.register_blueprint(admin_bp)

if __name__ == "__main__":
    app.run(debug=True)