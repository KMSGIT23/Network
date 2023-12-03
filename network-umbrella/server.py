from flask import Flask, render_template
import connectDB
import qrscanner

app = Flask(__name__)

@app.route('/')
def home():
    try:
        scan = qrscanner
        insert = connectDB.insert_sql(scan)
        results = connectDB.select_sql()
        return render_template('web.html', results=results)
    except Exception as e:
        print(f"Error: {e}")
        return "error"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
