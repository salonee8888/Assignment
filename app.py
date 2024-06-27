from flask import Flask

app = Flask(_name_)

@app.route('/')
def home():
    return 'Hello, World!'

if _name_ == '_main_':
    app.run(debug=True)

@app.route('/new-feature;')
def new_feature():
    return 'this is a new feature!'
