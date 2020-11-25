import json
import sys
sys.path.append('C:/Users/obybk/OneDrive/바탕 화면/AI/sentimental_chatbot/model/ET.py')

from flask import Flask, request, jsonify, abort
app = Flask(__name__)
@app.route('/answer', methods=['POST'])
def index():
    body = request.get_json()
    responseBody={
        "version": "2.0",
        "template":{
            "outputs": [
                {
                    "simpleText": {
                        "text": engine(body['userRequest']['utterance'])
                    }
                }
            ]
        }
    }
    return responseBody
    
t = 1
while t:
    tok = input("- ")
    if tok != "종료":
        answer = engine(tok)
        print(answer)
    
    elif tok == "종료":
        t=0
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)