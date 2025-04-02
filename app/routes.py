from flask import Blueprint, request, jsonify, render_template
from app.generate_code import generate_code

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.json
        user_code = data.get("code")
        option = data.get("option")
        target_language = data.get("target_language", None)
        error_message = data.get("error", None)

        if not user_code:
            return jsonify({"error": "Please provide code input"}), 400

        generated_code, explanation = generate_code(user_code, option, target_language, error_message)

        return jsonify({"code": generated_code, "explanation": explanation})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
