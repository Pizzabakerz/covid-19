from flask import Flask,render_template,jsonify
import json

with open('total_cases.json') as f:
  total_case_data = json.load(f)

with open('recovery_newcase.json') as f:
  recovery_newcase_data = json.load(f)

with open('total_death_recover.json') as f:
  total_death_recover = json.load(f)

with open('new_death_new_case.json') as f:
  new_death_new_case = json.load(f)

with open('final.json') as f:
  final = json.load(f)

app = Flask(__name__)

@app.route('/')
def root():
    return render_template("index.html")

@app.route('/total_cases')
def total_cases():
    return jsonify(total_case_data)

@app.route('/recovery_newcase')
def recovery_newcase():
    return jsonify(recovery_newcase_data)

@app.route('/total_death_recover')
def total_death_recover_fun():
    return jsonify(total_death_recover)

@app.route('/new_death_new_case')
def new_death_new_case_fun():
    return jsonify(new_death_new_case)
  
@app.route('/final')
def final_fun():
    return jsonify(final)

if __name__ == "__main__":
    app.run(debug=True)