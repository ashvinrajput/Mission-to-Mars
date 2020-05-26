from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import json

app = Flask(__name__, template_folder="mars_templates")

#PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find record from the mongo database
    mars_website = mongo.db.data.find_one()
    print(mars_website)

    # template and data
    return render_template("index.html", mars_page=mars_page)


# Route to inititae the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_data = scrape_mars.scrape_info()
  
    # Update the Mongo database using update and upsert=True
    mongo.db.data.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)