from flask import Flask, request, Response
from flaskext.mysql import MySQL
import json

mysql = MySQL()
app=Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'hardik99'
app.config['MYSQL_DATABASE_DB'] = 'ApiData'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
conn = mysql.connect()
cursor =conn.cursor()

@app.route("/")
def hello():
    return "ShitAPI v1.0"

@app.route("/get", methods=['GET'])
def get_data():
	cursor.execute("SELECT * from Data")
	data=json.dumps(cursor.fetchone())
	return Response(data, status=200, mimetype='application/json')

@app.route("/post", methods=['POST'])
def add():
	cursor.execute("INSERT INTO Data(data) VALUES (%s)", request.json.get("data", ""))
	conn.commit()
	return Response(status=201, mimetype='application/json')

if __name__ == "__main__":
    app.run()
