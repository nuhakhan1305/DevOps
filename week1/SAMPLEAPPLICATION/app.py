from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Welcome</title>
    </head>
    <body style="text-align:center; font-family:Arial; margin-top:100px;">

        <h1>Welcome to Event Registration System</h1>

        <p>Click the link below to register for the event.</p>

        <a href="/register">Go to Registration Form</a>

    </body>
    </html>
    """

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/success", methods=["POST"])
def success():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    event = request.form["event"]

    return render_template(
        "success.html",
        name=name,
        email=email,
        phone=phone,
        event=event
    )

if __name__ == "__main__":
    app.run(debug=True, port=5001)