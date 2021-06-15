from django.shortcuts import render
import requests

result=requests.get('https://d338b18c-e9eb-4402-b82d-d31629a3a6ef.mock.pstmn.io//mock')
if(result.status_code==200):
    result=result.json()
    mock_data=result
    result=[(result[i]["Name"]) for i in range(0,len(result))]
    print(result)

def loginreg():
   return render_template('loginreg.html')

def register():
   data=dict()
   if request.method == 'POST':
        data["id"]=len(result)
        data["Name"]=request.form["Name"]
        data["Age"]=request.form["Age"]
        data["DOB"]=request.form["DOB"]
        data["phone"]=request.form["phone"]
        data["id"]=request.form["id"]
        data=json.dumps(data) 
        mock_data.append(data) 
        print(mock_data)
        #print(requests.post('https://d338b18c-e9eb-4402-b82d-d31629a3a6ef.mock.pstmn.io//mock',json=mock))
   return render_template('userlists.html')

def pre():
   pass

def next():
   pass

def user_name(Name):
   if(Name):
    return render_template('user.html' ,name = Name)

def index(request):
    return render(request,'loginreg.html')