from flask import Flask, jsonify, request

# Initialise the app
app = Flask(__name__)

#Define what the app does
@app.get("/greet")
def index():
    fname = request.args.get("fname")
    lname = request.args.get("lname")
    if not fname and not lname:
        return jsonify({"status": "error"})
    elif fname and lname:
        response = {"data": f"Hello, {fname} {lname}!"}
    elif not fname:
        response = {"data": f"Hello, {lname}!"}
    else:
        response = {"data": f"Hello, {fname}!"}
    return jsonify(response)
