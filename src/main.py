import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request, jsonify
from flask_session import Session


# MVP 1 (ASAD) - NLP Intent Router
from api.ussd_assistant.routes import ussd_assistant_bp

# MVP 2 (SMS Guard)
from api.sms_guard.logic.routes import sms_guard_bp

# MVP 3 (KADA)
from api.kada.logic.routes import kada_bp

# Get the absolute path to the directory containing this script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the paths to the templates and static folders relative to the current_dir
templates_dir = os.path.join(current_dir, '..', 'templates')
static_dir = os.path.join(current_dir, '..', 'static')

app = Flask(__name__, template_folder=templates_dir, static_folder=static_dir)
app.secret_key = 'Masa123kc'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# ---- Register Blueprints ----
app.register_blueprint(ussd_assistant_bp, url_prefix="/asad")          # Handles POST /asad (NLP intent)
app.register_blueprint(sms_guard_bp, url_prefix='/sms-guard')
app.register_blueprint(kada_bp, url_prefix='/kada')

# ---- Home & Project Pages ----
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about_page():
    return render_template('about.html')
    
@app.route('/vibe-coding')
def vibe_coding_page():
    return render_template('vibe_coding.html')

@app.route('/project/<project_name>')
def project_page(project_name):
    # Removed other project info, only keeping relevant ones for now
    project_info = {
        "smart-ussd": {
            "title": "Smart USSD Assistant",
            "description": "An intelligent layer over USSD menus using NLP."
        },
        "sms-fraud-detection": {
            "title": "SMS Fraud Detection",
            "description": "A lightweight ML model that flags scam messages locally."
        },
        "kada": {
            "title": "KADA SMS Booking System",
            "description": "An intelligent SMS-based booking system for rides and deliveries."
        }
    }

    if project_name not in project_info:
        return render_template(
            'project_detail.html',
            project_title="Not Found",
            project_description="Project does not exist.",
            project_name=project_name
        )

    data = project_info[project_name]
    return render_template(
        'project_detail.html',
        project_title=data['title'],
        project_description=data['description'],
        project_name=project_name
    )

# ---- ASAD UI Page ----
@app.route("/asad", methods=["GET"])
def asad_page():
    return render_template("asad/index.html")

# ---- SMS Guard UI Page ----
@app.route("/sms-guard", methods=["GET"])
def sms_guard_ui():
    return render_template("sms_guard/index.html")

# ---- KADA UI Page ----
@app.route("/kada", methods=["GET"])
def kada_ui():
    return render_template("kada/index.html")

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)


