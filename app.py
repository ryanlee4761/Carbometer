from flask import Flask, render_template, flash, request, redirect, url_for, session
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
    
    @app.route("/foodquestionnaire", methods=("GET", "POST"))
    def foodquestionnaire():
        if request.method == "POST":
            session['responsedict'] = {
                'beef': request.form['beef'], 
                'pork': request.form['pork'], 
                'poultry': request.form['poultry'], 
                'cheese': request.form['cheese'], 
                'eggs': request.form['eggs'], 
                'rice': request.form['rice'], 
                'legumes': request.form['legumes'], 
                'carrots': request.form['carrots'], 
                'potatoes': request.form['potatoes'], 
            }
            return redirect(url_for('results'))
        session['responsedict'] = {}
        return render_template('foodquestionnaire.html')

    @app.route("/foodresults")
    def results():
        responsedict = session.get('responsedict', None)
        #return render_template('results.html')
        if responsedict != {}:
            return responsedict
        else:
            return redirect('foodquestionnaire')

    return app
app = create_app()