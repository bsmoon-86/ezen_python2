# flask 라이브러리 로드 
from flask import Flask, render_template, request
# random 라이브러리 로드 
import random

# Flask Class 생성
# Flask(파일의 이름)
# __name__ : 해당하는 파일의 이름
app = Flask(__name__)

# @ 네비게이션 : 특정한 주소로 요청이 들어온다면 바로 아래에 있는 함수를 호출
# route("/") : 해당하는 주소로 요청이 들어오면 
# @app.route("/") : localhost:8000/로 요청이 들어온다면 바로 아래의 함수를 호출
@app.route("/")
def index():
    # return 'Hello world'
    return render_template('index.html')

@app.route("/second")
def second():
    return 'Second Page'

# login api 생성
# localhost:3000/login 주소로 요청 시
@app.route("/login")
def login():
    return render_template('login.html')

@app.route('/login2')
def login2():
    # 유저가 입력한 데이터를 서버에서 변수에 대입
    # get방식으로 데이터를 보낸 경우에는 request안에 args키 값에 데이터가 존재
    print(request.args)
    input_id = request.args['_id']
    input_pass = request.args['_pass']
    print(input_id, input_pass)
    # return (input_id, input_pass)
    # if 조건식
    if (input_id == 'test') & (input_pass == '1234'):
        return "로그인 성공"
    else:
        return "로그인 실패"
    
@app.route('/main')
def main():
    return render_template('game.html')

# localhost:3000/game [post] 형태의 주소를 생성
@app.route("/game", methods=['post'])
def game():
    # 유저가 바위,가위, 보 중 선택한 값을 변수에 대입
    input_user = request.form['user']
    print(input_user)
    # 서버가 가위 바위 보 중 랜덤하게 선택
    _list = ['바위', '가위', '보']
    choice_list = random.choice(_list)

    # 무승부 경우
    if input_user == choice_list:
        result = '무승부'
    # 유저가 바위를 선택하였을때
    elif input_user == '바위':
        if choice_list == '가위':
            result = '승리'
        else:
            result = '패배'
    elif input_user == '가위':
        if choice_list == '보':
            result = '승리'
        else : 
            result = '패배'
    elif input_user == '보':
        if choice_list == '바위':
            result = '승리'
        else:
            result = '패배'
    return render_template('result.html', res = result)

# 서버를 실행
app.run(host = '0.0.0.0' ,port=3000)