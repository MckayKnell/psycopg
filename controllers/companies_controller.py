from flask import jsonify, request
import psycopg2
import os

database_name = os.environ.get('DATABASE_NAME')
app_host = os.environ.get('APP_HOST')
app_port = os.environ.get('APP_PORT')

conn = psycopg2.connect(f"dbname={database_name}")
cursor = conn.cursor()


def add_company():
    post_data = request.form if request.form else request.get_json()

    company_name = post_data.get('company_name')

    if not company_name:
        return jsonify({"message": "company_name is a Required Field"}), 400

    result = cursor.execute("""
        SELECT * FROM Companies
            WHERE company_name=%s""",
                            [company_name])
    result = cursor.fetchone()
    if result:
        return jsonify({"message": 'Company already exists'}), 400

    try:
        cursor.execute(
            """INSERT INTO Companies
                (company_name)
                VALUES(%s)""",
            (company_name,)

        )
        conn.commit()

    except:
        return jsonify({'message': 'Company could not be added'}), 400

    return jsonify({"message": f"Company {company_name} added to DB"}), 200


def companies_get_all():
    result = cursor.execute("""
            SELECT * FROM Companies;
        """)
    result = cursor.fetchall()

    record_list = []

    for record in result:
        record = {
            'company_id': record[0],
            'company_name': record[1],
        }
        record_list.append(record)

    return jsonify({"message": "company found", "result": record_list}), 200


def get_by_company_id(company_id):
    result = cursor.execute("""
            SELECT * FROM Companies
                    WHERE company_id = %s
        """, [company_id])
    result = cursor.fetchone()

    if result:
        return jsonify({"message": "products found", "results": result}), 200
    return jsonify({"message": f'Company with id {company_id} not found.'}), 404


def update_company(company_id):
    post_data = request.form if request.form else request.get_json()

    cursor.execute("""
  UPDATE Companies SET company_name=%s
   WHERE company_id = %s""",
                   (post_data.get("company_name"), company_id)
                   )

    cursor.execute("""
                            SELECT * FROM Companies WHERE company_id = %s""", [company_id])
    result = cursor.fetchone()

    result = {
        "company_id": result[0],
        "company_name": result[1]
    }
    return jsonify({'message': 'company Updated', 'results': result}), 200
