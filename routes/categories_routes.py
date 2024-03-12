from flask import Blueprint
from controllers import categories_controller

categories = Blueprint('categories', __name__)


@categories.route('/category', methods=['POST'])
def add_category():
    return categories_controller.add_category()


@categories.route('/categories', methods=['GET'])
def categories_get_all():
    return categories_controller.categories_get_all()


@categories.route('/category/<category_id>', methods=['GET'])
def get_by_category_id(category_id):
    return categories_controller.get_by_category_id(category_id)


@categories.route('/category/<category_id>', methods=['PUT'])
def update_category(category_id):
    return categories_controller.update_category(category_id)
