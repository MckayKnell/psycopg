from flask import Blueprint
from controllers import products_controller

product = Blueprint('products', __name__)


@app.route('/companies', methods=('POST'))
def add_company():
    return products_controller.add_company()


@app.route('/categories', methods=('POST'))
def add_category():
    return products_controller.add_category()


@app.route('/products', methods=['POST'])
def add_product():
    return products_controller.add_product()


@app.route('/products/categories', methods=('POST'))
def add_product_category():
    return products_controller.add_product_category()


@app.route('/companies', methods=('GET'))
def companies_get_all():
    return products_controller.companies_get_all()


@app.route('/categories', methods=('GET'))
def categories_get_all():
    return products_controller.categories_get_all()


@app.route('/products', methods=['GET'])
def products_get_all():
    return products_controller.products_get_all()


@app.route('/products/active', methods=('GET'))
def get_active_products():
    return products_controller.get_active_products()


@app.route('/products/companies/<id>', methods=['GET'])
def products_by__company_id():
    return products_controller.products_by_company_id()


@app.route('/companies/<id>', methods=('GET'))
def get_by_company_id(company_id):
    return products_controller.get_by_company_id()


@app.route('/categories/<id>', methods=['GET'])
def get_by_category_id(category_id):
    return products_controller.get_by_category_id()


@app.route('/products/<id>', methods=['GET'])
def get_by_product_id(product_id):
    return products_controller.get_by_product_id()


@app.route('/companies/<id>', methods=['PUT'])
def update_company(company_id):
    return products_controller.update_company()


@app.route('/companies/<id>', methods=('PUT'))
def update_category(category_id):
    return products_controller.update_category()


@app.route('/products/<id>', methods=['PUT'])
def update_products(product_id):
    return products_controller.update_products()


@app.route('/productscategories/<id>/<id>', methods=['PUT'])
def update_product_categories_xref():
    return products_controller.update_product_categories_xref()


@app.route('/products/delete', methods=['DELETE'])
def remove_product():
    return products_controller.remove_product()
