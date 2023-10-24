from flask import Flask, render_template, request, jsonify
import pymysql

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")  # 웹 페이지의 메인 화면을 렌더링하여 반환합니다.

@app.route('/join', methods=["POST"])
def join_post():
    # POST 요청으로부터 데이터를 가져옵니다.
    pid = request.form['pid']  # 클라이언트에서 'pid' 파라미터를 가져와서 아이디로 저장합니다.
    pname = request.form['pname']  # 클라이언트에서 'pname' 파라미터를 가져와서 이름으로 저장합니다.
    pposition = request.form['pposition']  # 클라이언트에서 'pposition' 파라미터를 가져와서 포지션으로 저장합니다.
    pdate = request.form['pdate']  # 클라이언트에서 'pdate' 파라미터를 가져와서 날짜로 저장합니다.
    pgrade = request.form['pgrade']  # 클라이언트에서 'pgrade' 파라미터를 가져와서 등급으로 저장합니다.

    # MySQL 데이터베이스에 연결합니다.
    conn = pymysql.connect(host='localhost', user='kms', password='1234567', db='kkk')
    cur = conn.cursor() 

    # SQL 쿼리와 데이터를 설정합니다.
    sql = "insert into giants_player values(%s, %s, %s, %s, %s)"
    data = (pid, pname, pposition, pdate, pgrade)

    # 데이터베이스에 데이터를 삽입합니다.
    cur.execute(sql, data)
    conn.commit()

    # 데이터베이스 연결을 닫습니다.
    conn.close()

    # 클라이언트에게 JSON 응답을 반환합니다.
    return jsonify({'msg' : '등록 완료!'})  # 클라이언트에게 "등록 완료!" 메시지를 JSON 형식으로 반환합니다.

if __name__ == "__main__":
    # 애플리케이션을 0.0.0.0 주소에서 애플리케이션을 실행합니다.
    app.run(host='0.0.0.0')
