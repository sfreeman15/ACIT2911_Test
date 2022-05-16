
from flask import Flask, render_template, request
import calFunctions
import os

app=Flask(__name__)
@app.route("/",methods=['POST','GET'])


def calculate():
    result=''
    calList=[]
   
    if request.method=='POST' and 'num1' in request.form and 'num2' in request.form:
        num1=float(request.form.get('num1'))
        operator=request.form.get('Operator')
        num2=float(request.form.get('num2'))
        calList.append(num1)
        calList.append(num2)
        if operator=="Addition":
            calList.append("+")
            result=round((calFunctions.addFunction(num1,num2)),2)
        elif operator=="Subtraction":
            calList.append("-")
            result=round((calFunctions.subtractTwoNum(num1,num2)),2)
        elif operator=="Multiplication":
            calList.append("x")
            result=round((calFunctions.multiplyTwoNum(num1,num2)),2)
        elif operator=="Division":
            calList.append("/")
            result=calFunctions.divideTwoNum(num1,num2)
        result=str(calList[0])+" "+str(calList[2])+ " "+ str(calList[1])+" = "+str(result)
    return render_template("index.html", message=result)
   
if __name__=="__main__":
    app.secret_key="ItIsASecret&$$$$@"
    app.debug=True
    # Heroku will set the PORT environment variable for web traffic
    port = os.environ.get("PORT", 5000)
    app.run(debug=False, host="0.0.0.0",port=port)# set debug=False before deployment