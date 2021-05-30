from flask import Flask, request, make_response
from functools import wraps

app = Flask(__name__)

def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # check and see authorization is authorization is correct
        auth = request.authorization
        if auth and auth.username == 'username' and auth.password == 'password':
            return f(*args,**kwargs)
        
        return make_response('Could not verify your login!',401 , {'www-Authenicate': 'Basic realm="login required"'})

    return decorated

@app.route('/')
def index():
    if request.authorization and request.authorization.username == 'username'and request.authorization.password == 'password':
        return "<h2>this is index page</h2>"
    
    return make_response('Could not verify! Please Login!', 401, {'www-Authenticate' : 'Basic realm="Login required"'})

@app.route('/page')
@auth_required
def page():
   return f"<h2>this is page of {request.authorization.username}</h2>"

@app.route('/logout')
@auth_required
def logout():
    return f"<h2>this is logout-page of {request.authorization.username}</h2>"

if __name__ == '__main__':
    app.run(debug=True)

# Notes:-- HTTP basic authentication
'''this is type that authenticate the app by pop in chrome browser or any browser that will be a method simply used the request.authorization and show the pages the user cansel then  this will return [could not verify!!] by useing the make_response give it the values of syntax above'''

''' create a decoretors by from functools import wraps'''