from flask import Blueprint
from controllers import products_controller

product = Blueprint('products', __name__)


@app.route('/products', methods=['POST'])
def add_product():
    return products_controller.add_product()


@app.route('/products/categories', methods=('POST'))
def add_product_category():
    return products_controller.add_product_category()


@app.route('/products', methods=['GET'])
def products_get_all():
    return products_controller.products_get_all()


@app.route('/products/active', methods=('GET'))
def get_active_products():
    return products_controller.get_active_product()


@app.route('/products/companies/<id>', methods=['GET'])
def products_by__company_id():
    return products_controller.products_by_company_id()


@app.route('/products/<id>', methods=['GET'])
def get_by_product_id(product_id):
    return products_controller.get_by_product_id()


@app.route('/products/<id>', methods=['PUT'])
def update_products(product_id):
    return products_controller.update_products()


@app.route('/products/delete', methods=['DELETE'])
def remove_product():
    return products_controller.remove_product()
