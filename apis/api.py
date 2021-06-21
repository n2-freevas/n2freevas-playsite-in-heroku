from flask import Blueprint
from apis.api_handler.api_responseFrame import *

app = Blueprint("api",__name__)

@app.route("/v1")
def v1():
    return setResponseFrame(
        description = "You access",
        data = {
            "test": "string-v1",
            "test2": 123
        }    
    )
