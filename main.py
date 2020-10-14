from flask import Flask, render_template, request, redirect
import mariadb
import sys

app = Flask(__name__)
# main service reservation search


def get_conn():
    conn = mariadb.connect(
        user="root",
        password="000000",
        host="193.123.233.236",
        port=3306,
        database="test"
    )
    return conn


conn = get_conn()
cur = conn.cursor()


@app.route("/reservation")
def reservation():
    return render_template("Form.html")


@app.route("/form", methods=['POST'])
def form():
    if request.method == 'POST':
        reservation_form = request.form
        name = reservation_form['name']
        phone = reservation_form['phone']
        pet = reservation_form['pet']
        service = reservation_form['service']
        p_date = reservation_form['date']
        r_time = reservation_form['time']

        sql = """INSERT INTO reservation
            (name, phone, pet, service, p_date, r_time)
            values ("{}","{}","{}","{}","{}","{}")
        """.format(name, phone, pet, service, p_date, r_time)
        print(sql)
        cur.execute(sql)

        conn.commit()
        conn.close()
        return "예약이 완료되었습니다."
    return render_template("Form.html")
# @app.route("/test")
# def test():
#     sql = "SELECT p_name, p_date FROM pet_sitter"
#     result = ""

#     try:
#         conn = get_conn()
#         cur = conn.cursor()
#         cur.execute(
#                 sql
#                 )
#         result += '<ul>'
#         for(p_name, p_date) in cur:
#                 result += """
#                     <li>이름 = {}</li>
#                     <li>날짜 = {}</li>
#                     """.format(p_name, p_date)
#         result += '</ul>'

#     except mariadb.Error:
#         result = "펫시터 없음"
#         sys.exit(1)
#     finally:
#         if conn:
#             conn.close()
#     return result


@app.route("/")
def main():
    return render_template('main.html')


# @app.route("/service")
# def service():
#     return render_template('service.html')


# @app.route("/reservation")
# def reservation():
#     return render_template('reservation.html')


# @app.route("/search")
# def search():
#     return


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5001)
