from flask import Flask, jsonify, request
from flaskext.mysql import MySQL

mysql = MySQL()
app=Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'hardik99'
app.config['MYSQL_DATABASE_DB'] = 'Data'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/")
def hello():
    return "ShitAPI v1.0"

if __name__ == "__main__":
    app.run()
