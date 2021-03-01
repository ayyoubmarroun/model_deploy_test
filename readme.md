# Data Engineer Test

## ML
### Exercice
Our goal is to convert this notebook experiment into a real python application, able to perform predictions in real time, reading input features for the model via a HTTP request.

The application should use Flask micro web framework (or similar technology) for reading the HTTPrequest.

The HTTP response for the /predict route should be a JSON serialized array with the result of the prediction, in the same order as the array of input features.

### Solution
The solution is a microservice that exposes a sklearn RandomForest model to an HTTP request via flask.
There is some basic data validation before the predictions being done. The output of the request is in fact the input plus the predicted field *"Target"*.
### Structure
The microservice is implemented using hexagonal architecture.


### Test
Before testing anything, please set up correctly your environment.
#### Environment
- You'll need python 3.5+
- Install requirements

To run the app, simply go to src/microservice and run: `flask run`.

To test simply POST to `/predict` with `Content-Type` as `application/json` and all parameters correctly providen.

