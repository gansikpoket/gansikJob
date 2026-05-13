# BLUEPRINT | DONT EDIT

from flask import Flask, render_template, request
import json

app = Flask("JobScraper")


def load_jobs():
    with open("jobs.json", "r") as f:
        return json.load(f)

# /BLUEPRINT


# 👇🏻 YOUR CODE 👇🏻:
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    with open("jobs.json", "r", encoding="utf-8") as f:
        jobs = json.load(f)
    result = []
    for job in jobs:
        if keyword in job["title"]:
            result.append(job)
    return render_template("search.html", jobs=result)
# /YOUR CODE


# BLUEPRINT | DONT EDIT

if __name__ == "__main__":
    app.run()

# /BLUEPRINT
