from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection details
mongo_host = "mongodb"  # The service name defined in your docker-compose.yml
mongo_port = 27017
mongo_user = "myuser"
mongo_password = "mypassword"
auth_source = "admin"


# Connect to MongoDB
client = MongoClient(
    host=mongo_host,
    port=mongo_port,
    username=mongo_user,
    password=mongo_password,
    authSource=auth_source,
)
db = client["mydatabase"]
collection = db["profiles"]

# db = client.mydatabase  # Replace with your database name
# collection = db.profiles  # Replace with your collection name

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        profile = {"name": name, "email": email}
        collection.insert_one(profile)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
