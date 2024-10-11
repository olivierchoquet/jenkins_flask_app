
# Minimal application flask
#
# Get started :
# flask --app hello run
# * Serving Flask app 'hello'
# * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)


from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
    
if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')
