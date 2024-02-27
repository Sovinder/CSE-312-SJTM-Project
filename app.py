from flask import Flask
from flask import render_template
from flask import make_response
app = Flask(__name__,static_url_path='/static')

@app.after_request
def add_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    return response

@app.route("/")
def home():
    response = make_response(render_template('index.html'))
    response.headers['Content-Type'] = 'text/html'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080,debug=False)