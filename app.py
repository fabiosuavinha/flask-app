# -*- coding: utf -8 -*-

import os

from flask import request
from flask import Flask
app = Flask(__name__)



@app.route('/metallica', methods=['POST','GET'])
def metal():

	MUSICA_DO_METALLICA = ''
	
	def verificar_se_musica_e_do_metallica(musica):
		

		MUSICA_DO_METALLICA=[
			'Enter Sandman',
			'Fuel',
			'Murder One',
		]

		MUSICA_DO_METALLICA = [ musica.lower() for musica in MUSICA_DO_METALLICA ]	
		
		if musica.lower() in MUSICA_DO_METALLICA:
			return True
		else:
			return False

	if request.method == 'POST':

		musica = request.form['nome-musica']

		if verificar_se_musica_e_do_metallica(musica):
			MUSICA_DO_METALLICA = 'E do METALLICA'
		else:
			MUSICA_DO_METALLICA = 'NAO E!'				

	
	return '''
         
		<form action='/metallica' method='POST'>
		<label for ='nome-musica'>Nome da Musica</label>
		<input type='text' id='nome-musica' name='nome-musica'>
		<button>Ver se a musica e do Metallica |_| </boutton> 

		</form>	

		<p>{}</p>


		'''.format(MUSICA_DO_METALLICA)


@app.route("/")
def hello():
    
    return '''

    <style>
     
       img{
          width: 500px;
          height: 400px;
         } 	
       
       .imagem-grande{
       		width: 500px;
       		height: 500px;
		}

       .imagem-pequena{
             width: 250px;
             height: 200px;

       }		
       	


    </style>



    <h1>Flask App</h1>
    <hr>
    <h2> Meu primeiro aplicativo em Flask</h2>
    <h3> Cafe...Com Metallica!</h3>

    <img class ='imagem-pequena' src='https://i.ebayimg.com/images/g/570AAOSwZQRYhLCO/s-l300.jpg'>
    <img class ='imagem-pequena' src='https://images.pexels.com/photos/8911/pexels-photo.jpg?cs=srgb&dl=beans-caffeine-coffee-8911.jpg&fm=jpg'>

    <p> by: <strong> Fabio Suavinha </strong></p>

    '''

if __name__ == "__main__":
	
	os.environ['FLASK_APP'] = 'app'
	os.environ['FLASK_ENV'] = 'development'

	app.run()  