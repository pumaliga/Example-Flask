import json

from flask import render_template, jsonify
from flask_login import login_required

from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@main.route('/get_info_one')
def get_info_one():
    data_info = [{
        "squadName": "Super hero squad",
        "homeTown": "Metro City",
        "formed": 2016,
        "secretBase": "Super tower",
        "active": True,
        "members": [

            {

               "name": "Molecule Man",
               "age": 29,
               "secretIdentity": "Dan Jukes",
               "powers": [

                    "Radiation resistance",
                    "Turning tiny",
                    "Radiation blast"
              ]
            },
            {
                "name": "Madame Uppercut",
                "age": 39,
                "secretIdentity": "Jane Wilson",
                "powers": [

                    "Million tonne punch",
                    "Damage resistance",
                    "Superhuman reflexes"
                ]
            },
          ]
        }]
    # return json.dumps()
    return jsonify(data_info)


@main.route('/get_info_two')
def get_info_two():
    category = {'en': {
        1: {"category_id": 1,
            "title": "Classic",
            "gradient_color_top": "#8E92FF", "gradient_color_bottom": "#686DF9"},
        2: {"category_id": 2,
            "title": "Only girls",
            "gradient_color_top": "#FF9AC2", "gradient_color_bottom": "#E56E95"},
        3: {"category_id": 3,
            "title": "A game for three",
            "gradient_color_top": "#FCE06E", "gradient_color_bottom": "#FF744E"},
        4: {"category_id": 4,
            "title": "BDSM",
            "gradient_color_top": "#F3ACCD", "gradient_color_bottom": "#9D61FD"}}}

    return jsonify(category)


@main.route('/get_info_three')
def get_info_three():
    person = {
        "surname": "Иванов",
        "name": "Иван",
        "patronymic": "Иванович",
        "birthdate": "01.01.1990",
        "birthplace": "Москва",
        "phone": "8 926 766 48 48"
    }
    # return jsonify(person)
    return json.dumps(person)


