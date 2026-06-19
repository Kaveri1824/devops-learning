from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database Connection
db = mysql.connector.connect(
    host="mysql-free-tier.cehuakoia7qd.us-east-1.rds.amezonaws.com",
    user="admin",
    password="Kaveri1212",
    Database="employees",
    port=3306
)

# GET - Fetch all records
@app.route('/employees', methods=['GET'])
def get_employees():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Demo")
    data = cursor.fetchall()
    cursor.close()
    return jsonify(data)

# POST - Insert record
@app.route('/employees', methods=['POST'])
def add_employee():
    data = request.json

    cursor = db.cursor()
    query = "INSERT INTO Demo (name) VALUES (%s)"
    cursor.execute(query, (data['name'],))
    db.commit()
    cursor.close()

    return jsonify({"message": "Employee added successfully"})

# PUT - Update record
@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    data = request.json

    cursor = db.cursor()
    query = "UPDATE Demo SET name=%s WHERE id=%s"
    cursor.execute(query, (data['name'], id))
    db.commit()
    cursor.close()

    return jsonify({"message": "Employee updated successfully"})

# DELETE - Delete record
@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    cursor = db.cursor()
    query = "DELETE FROM Demo WHERE id=%s"
    cursor.execute(query, (id,))
    db.commit()
    cursor.close()

    return jsonify({"message": "Employee deleted successfully"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)