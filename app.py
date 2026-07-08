from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    return f"""
    <h1>Thank You {name}!</h1>
    <p>Your email: {email}</p>
    <p>Your message: {message}</p>
    """
    
if __name__ == "__main__":
    app.run(debug=True)