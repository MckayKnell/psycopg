from flask import Flask, jsonify, request
import psycopg2
import os

database_name = os.environ.get('DATABASE_NAME')
app_host = os.environ.get('APP_HOST')
app_port = os.environ.get('APP_PORT')

conn = psycopg2.connect(f"dbname={database_name}")
cursor = conn.cursor()


app = Flask(__name__)


def add_product():
    post_data = request.form if request.form else request.get_json()

    product_name = post_data.get('product_name')
    description = post_data.get('description')
    price = post_data.get('price')

    if not product_name:
        return jsonify({"message": "product_name is a Required Field"}), 400

    result = cursor.execute("""
        SELECT * FROM Products
            WHERE product_name=%s""",
                            [product_name])
    result = cursor.fetchone()
    if result:
        return jsonify({"message": 'Product already exists'}), 400

    try:
        cursor.execute(
            """INSERT INTO Products
                (product_name, description, price)
                VALUES(%s, %s, %s)""",
            (product_name, description, price)

        )
        conn.commit()

    except:
        cursor.rollback()
        return jsonify({'message': 'product could not be added'}), 400

    return jsonify({"message": f"Product {product_name} added to DB"}), 200


def products_get_all():
    result = cursor.execute("""
            SELECT * FROM Products;
        """)
    result = cursor.fetchall()

    record_list = []

    for record in result:
        record = {
            'product_id': record[0],
            'product_name': record[1],
            'description': record[2],
            'price': record[3],
            'active': record[4]
        }
        record_list.append(record)

    return jsonify({"message": "products found", "results": record_list}), 200


def get_active_product():
    result = cursor.execute("""
            SELECT * FROM Products;
                WHERE active=%s
        """)
    result = cursor.fetchall()

    record_list = []

    for record in result:
        record = {
            'product_id': record[0],
            'product_name': record[1],
            'description': record[2],
            'price': record[3],
            'active': record[4]
        }
        record_list.append(record)

    return jsonify({"message": "products found", "results": record_list}), 200


def products_by_company_id(company_id):
    result = cursor.execute("""
            SELECT * FROM Products;
                    WHERE company_id
        """)
    result = cursor.fetchall()

    for record in result:
        if record['company_id'] == int(company_id):
            return jsonify({"message": "products found", "results": record}), 200
    return jsonify({"message": f'Company with id {company_id} not found.'}), 404


def get_by_product_id(product_id):
    result = cursor.execute("""
            SELECT * FROM Products;
                    WHERE product_id
        """)
    result = cursor.fetchall()

    for product in result:
        if product['product_id'] == int(product_id):
            return jsonify({"message": "products found", "results": product}), 200
    return jsonify({"message": f'Products with id {product_id} not found.'}), 404


def update_products(product_id):
    post_data = request.form if request.form else request.get_json()

    result = cursor.execute("""
  "UPDATE Products SET product_name=(%s)"
  " WHERE product_id = (%s)", 
  ("product_name", "description", "price")
        """)
    result = cursor.fetchall()

    record = {}

    for record in result:
        if product['product_id'] == int(product_id):
            product = record

    product['name'] = post_data.get('name', product['name'])
    product['description'] = post_data.get('description', product['description'])
    product['price'] = post_data.get('price', product['price'])

    return jsonify({'message': 'product Updated', 'results': product}), 200


def remove_product(product_id):
    post_data = request.form if request.form else request.get_json()

    result = cursor.execute("""
    SELECT * FROM Products WHERE product_id
        """)
    result = cursor.fetchall()

    product = {}

    product['product_id'] = post_data['product_id']
    product['name'] = post_data['name']
    product['description'] = post_data['description']
    product['price'] = post_data['price']
    product['active'] = post_data['active']

    result.remove(product)

    return jsonify({'message': 'product removed', 'results': product}), 200
