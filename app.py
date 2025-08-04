from flask import Flask, request, render_template

app = Flask(__name__)

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://Abutalha:Abuisbest@free-cluster.oryjuey.mongodb.net/?retryWrites=true&w=majority&appName=Free-Cluster"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/buyhome')
def buy():
    return render_template("buyhome.html")

@app.route('/sellhome')
def sell():
    return render_template("sellhome.html")

@app.route('/get-rental')
def get_rental():
    return render_template("get-rental.html")

@app.route('/rent-out')
def rent_out():
    return render_template("rent-out.html")

@app.route('/RentSubmit', methods=['POST'])
def rent_submit():
    return render_template("rent-submit.html", message="Your Details are Under Review, We will Reach/Contact you soon!")



if __name__ == "__main__":
    app.run(debug = True)