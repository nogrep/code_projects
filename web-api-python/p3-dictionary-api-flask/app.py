from flask import Flask, jsonify, request
from model.dbHandler import match_exact, match_like

app = Flask(__name__)
@app.get("/")
def index():
    """
    Default route
    This method will
    1. Provide usage instructions formatted as JSON
    """
    response = {"usage":"/dict?=<word>"}
    return jsonify(response)

@app.get("/dict")
def dict():
    """
    DEFAULT ROUTE
    This method will
    1. Accept a word from request
    2. Try to find an exact match and return it if found
    3. If not found, find all approximate matches and return
    """
    words = request.args.getlist("word")
    if not words:
        response = { "status":"error","words":words,"data":"word not found" }
        return jsonify(response)
    response = {"words":[]}
    for word in words:
        if not word:
            response["words"].append({"status":"error","data":"Not a valid word or no word provided"})
        definition = match_exact(word)
        if definition:
            response["words"].append({"status":"success","data":definition})
        else:
            definition = match_like(word)
            if definition:
                response["words"].append({"status":"partial","data":definition})
            else:
                response["words"].append({"status":"error","data":"word not found"})
    return jsonify(response)

if __name__ == "__main__":
    app.run()

