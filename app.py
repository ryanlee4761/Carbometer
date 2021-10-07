from flask import Flask, render_template, flash, request, url_for
#from flaskr.db import get_db

def create_app(test_config = None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    @app.route("/")
    def index():
        return render_template('index.html')

    @app.route("/inputpage", methods=("GET", "POST"))
    def inputpage():
        if request.method == "POST":
            given = request.form['inputfield']
            if int(given) >= 500:
                flash("That's a big number!")
            else:
                flash("Tiny. Go bigger.")
        return render_template('inputpage.html')

    return app

app = create_app()