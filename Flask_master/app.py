from flask import Flask, request, render_template
#request takes how the request whether it it get or post web info
app = Flask(__name__)

#@ signifies a decorator - way to wrap  a function and modify its behaviours. In flask we are connecting
# a url to the return in a fn
@app.route('/')

def index():
    return "Method used %s" %request.method

@app.route('/postfn', methods = ['GET', 'POST'])
def postfn():
    if request.method == 'POST':
        return 'You are using POST'
    else:
        return 'You are using Get'
@app.route('/tuna')
def tuna():
    return '<h2> Sample text <h2>'

@app.route('/profile/<username>')
def profile(username):
    return render_template("profile.html",name =username)
@app.route('/post/<int:postid>')
def postid(postid):
    return '<h2> Post id is %s<h2>' %postid

#It says kick off the web server
if __name__ =="__main__":
    app.run(debug= True)
