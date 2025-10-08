from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Define la ruta y los verbos HTTP permitidos
@app.route('/api/resource', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_resource():
    http_verb = request.method
    # Lógica para manejar los diferentes verbos HTTP
    if http_verb == 'GET':
        response_data = {
            "status": "success",
            "message": "Datos obtenidos con exito.",
            "data": {"id": 1, "name": "Ejemplo GET"}
        }
        return jsonify(response_data), 200
    # ... otras lógicas para POST, PUT, DELETE
    else:
        return jsonify({"status": "error", "message": "Verbo HTTP no soportado"}), 405

# Verifica si la aplicación se está ejecutando en Render
if __name__ == '__main__':
    # Usa el puerto que Render asigna, si está disponible, o usa 8080
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
