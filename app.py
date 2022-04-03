from flask import Flask, request, jsonify, render_template
from dummy import output
import pandas as pd
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/resources/hr')
def hr():
    return render_template('hr.html')


@app.route('/resources/it')
def it():
    return render_template('it.html')

@app.route('/resources/legal')
def legal():
    return render_template('legal.html')

@app.route('/resources/pm')
def pm():
    return render_template('project_management.html')

@app.route('/resources/medicine')
def med():
    return render_template('medicine.html')

@app.route('/resources/media')
def media():
    return render_template('media.html')

@app.route('/resources',methods=['POST'])
def resources():
    domain = request.form.get("domain")
    print(domain)
    if(domain == "Human Resources"):
        return render_template('hr.html')
    if(domain == "Information Technology"):
        return render_template('it.html')
    if(domain == "Interior Design"):
        return render_template('interior_design.html')
    if(domain == "Legal"):
        return render_template('legal.html')
    if(domain == "Medicine"):
        return render_template('medicine.html')
    if(domain == "Media"):
        return render_template('media.html')
    if(domain == "Project Management"):
        return render_template('project_management.html')
    if(domain == "Pyschology"):
        return render_template('pyschology.html')
    if(domain == "Culinary"):
        return render_template('chef.html')
    return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)