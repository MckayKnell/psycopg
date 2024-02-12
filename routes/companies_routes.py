from flask import Blueprint
from controllers import companies_controller

product = Blueprint('companies', __name__)


@app.route('/companies', methods=('POST'))
def add_company():
    return companies_controller.add_company()


@app.route('/companies', methods=('GET'))
def companies_get_all():
    return companies_controller.companies_get_all()


@app.route('/companies/<id>', methods=('GET'))
def get_by_company_id(company_id):
    return companies_controller.get_by_company_id()


@app.route('/companies/<id>', methods=['PUT'])
def update_company(company_id):
    return companies_controller.update_company()
