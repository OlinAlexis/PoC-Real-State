from flask import Flask, render_template

# store the flask instance
# instantiating the flask object
app = Flask(__name__)


# url to view website
@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/residential')
def residential():
    return render_template("residential.html")


if __name__ == "__main__":
    app.run(debug=True)
