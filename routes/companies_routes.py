from flask import Blueprint
from controllers import companies_controller

companies = Blueprint('companies', __name__)


@companies.route('/company', methods=['POST'])
def add_company():
    return companies_controller.add_company()


@companies.route('/companies', methods=['GET'])
def companies_get_all():
    return companies_controller.companies_get_all()


@companies.route('/company/<company_id>', methods=['GET'])
def get_by_company_id(company_id):
    return companies_controller.get_by_company_id(company_id)


@companies.route('/company/<company_id>', methods=['PUT'])
def update_company(company_id):
    return companies_controller.update_company(company_id)
