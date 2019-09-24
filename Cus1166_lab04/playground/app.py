# '/': This route should display a static welcome message. The message should be defined in the
# template index.html
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# /welcome/<string:student_name> This message should display a welcome message that
# includes the student_name specified in the route. The route should render the template
# welcome.html .
@app.route("/welcome/<string:student_name>")
def welcome(student_name):
    return render_template("welcome.html", student_name=student_name)


# /roster/<int:grade_view> :
# To implement this route you need to first define a global variable that stores a list of tuples -
# name this variable class_roster . Each tuple in the list must have three elements; a
# student's name, a student's grade and a student's class standing (i.e. 'Freshman',
# 'Sophomore', junior', 'Senior'). Populate this variable with student information (create at
# least 7 student entries, use dummy data).
class_roster = [
    ('Neetu', 'A+', 'Senior'),
    ('Jagu', 'A+', 'Senior'),
    ('Alex', 'C+', 'Senior'),
    ('Dilpreet', 'A-', 'Senior'),
    ('Sabrina', 'A', 'Senior'),
    ('John', 'A', 'Senior'),
    ('Mo', 'A+', 'Senior'),
]


@app.route("/roster/<int:grade_view>")
def roster(grade_view):
    return render_template("roster.html", class_roster=class_roster, grade_view=grade_view)


if __name__ == '__main__':
    app.run()
