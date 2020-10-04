from flask import Flask, jsonify, request, render_template,redirect,session
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_claims
)
import timedelta
import os



app = Flask(__name__)
app.secret_key = "any random string"
app.config['JWT_SECRET_KEY'] = 'cambiar_no_olvidar' 
#app.config["IMAGE_UPLOADS"] = "./static/"
app.config["IMAGE_UPLOADS"] = "/tmp"
jwt = JWTManager(app)



################################### WEB ADMIN ###################################################
#################################################################################################

@app.route('/wa_login', methods=['GET'])
def wa_login():
    _error = request.args.get('error')
    if _error is None:
        _error = 0
    print(_error)
    return render_template('wa_login.html',error = _error)

    
@app.route('/', methods=['GET'])
def wa_inicio():
    _error = request.args.get('error')
    if _error is None:
        _error = 0
    print(_error)
    return render_template('inicio.html')

@app.route('/test', methods=['GET'])
def wa_test():
    return render_template('test.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

