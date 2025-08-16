from flask import Flask, request, render_template, jsonify
import cloudinary_setup

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
    db = client['flask_db']
    coll = db['rentalpending']

    uploaded_urls = []
    # Handle multiple images
    if "images" in request.files:
        images = request.files.getlist("images")
        for img in images:
            if img.filename != "":
                result = cloudinary_setup.cloudinary.uploader.upload(img, folder="property_images")
                uploaded_urls.append(result["secure_url"])
    

    # Handle optional reel
    reel_url = None
    if "reel" in request.files and request.files["reel"].filename != "":
        reel = request.files["reel"]
        result = cloudinary_setup.cloudinary.uploader.upload(reel, resource_type="video", folder="property_videos")
        reel_url = result["secure_url"]

    #return jsonify({
    #    "images": uploaded_urls,
    #    "reel": reel_url
    #})
    coll.insert_one({
    "owner_name": request.form.get("owner_name"),
    "owner_contact": request.form.get("owner_contact"),
    "owner_info": request.form.get("owner_info"),
    "property_location": request.form.get("property_location"),
    "google_pin": request.form.get("google_pin"),
    "docs": request.form.getlist("docs[]"),
    "requirements": request.form.getlist("requirements[]"),
    "deposit": request.form.get("deposit"),
    "monthly_rent": request.form.get("monthly_rent"),
    "maintenance": request.form.get("maintenance"),
    "sharing_rent": request.form.get("sharing_rent"),
    "restrictions": request.form.getlist("restrictions[]"),
    "facilities": request.form.getlist("facilities[]"),
    "images": uploaded_urls,   # list of Cloudinary URLs
    "reel": reel_url           # string URL, or None if not uploaded
})


    return render_template("rent-submit.html", message="Your Details are Under Review, We will Reach/Contact you soon!")



if __name__ == "__main__" :
    app.run(debug = True)