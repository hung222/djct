from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def giachoitk():
    return 'giachoitk!'
 
if __name__ == '__main__':
    app.run()