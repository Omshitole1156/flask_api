from flask import Flask 
app = Flask(__name__) 
 
@app.route("/") 
def home(): 
    return "Hello from Cloud PaaS using Render!" 
 
if __name__ == "__main__": 
    app.run() 