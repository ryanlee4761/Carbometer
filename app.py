from flask import Flask, render_template, request, redirect, url_for, session, Blueprint


def create_app(test_config=None):
    foodemissions = [6.62, 2.45, 1.72, 1.26,
                     0.89, 0.72, 0.16, 0.11, 0.07, 0.03]
    clothingemissions = [4.6, ]
    # 2.1 kg co2 cotton, 5.5 kg co2 polyester
    #4.6, 12.1
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

    @app.route("/clothing")
    def clothing():
        return render_template('clothing.html')

    @app.route("/food")
    def food():
        return render_template('food.html')

    @app.route("/utilities")
    def utilities():
        return render_template('utilities.html')

    bp = Blueprint('more', __name__, url_prefix='/more')

    @bp.route("/more/about")
    def about():
        return render_template('more/about.html')

    @bp.route("/more/action")
    def action():
        return render_template('more/action.html')

    @bp.route("/more/sources")
    def sources():
        return render_template('more/sources.html')

    app.register_blueprint(bp)

    # got lazy, just commented out the old python stuff, need to refer to it later
    # for when i add the questionnaire
    """@app.route("/foodquestionnaire", methods=("GET", "POST"))
    def foodquestionnaire():
        if request.method == "POST":
            session['foodlist'] = [
                request.form['beef'],
                request.form['pork'],
                request.form['poultry'],
                request.form['cheese'],
                request.form['eggs'],
                request.form['rice'],
                request.form['legumes'],
                request.form['carrots'],
                request.form['potatoes'],
            ]
            return redirect(url_for('foodresults'))
        session['foodlist'] = {}
        return render_template('foodquestionnaire.html')
        # fix 2 2 2 2 2 2 2  2 2 bug
        # round numbers??

    @app.route("/foodresults")
    def foodresults():
        foodlist = session.get('foodlist', None)
        foodco2 = 0
        if foodlist != {}:
            for i in range(len(foodemissions)-1):
                foodco2 += int(foodlist[i]) * foodemissions[i]
            return render_template('foodresults.html', foodco2=foodco2)
        else:
            return redirect('foodquestionnaire')

    @app.route("/clothingquestionnaire", methods=("GET", "POST"))
    def clothingquestionnaire():
        if request.method == "POST":
            session['clothingdict'] = [
                request.form['clothing_top'],
                request.form['clothing_bottom'],
                request.form['clothing_shoes'],
                request.form['clothing_outerwear'],
            ]
            session['clothingoften'] = int(request.form['clothing_often'])
            # laundry habits

            return redirect('clothingresults')
        session['clothingdict'] = {}
        session['clothingoften'] = None
        # laundry habits
        return render_template('clothingquestionnaire.html')

    @app.route("/clothingresults")
    def clothingresults():
        clothingdict = session.get('clothingdict', None)
        clothingoften = session.get('clothingoften', None)
        clothingco2 = 0
        if clothingdict != {}:
            for i in range(len(clothingdict)-1):
                # * something idk wait for jessica
                # * clothingemissions[i] but fill in list
                clothingco2 += int(clothingdict[i]) * clothingoften

            # laundry habits
            return render_template('clothingresults.html', clothingco2=clothingco2)
        else:
            return redirect('clothingquestionnaire')

    @app.route("/utilitiesquestionnaire", methods=("GET", "POST"))
    def utilitiesquestionnaire():
        if request.method == "POST":
            session['kwh_pm'] = int(request.form['kwh_pm'])
            session['weeklydrive'] = int(request.form['weeklydrive'])
            session['weeklybus'] = int(request.form['weeklybus'])
            session['carpoolers'] = int(request.form['carpoolers'])
            session['busmode'] = request.form['busmode']
            return redirect('utilitiesresults')
        session['kwh_pm'] = None
        session['weeklydrive'] = None
        session['weeklybus'] = None
        session['carpoolers'] = None
        session['busmode'] = None
        return render_template('utilitiesquestionnaire.html')

    @app.route("/utilitiesresults")
    def utilitiesresults():
        kwh_pm = session.get('kwh_pm', None)
        weeklydrive = session.get('weeklydrive', None)
        weeklybus = session.get('weeklybus', None)
        carpoolers = session.get('carpoolers', None)
        busmode = session.get('busmode', None)
        busfactor = 0
        utilitiesco2 = 0

        if not (busmode == None or weeklydrive == None):
            # fix radio buttons
            if busmode == "bus":
                busfactor = 0.64
            elif busmode == "light":
                busfactor = 0.36
            elif busmode == "heavy":
                busfactor = 0.22

            utilitiesco2 += kwh_pm * 12 * .92
            utilitiesco2 += weeklydrive * .89 / (carpoolers+1)
            utilitiesco2 += weeklybus * busfactor

            return render_template('utilitiesresults.html', utilitiesco2=utilitiesco2)
        else:
            return redirect('utilitiesquestionnaire')"""

    return app


app = create_app()
