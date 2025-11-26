from flask import Flask, request, jsonify

app = Flask(__name__)

def simple_ai(prompt: str) -> str:
    if not prompt:
        return "No prompt provided."
    p = prompt.lower()
    if any(x in p for x in ("hola", "buenos", "saludos")):
        return "¡Hola! Soy tu asistente simple."
    if len(prompt) < 30:
        return f"Resumen: {prompt}"
    return prompt[::-1]

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "App CI/CD - OK (Atancuri)"}), 200

@app.route("/ai", methods=["POST"])
def ai():
    data = request.get_json() or {}
    prompt = data.get("prompt", "")
    return jsonify({
        "prompt": prompt,
        "response": simple_ai(prompt)
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1001)
