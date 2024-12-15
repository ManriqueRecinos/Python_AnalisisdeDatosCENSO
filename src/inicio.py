from flask import Flask, jsonify, request
from app import get_data_poblacion

app = Flask(__name__)

@app.route("/api/poblacion", methods=['GET'])
def get_poblacion():
    data = get_data_poblacion()
    
    return jsonify({
       # "headers": headers,
        "data": data
    })




if __name__=='__main__':
    app.run(debug=True)