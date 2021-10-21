from flask import Flask, render_template, request, redirect, url_for, session, Blueprint


def create_app(test_config=None):
    foodemissions = [6.62, 2.45, 1.72, 1.26,
                     0.89, 0.72, 0.16, 0.11, 0.07, 0.03]
    clothingemissions = [30.0, 65.3, 15.7, 44.5]

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

    @app.route("/clothing", methods=("GET", "POST"))
    def clothing():
        clothingdict = None
        clothingco2 = None
        if request.method == "POST":
            clothingdict = [
                request.form['clothing_top'],
                request.form['clothing_bottom'],
                request.form['clothing_shoes'],
                request.form['clothing_outerwear'],
            ]
            clothingco2 = 0
            clothingoften = int(request.form['clothing_often'])
            # set laundry habits var
            for i in range(len(clothingdict)-1):
                clothingco2 += int(clothingdict[i]) * \
                    clothingemissions[i] * clothingoften
            # + laundry habits increment co2

        return render_template('clothing.html', clothingco2=clothingco2)

    @app.route("/food", methods=("GET", "POST"))
    def food():
        foodlist = None
        foodco2 = None
        if request.method == "POST":
            foodlist = [
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
            foodco2 = 0
            for i in range(len(foodemissions)-1):
                foodco2 += int(foodlist[i]) * foodemissions[i]
        return render_template('food.html', foodco2=foodco2)
        # fix same number roudning bug --> round numbers??
        # round to tenths place

    @app.route("/utilities", methods=("GET", "POST"))
    def utilities():
        kwh_pm = None
        weeklydrive = None
        weeklybus = None
        carpoolers = None
        busmode = None
        busfactor = None
        utilitiesco2 = None
        if request.method == "POST":
            kwh_pm = int(request.form['kwh_pm'])
            weeklydrive = int(request.form['weeklydrive'])
            weeklybus = int(request.form['weeklybus'])
            carpoolers = int(request.form['carpoolers'])
            busmode = request.form['busmode']
            busfactor = 0
            utilitiesco2 = 0

        if not (busmode == None or weeklydrive == None):
            if busmode == "bus":
                busfactor = 0.64
            elif busmode == "light":
                busfactor = 0.36
            elif busmode == "heavy":
                busfactor = 0.22

            utilitiesco2 += kwh_pm * 12 * .92
            utilitiesco2 += weeklydrive * .89 / (carpoolers+1)
            utilitiesco2 += weeklybus * busfactor
        return render_template('utilities.html', utilitiesco2=utilitiesco2)

    bp = Blueprint('more', __name__, url_prefix='/more')

    @bp.route("/about")
    def about():
        return render_template('more/about.html')

    @bp.route("/action")
    def action():
        return render_template('more/action.html')

    @bp.route("/sources")
    def sources():
        return render_template('more/sources.html')

    app.register_blueprint(bp)

    # error 404 page?

    return app


app = create_app()
