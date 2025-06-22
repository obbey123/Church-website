from flask import render_template, request, redirect
from app import app
import json
import os
from flask import request, flash

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/sermon")
def sermon():
    return render_template("sermon.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        contact_data = {
            "name": name,
            "email": email,
            "message": message
        }

        # Make sure the data folder exists
        file_path = os.path.join("data", "messages.json")
        os.makedirs("data", exist_ok=True)

        # Load existing messages or start new list
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                messages = json.load(f)
        else:
            messages = []

        # Add the new message and save
        messages.append(contact_data)
        with open(file_path, "w") as f:
            json.dump(messages, f, indent=4)

        return redirect("/contact")

    return render_template("contact.html")

@app.route("/admin")
def admin():
    file_path = os.path.join("data", "messages.json")

    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            messages = json.load(f)
    else:
        messages = []

    return render_template("admin.html", messages=messages)

@app.route("/events")
def events():
    file_path = os.path.join("data", "events.json")
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            events = json.load(f)
    else:
        events = []

    return render_template("events.html", events=events)

@app.route("/gallery")
def gallery():
    import os
    image_folder = os.path.join(app.root_path, "static", "images")
    images = []

    if os.path.exists(image_folder):
        for filename in os.listdir(image_folder):
            if filename.lower().endswith((".jpg", ".jpeg", ".png", ".gif")):
                images.append(f"/static/images/{filename}")

    return render_template("gallery.html", images=images)

from flask import request, flash, redirect, url_for

@app.route("/donate", methods=["GET", "POST"])
def donate():
    if request.method == "POST":
        name = request.form.get("name")
        amount = request.form.get("amount")
        method = request.form.get("method")

        # Normally, here you'd save to a database or send to a payment processor
        print(f"Donation received: {name} donated R{amount} via {method}")

        flash("Thank you for your donation!", "success")
        return redirect(url_for("donate"))

    return render_template("donate.html")

import json

@app.route("/sermons")
def sermons():
    with open("data/sermons.json", "r") as f:
        sermons = json.load(f)
    return render_template("sermons.html", sermons=sermons)

@app.route("/admin/sermons", methods=["GET", "POST"])
def admin_sermons():
    if request.method == "POST":
        title = request.form.get("title")
        preacher = request.form.get("preacher")
        date = request.form.get("date")
        video = request.form.get("video")

        new_sermon = {
            "title": title,
            "preacher": preacher,
            "date": date,
            "video": video
        }

        with open("data/sermons.json", "r") as f:
            sermons = json.load(f)

        sermons.append(new_sermon)

        with open("data/sermons.json", "w") as f:
            json.dump(sermons, f, indent=2)

        flash("Sermon added!", "success")
        return redirect(url_for("admin_sermons"))

    return render_template("admin_sermons.html")

@app.route("/biblestudy")
def bible_study():
    return render_template("biblestudy.html")

@app.route("/devotionals")
def devotionals():
    devotionals_list = [
        "God’s grace is sufficient for today.",
        "Your strength comes from the Lord.",
        "You are never alone; He goes before you.",
        "His mercies are new every morning.",
        "Trust God’s plan even when you don’t understand it."
    ]
    return render_template("devotionals.html", devotionals=devotionals_list)

@app.route("/submit_prayer", methods=["POST"])
def submit_prayer():
    name = request.form.get("name")
    prayer = request.form.get("prayer")
    flash("Thank you for your prayer request.", "success")
    return redirect("/contact")

@app.route("/submit_testimony", methods=["POST"])
def submit_testimony():
    name = request.form.get("name")
    testimony = request.form.get("testimony")
    flash("Thank you for sharing your testimony.", "success")
    return redirect("/contact")


@app.route("/partner", methods=["GET", "POST"])
def partner():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")

        with open("partners.txt", "a") as f:
            f.write(f"{name}, {email}, {phone}\n")

        flash("Thank you for signing up as a partner!", "success")
        return redirect("/partner")

    return render_template("partner.html")
