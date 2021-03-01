from flask import Blueprint, request, jsonify, Response, abort
from microservice.adapters import RandomForestModel, InvalidInput
from .error import  InvalidRequest

predict_blueprint = Blueprint("predict", __name__)
model = RandomForestModel()

@predict_blueprint.route("/predict", methods=["POST"])
def predict():
    data = validate_request(request)
    model.validate_data(data)
    res = model.predict(data)
    return jsonify(res)



def validate_request(request):
    content_type = request.headers.get("Content-Type")
    if (content_type != "application/json"):   
        raise InvalidRequest("Content-type must be 'application/json' not '{}'".format(content_type))
    data = request.get_json()
    return data

@predict_blueprint.errorhandler(InvalidInput)
@predict_blueprint.errorhandler(InvalidRequest)
def handle_bad_request(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response