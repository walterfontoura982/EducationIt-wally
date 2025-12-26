from flask import Flask, jsonify, request

def create_app():
    app = Flask(__name__)

    orders = [
        {"id": 1, "item": "Libro", "quantity": 1},
        {"id": 2, "item": "Teclado mecánico", "quantity": 2},
    ]

    @app.route("/health", methods=["GET"])
    def health():
        return jsonify({"status": "Super -- >>ok"}), 200

    @app.route("/orders", methods=["GET"])
    def list_orders():
        return jsonify(orders), 200

    @app.route("/orders", methods=["POST"])
    def create_order():
        data = request.json or {}
        new_id = max(o["id"] for o in orders) + 1 if orders else 1
        order = {
            "id": new_id,
            "item": data.get("item", "unknown"),
            "quantity": data.get("quantity", 1),
        }
        orders.append(order)
        return jsonify(order), 201

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8000)
    
    
''' No andaba por esto 
🔴 Entonces… ¿por qué desde el navegador no responde?
1️⃣ Security Group de la EC2 ❗ (ESTE ES EL MOTIVO REAL)

Aunque Flask esté perfecto, AWS bloquea el puerto 8000 por defecto.

Tenés que habilitarlo en el Security Group de la instancia.

✔️ Regla necesaria

En el Security Group:

Tipo	Protocolo	Puerto	Origen
Custom TCP	TCP	8000	0.0.0.0/0

SSH  in aws
Type            Protocol    Port range    Description
Custom TCP      TCP         8000            0.0.0.0/0    
SSH             TCP         22              Mi Ip/32 o 0.0.0.0/0


    
'''