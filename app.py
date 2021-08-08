import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
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
    return render_template("index.html", page_title="Home")


@app.route("/get_activities")
def get_activities():
    place_to_visit = list(mongo.db.place_to_visit.find())
    return render_template("places_to_visit.html", place_to_visit=place_to_visit)


# class AddForm(FlaskForm):
    # name = StringField('name', validators=[DataRequired()])


@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        activity = {
            "category_name": request.form.get("category_name"),
            "name": request.form.get("name"),
            "age_range": request.form.get("age_range"),
            "description": request.form.get("description")
        }
        mongo.db.tasks.insert_one(task)
        flash("Thank you for adding a new activity to our site for others to enjoy!!")
        return redirect(url_for("get_activities"))

    categories = mongo.db.categories.find().sort("category_name", 1),
    age_ranges = mongo.db.age_ranges.find()
    return render_template("add_activity.html", categories=categories, age_ranges=age_ranges)
    # form = AddForm()
    # return render_template("add_activity.html", form=form)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

