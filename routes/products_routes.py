from flask import Blueprint
from controllers import products_controller

products = Blueprint('products', __name__)


@products.route('/product', methods=['POST'])
def add_product():
    return products_controller.add_product()


@products.route('/products', methods=['GET'])
def products_get_all():
    return products_controller.products_get_all()


@products.route('/products/active', methods=['GET'])
def get_active_products():
    return products_controller.get_active_product()


@products.route('/product/company/<company_id>', methods=['GET'])
def product_by__company_id(company_id):
    return products_controller.product_by_company_id(company_id)


@products.route('/product/<product_id>', methods=['GET'])
def get_by_product_id(product_id):
    return products_controller.get_by_product_id(product_id)


@products.route('/product/<product_id>', methods=['PUT'])
def update_product(product_id):
    return products_controller.update_product(product_id)


@products.route('/product/<product_id>', methods=['DELETE'])
def remove_product(product_id):
    return products_controller.remove_product(product_id)
