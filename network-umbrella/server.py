from flask import Flask, render_template
import connectDB
import cv2
from pyzbar.pyzbar import decode



app = Flask(__name__)

@app.route('/')
def home():
    try:
        results = connectDB.select_sql()
        return render_template('web.html', results=results)
    except Exception as e:
        print(f"Error: {e}")
        return "error"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
