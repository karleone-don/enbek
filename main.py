from flask import Flask, render_template, request, jsonify
import TPFs

app = Flask(__name__)

@app.route("/process", methods=["POST"])
def process():
    data = request.get_json()
    gender = data["gender"]
    age = data["age"]
    education = data["education"]
    experience = data["experience"]
    information = data["information"]
    project = data["project"]
    time_management = data["time_management"]
    situation = data["situation"]

    conclusion, advice = TPFs.text_generation(
                        gender, 
                        age, 
                        education, 
                        experience, 
                        information, 
                        project,
                        time_management,
                        situation
                        )

    return jsonify({'status': 'success', 'conclusion': conclusion, 'advice': advice})

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/kk")
def index_kz():
    return render_template("index_kk.html")

if __name__ == "__main__":
    app.run()