import json
from ET import engine
from flask import Flask, request, jsonify, abort


t = 1
while t:
    tok = input("- ")
    if tok != "종료":
        answer = engine(tok)
        print(answer)
    
    elif tok == "종료":
        t=0
