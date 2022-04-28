from asyncio import threads
from distutils.log import debug
from pickle import TRUE
from flask import Flask
from views import views
from waitress import serve



app = Flask(__name__, static_folder="static")
app.register_blueprint(views, url_prefix="/")


if __name__ == '__main__':
    app.run(debug=True, port=8080, host="0.0.0.0")
    

    


