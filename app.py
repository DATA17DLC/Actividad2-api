from flask import Flask, jsonify

app = Flask(__name__)
# endpoint para la ruta personas, get es la solicitud para obtener datos
@app.route('/personas', methods=['GET'])
# funcion que da la lista
def obtener_personas():
    # Lista de nombres de personas
    lista_personas = ["Lina", "Javier", "Jesus", "Santiago", "Anderson"]
    # Convertir la lista a JSON y devolverla
    return jsonify(lista_personas)
#verifica si se esta ejecutando directamente o importado
if __name__ == '__main__':
    # inicia el servidor integrado con flask
    app.run(debug=True)
