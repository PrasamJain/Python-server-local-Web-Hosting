# Here we local host a HTML file i.e index.html
# index.html contains a normal template of food website design. And we just demonstrate how we make local server using python with importing FLASK.
# port : 80 and host : 0.0.0.0.

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')
   
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
