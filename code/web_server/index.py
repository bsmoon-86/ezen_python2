# flask 라이브러리 로드 
from flask import Flask

# Flask Class 생성
# Flask(파일의 이름)
# __name__ : 해당하는 파일의 이름
app = Flask(__name__)

# @ 네이베이션 : 특정한 주소로 요청이 들어온다면 바로 아래에 있는 함수를 호출
# route("/") : 해당하는 주소로 요청이 들어오면 
# @app.route("/") : locahost:8000/로 요청이 들어온다면 바로 아래의 함수를 호출
@app.route("/")
def index():
    return 'Hello world'

@app.route("/second")
def second():
    return 'Second Page'


# 서버를 실행
app.run(port=8000)