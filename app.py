import os
from flask import (
    Flask, flash, render_template,
    redirect, request, url_for)
from flask_pymongo import PyMongo
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def home():
    return render_template("index.html")


#returns the current list of activities in the database
@app.route("/get_activities")
def get_activities():
    place_to_visit = list(mongo.db.place_to_visit.find())
    return render_template("places_to_visit.html", place_to_visit=place_to_visit)


# class AddForm(FlaskForm):
    # name = StringField('name', validators=[DataRequired()])


#to add activity to site
@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        activity = {
            "category_name": request.form.get("category_name"),
            "name": request.form.get("name"),
            "description": request.form.get("description"),
            "age_range": request.form.get("age"),
            "location": request.form.get("location"),
            "image": request.form.get("image")
        }
        mongo.db.place_to_visit.insert_one(activity)
        flash("Thank you for adding a new activity to our site for others to enjoy!!")
        return redirect(url_for("get_activities"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    age_ranges = mongo.db.age_ranges.find()
    return render_template("add_activity.html", categories=categories, age_ranges=age_ranges)
    # form = AddForm()
    # return render_template("add_activity.html", form=form)


# to edit activities on the site
@app.route("/edit_activity/<activity_id>", methods=["GET", "POST"])
def edit_activity(activity_id):
    if request.method == "POST":
        load = {
            "category_name": request.form.get("category_name"),
            "name": request.form.get("name"),
            "description": request.form.get("description"),
            "age_range": request.form.get("age_range"),
            "location": request.form.get("location"),
            "image": request.form.get("image")
        }
        mongo.db.place_to_visit.update({"_id": ObjectId(activity_id)}, load)
        flash("Activity succesfully updated. Thank you for keeping our site up to date!")
        return redirect(url_for("get_activities"))
        
    activity = mongo.db.place_to_visit.find_one({"_id": ObjectId(activity_id)})

    categories = mongo.db.categories.find().sort("category_name", 1)
    age_ranges = mongo.db.age_ranges.find()
    return render_template("edit_activity.html", activity=activity, categories=categories, age_ranges=age_ranges)


# to delete activities from the site
@app.route("/delete_activity/<activity_id>")
def delete_activity(activity_id):
    mongo.db.place_to_visit.remove({"_id": ObjectId(activity_id)})
    flash("Actvity Successfully Deleted. Thank You!")
    return redirect(url_for("get_activities"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

