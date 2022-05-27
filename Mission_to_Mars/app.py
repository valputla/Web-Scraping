from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# conn = "mongodb://localhost:27017"
# client = pymongo.MongoClient(conn)


# Or set inline
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")
mars_collection = mongo.db.mars



@app.route("/")
def index():
   
    mars_results = mars_collection.find_one()
    # mongo.db.mars_data.find_one()
 
    return render_template("index.html", mars=mars_results)

@app.route("/scrape")
def scraper():
   
    mars_data = scrape_mars.scrape()
    
    mars_collection.update_one({}, {"$set": mars_data}, upsert=True)
    
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
