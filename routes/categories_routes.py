from flask import Blueprint
from controllers import categories_controller

product = Blueprint('categories', __name__)


@app.route('/categories', methods=('POST'))
def add_category():
    return categories_controller.add_category()


@app.route('/categories', methods=('GET'))
def categories_get_all():
    return categories_controller.categories_get_all()


@app.route('/categories/<id>', methods=['GET'])
def get_by_category_id(category_id):
    return categories_controller.get_by_category_id()


@app.route('/companies/<id>', methods=('PUT'))
def update_category(category_id):
    return categories_controller.update_category()
