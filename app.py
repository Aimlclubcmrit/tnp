from flask import render_template,url_for,Flask
app=Flask(__name__,static_url_path='/static')
@app.route("/")
def index():
    return render_template("index.html")
