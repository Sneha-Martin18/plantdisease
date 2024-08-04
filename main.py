from flask import *
from public import public
from admin import admin
from farmer import farmer

app=Flask(__name__)
app.secret_key="core"
app.register_blueprint(public)
app.register_blueprint(admin)
app.register_blueprint(farmer)

app.run(debug=True,port=5009)


