from flask import Flask,render_template,request

app = Flask(__name__)

#simple route
@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"


#route with render 
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return (
        "<h1>Contact Us</h1>"
        "<p>Email: example@example.com</p>"
        "<p>Phone: 123-456-7890</p>"
    )
#HTTP verbs
@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        name = request.form.get("name")
        surname=request.form.get("surname")
        email = request.form.get("email")
        message = request.form.get("message")
        # Process the form data (e.g., save to database, send email, etc.)
        return f"<h1>Thank you, {name} {surname}!</h1><p>We have received your {message}. </p>"

    return render_template("submit.html")
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)