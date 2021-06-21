import datetime
from flask.json import jsonify
def setResponseFrame(description, data):
    return jsonify(
        {
            'date': str(datetime.datetime.today()),
            'description': description,
            'data': data
        }
    )