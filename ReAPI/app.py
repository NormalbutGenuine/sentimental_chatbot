import json
import sys
from engineT import engine

from flask import Flask, request, jsonify, abort
app = Flask(__name__)
@app.route('/api/answer', methods=['POST'])
def index():
    body = request.get_json()
    print(body)
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
# while t:
#     tok = input("- ")
#     if tok != "종료":
#         answer = engine(tok)
#         print(answer)
    
#     elif tok == "종료":
#         t=0
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
