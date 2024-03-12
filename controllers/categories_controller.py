from flask import jsonify, request
import psycopg2
import os

database_name = os.environ.get('DATABASE_NAME')
app_host = os.environ.get('APP_HOST')
app_port = os.environ.get('APP_PORT')

conn = psycopg2.connect(f"dbname={database_name}")
cursor = conn.cursor()


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
                (category_name)
                VALUES(%s)""",
            (category_name,)

        )
        conn.commit()

    except Exception as e:
        print(e)
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

    return jsonify({"message": "category found", "result": record_list}), 200


def get_by_category_id(category_id):
    result = cursor.execute("""
            SELECT * FROM Categories
                WHERE category_id = %s
                            
        """, [category_id])
    result = cursor.fetchone()

    if result:
        return jsonify({"message": "categories found", "results": result}), 200
    return jsonify({"message": f'categories with id {category_id} not found.'}), 404


def update_category(category_id):
    post_data = request.form if request.form else request.get_json()

    cursor.execute("""
  UPDATE Categories SET category_name=%s
   WHERE category_id = %s""",
                   (post_data.get("category_name"), category_id)
                   )

    cursor.execute("""
                            SELECT * FROM Categories WHERE category_id = %s""", [category_id])
    result = cursor.fetchone()

    result = {
        "category_id": result[0],
        "category_name": result[1]
    }

    return jsonify({'message': 'category Updated', 'result': result}), 200
