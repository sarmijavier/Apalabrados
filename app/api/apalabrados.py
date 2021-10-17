from app.api import bp
from app import db
import json
from flask import request, render_template
from app.models import Numeros, Textos, Caracteres

def filter_special_characters(character):
	
	ascii_number = ord(character)

	if ascii_number > 57 and ascii_number < 65:
		return character
	elif ascii_number > 90 and ascii_number < 97:
		return character


@bp.route('/apalabrados', methods=['GET','POST'])
def post_caracter():

	data = request.form['texto']

	if data.isnumeric():

		number = int(data)
		last_number = db.session.query(Numeros).order_by(Numeros.id.desc()).first()
		acumulado = last_number.acumulado + number

		number_info = {
			'numero': number,
			'acumulado': acumulado
		}

		number_to_save = Numeros()
		number_to_save.from_dict(number_info)
		db.session.add(number_to_save)
		db.session.commit()

		return render_template('apalabrados.html', numbers=data)

	else: 
		first_letter = data[0]
		last_letter = data[-1]

		texto_to_save = {
			'texto': data,
			'inicial': first_letter,
			'final': last_letter
		}

		texto = Textos()
		texto.from_dict(texto_to_save)
		db.session.add(texto)
		db.session.commit()
		
		#special caracters
		special_caracters = list(filter(filter_special_characters, data))
		if len(special_caracters) > 0:

			for character in special_caracters:

				character_info = {
					'caracter': character
				}

				caracter = Caracteres()
				caracter.from_dict(character_info)
				db.session.add(caracter)
				db.session.commit()

		return render_template('apalabrados.html', first_letter=first_letter, last_letter=last_letter, data=data, special_caracters=special_caracters)



