from flask import Flask

app = Flask(__name__)

shapes_list = {1:"cone", 2:"circle" , 3:"square", 4:"kite" }


@app.route('/')
def index():
    return 'Hello world'

@app.route('/whereami')
def whereami():
    return 'Ghana!'

@app.route('/getallitems')
def shapes():
    return shapes_list




    


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

