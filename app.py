from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Debugging: Print message in the terminal (You can replace this with database storage or email sending)
        print(f"New Message from {name} ({email}): {message}")
        
        return "Message sent successfully!"

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
