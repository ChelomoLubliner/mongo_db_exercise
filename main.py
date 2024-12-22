from flask import Flask
from pymongo import MongoClient
import api_routes  # Import the routes from the other file

# Initialize Flask app
app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['attacks_db']  # Replace with your database name
collection = db['attacks']  # Replace with your collection name

# Pass the app, db, and collection to the routes
api_routes.initialize_routes(app, db, collection)

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
