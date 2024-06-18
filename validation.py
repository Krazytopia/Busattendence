from flask import Flask, request, jsonify
import mysql.connector
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

db = mysql.connector.connect(
    host='your_database_host',
    user='your_database_user',
    password='your_database_password',
    database='your_database_name'
)

@app.route('/register', methods=['POST'])
def register():
    bus_id = request.json.get('busId')
    password = request.json.get('password')

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    cursor = db.cursor()
    query = "INSERT INTO users (busId, password) VALUES (%s, %s)"
    cursor.execute(query, (bus_id, hashed_password))
    db.commit()

    return jsonify({'success': True, 'message': 'User registered successfully'})

@app.route('/login', methods=['POST'])
def login():
    bus_id = request.json.get('busId')
    password = request.json.get('password')

    cursor = db.cursor()
    query = "SELECT password FROM users WHERE busId = %s"
    cursor.execute(query, (bus_id,))
    result = cursor.fetchone()

    if result:
        hashed_password = result[0]
        if bcrypt.check_password_hash(hashed_password, password):
            return jsonify({'success': True, 'message': 'Login successful'})
        else:
            return jsonify({'success': False, 'message': 'Invalid bus ID or password'})
    else:
        return jsonify({'success': False, 'message': 'Invalid bus ID or password'})

if __name__ == '__main__':
    app.run(debug=True)

#from flask import Flask, request, jsonify
import mysql.connector
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

db = mysql.connector.connect(
    host='your_database_host',
    user='your_database_user',
    password='your_database_password',
    database='your_database_name'
)

@app.route('/register', methods=['POST'])
def register():
    bus_id = request.json.get('busId')
    password = request.json.get('password')

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    cursor = db.cursor()
    query = "INSERT INTO users (busId, password) VALUES (%s, %s)"
    cursor.execute(query, (bus_id, hashed_password))
    db.commit()

    return jsonify({'success': True, 'message': 'User registered successfully'})

@app.route('/login', methods=['POST'])
def login():
    bus_id = request.json.get('busId')
    password = request.json.get('password')

    cursor = db.cursor()
    query = "SELECT password FROM users WHERE busId = %s"
    cursor.execute(query, (bus_id,))
    result = cursor.fetchone()

    if result:
        hashed_password = result[0]
        if bcrypt.check_password_hash(hashed_password, password):
            return jsonify({'success': True, 'message': 'Login successful'})
        else:
            return jsonify({'success': False, 'message': 'Invalid bus ID or password'})
    else:
        return jsonify({'success': False, 'message': 'Invalid bus ID or password'})

if __name__ == '__main__':
    app.run(debug=True)


#pip install flask flask_bcrypt mysql-connector-python -> Run this in terminal for libraries