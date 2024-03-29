from flask import Flask
from routes.products_routes import products
from routes.companies_routes import companies
from routes.categories_routes import categories
from db import create_all

app = Flask(__name__)

app.register_blueprint(products)
app.register_blueprint(companies)
app.register_blueprint(categories)


if __name__ == '__main__':
    create_all()
    app.run(host='0.0.0.0', port='8086')
