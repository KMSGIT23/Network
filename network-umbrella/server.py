from flask import Flask, render_template, request
import connectDB

app = Flask(__name__)

@app.route('/')
def home():
    try:
        return render_template('main.html')
    except Exception as e:
        print(f"Error: {e}")
        return "error"

@app.route('/borrow.html')
def insert():
    try:
        return render_template('borrow.html')
        i1 = request.form['input1']
        i2 = request.form['input2']
        #insert = connectDB.insert_sql(scan)
    except Exception as e:
        print(f"Error: {e}")
        return "error"

@app.route('/returnback.html', methods=['GET', 'POST'])
def delete():
    try:
        if request.method == 'POST':
            i1 = request.form['input1']
            print(f'입력 값: {i1}')
            delete = connectDB.delete_sql(i1)
        return render_template('returnback.html')

    except Exception as e:
        print(f"Error: {e}")
        return "error"

@app.route('/view')
def view():
    try:
        results = connectDB.select_sql()
        return render_template('web.html', results=results)
    except Exception as e:
        print(f"Error: {e}")
        return "error"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
