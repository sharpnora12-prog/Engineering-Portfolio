from flask import Flask, render_template
from datetime import date
import json

def load_projects():
    with open("data/projects.json","r",encoding="utf-8") as file:
        return json.load(file)
def load_experiences():
    with open("data/experiences.json", "r", encoding="utf-8") as file:
        return json.load(file)
app = Flask(__name__)


@app.route("/")
def home():
    projects=load_projects()

    return render_template(
        "index.html",
        projects=projects
    )
        



@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/experience")
def experience():

    experiences = load_experiences()

    experiences_sorted = sorted(
        experiences,
        key=lambda x: x["start_date"],
        reverse=True
    )

    return render_template(
        "experience.html",
        experiences=experiences_sorted
    )


@app.route("/projects")
def projects():
    projects=load_projects()
    return render_template("projects.html",projects=projects)
@app.route("/projects/<slug>")
def project(slug):
    projects=load_projects()
    for project in projects:
        if project["slug"] == slug:
            return render_template("project.html",project=project)

    return "Project not found", 404

@app.route("/toolbox")
def toolbox():
    return render_template("toolbox.html")


@app.route("/resume")
def resume():
    return render_template("resume.html")


if __name__ == "__main__":
    app.run(debug=True)

