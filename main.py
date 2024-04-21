# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask,request,jsonify
app=Flask(__name__)
@app.route('/via_postman',methods=['POST'])
def calculator():
    if request.method=='POST':
        op=request.json['op']
        n1=int(request.json['n1'])
        n2 = int(request.json['n2'])
        if op=='add':
            result= 'Result is '+str(n1+n2)
        if op=='sub':
            result= 'Result is '+str(n1-n2)
        if op=='mul':
            result= 'Result is '+str(n1*n2)
        if op=='divide':
            result= 'Result is '+str(n1/n2)
        return jsonify(result)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
