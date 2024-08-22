from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/personas', methods=['GET'])
def obtener_personas():
    # Lista de nombres de personas
    lista_personas = ["Lina", "Javier", "Jesus", "Santiago", "Anderson"]
    # Convertir la lista a JSON y devolverla
    return jsonify(lista_personas)

if __name__ == '__main__':
    app.run(debug=True)
