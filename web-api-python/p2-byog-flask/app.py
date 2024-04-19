from types import MethodType
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.get("/")
def index():
    """
    TODO: Render the home page provided under templates/index.html in the repository
    """
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    """
    TODO:
    1. Capture the word that is being searched
    2. Seach for the word on Google and display results
    """
    args = request.form.get("q")
    print(request.form.get("q"))
    print(request.form.get("search_button"))
    if request.form.get('search_button') == 'search_btn':
        return redirect(f"https://google.com/search?q={args}")
    elif request.form.get('lucky_button') == 'lucky_btn':
        return redirect(f"https://google.com/search?q={args}&btnI=1")
    return "TODO"


if __name__ == "__main__":
    app.run()
