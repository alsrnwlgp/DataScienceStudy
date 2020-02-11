#pip install flask-mysql

from flask import Flask, render_template, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
#MySQL DB를 설정하기
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
app.config['MYSQL_DATABASE_DB'] = 'test'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/")
def index():
    return render_template('index.html') #폴더이름이 templates인 곳에서 가져옴

@app.route("/write", methods = ['GET', 'POST'])
def write():
    if request.method == 'GET':
        return render_template('writeform.html')
    else:
        vals = request.form['title'],request.form['content'],request.form['writer']
        #database에 저장하기
        conn = mysql.connect() #mysql data에 접근
        cursor = conn.cursor() #명령어 입력하는 공간
        cursor.execute("insert into board(title, content, writer) values(%s, %s, %s)", vals)
        conn.commit()
        conn.close()
        return render_template('index.html')

@app.route("/list")
def list():
    return "list"

if __name__ == "__main__":
    app.run(debug=True) #개발의 편의성을 위해 debug=True를 사용함 계속 업데이트 해줌

