from flask import Flask, jsonify, request
import psycopg2
import os

database_name = os.environ.get('DATABASE_NAME')
app_host = os.environ.get('APP_HOST')
app_port = os.environ.get('APP_PORT')

conn = psycopg2.connect(f"dbname={database_name}")
cursor = conn.cursor()


app = Flask(__name__)


def add_category():
    post_data = request.form if request.form else request.get_json()

    category_name = post_data.get('category_name')

    if not category_name:
        return jsonify({"message": "category_name is a Required Field"}), 400

    result = cursor.execute("""
        SELECT * FROM Categories
            WHERE category_name=%s""",
                            [category_name])
    result = cursor.fetchone()
    if result:
        return jsonify({"message": 'Company already exists'}), 400

    try:
        cursor.execute(
            """INSERT INTO Categories
                (product_name, description, price)
                VALUES(%s, %s, %s)""",
            (category_name)

        )
        conn.commit()

    except:
        cursor.rollback()
        return jsonify({'message': 'category could not be added'}), 400

    return jsonify({"message": f"Category {category_name} added to DB"}), 200


def categories_get_all():
    result = cursor.execute("""
            SELECT * FROM Categories;
        """)
    result = cursor.fetchall()

    record_list = []

    for record in result:
        record = {
            'category_id': record[0],
            'category_name': record[1],
        }
        record_list.append(record)

    return jsonify({"message": "category found", "results": record_list}), 200


def get_by_category_id(category_id):
    result = cursor.execute("""
            SELECT * FROM Categories;
                    WHERE category_id
        """)
    result = cursor.fetchall()

    for record in result:
        if record['category_id'] == int(category_id):
            return jsonify({"message": "categories found", "results": record}), 200
    return jsonify({"message": f'categories with id {category_id} not found.'}), 404


def update_categories(category_id):
    post_data = request.form if request.form else request.get_json()

    result = cursor.execute("""
  "UPDATE Categories SET category_name=(%s)"
  " WHERE category_id = (%s)", 
  ("category_name")
        """)
    result = cursor.fetchall()

    record = {}

    for record in result:
        if category['category_id'] == int(category_id):
            category = record

    category['name'] = post_data.get('name', category['name'])

    return jsonify({'message': 'category Updated', 'results': category}), 200
