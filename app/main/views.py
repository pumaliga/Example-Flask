import json
import os

from flask import render_template, jsonify, request, flash, redirect, url_for
from flask_login import login_required
from werkzeug.utils import secure_filename

from . import main
from .. import ALLOWED_EXTENSIONS, UPLOAD_FOLDER
from ..models import session, Category


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@main.route('/add/category', methods=['GET', 'POST'])
@login_required
def add_category():
    if request.method == 'POST':

        try:
            data = request.form
            name = data.get('name')
            description = data.get('description')

            # if 'avatar' not in request.files:
            #     flash('No file part')
            #     return redirect(url_for('main.add_category'))

            file = request.files.get('avatar')

            if file.filename == '':
                flash('No selected file')
                return redirect(url_for('main.add_category'))

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(UPLOAD_FOLDER, filename))
                with session() as s:
                    new_category = Category(avatar=filename, name=name,
                                            description=description)
                    s.add(new_category)
                    s.commit()
                return redirect(url_for('main.add_category'))

        except KeyError:
            return jsonify({'saved': 'No file'})

    return render_template('add_category.html')


@main.route('/add/product', methods=['GET', 'POST'])
def add_product():
    with session() as s:
        categories = s.query(Category).all()

    return render_template('add_product.html', categories=categories)


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


