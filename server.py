from flask import Flask, render_template, redirect, url_for

from forms import TeamForm, ProjectForm

from model import db, connect_to_db, User, Team, Project

USER_ID = 1

app = Flask(__name__)
app.secret_key = "keep this secret"

@app.route("/")
def home():
    team_form = TeamForm()
    project_form = ProjectForm()
    project_form.update_teams(User.query.get(USER_ID).teams)
    return render_template("home.html", team_form=team_form, project_form=project_form)

@app.route("/add-team", methods=["POST"])
def add_team():
    team_form = TeamForm()

    if team_form.validate_on_submit():
        print(team_form.team_name.data)

    return redirect(url_for("home"))


@app.route("/add-project", methods=["POST"])
def add_project():
    project_form = ProjectForm()
    project_form.update_teams(User.query.get(USER_ID).teams)

    if project_form.validate_on_submit():
        print(project_form.project_name.data)
        print(project_form.description.data)
        print(project_form.completed.data)
        print(project_form.team_selection.data)
    
    return redirect(url_for("home"))





if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug = True)

