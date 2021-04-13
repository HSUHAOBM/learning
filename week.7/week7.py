from flask import Flask,session,request,redirect,render_template
import mysql.connector
from flask_cors import CORS
import json
from flask import jsonify


 # 資料庫
DBhost='localhost'        
DBdatabase='website'
DBuser='root'      
DBpassword='root'

app=Flask(
    __name__,
    static_folder="static",
    static_url_path="/")
CORS(app)

app.config['SECRET_KEY'] = 'laowangaigebi' #key
app.config['JSON_AS_ASCII'] = False



#首頁
@app.route("/")
def home():
    UserAccount = session.get('UserAccount')
    if UserAccount:
        return redirect('/menber')
    else:
        return render_template("index.html")

#註冊
@app.route("/registered", methods=["POST"])
def Registered():
    ReUser=request.form["username"]
    ReAccount=request.form["useraccount"]
    RePassword=request.form["userpassword"]
#     print(ReUser,ReAccount,RePassword)
    if not ReUser.strip() or not ReAccount.strip() or not RePassword.strip():
        return redirect('/error/?message=資料為空白')
    
    try:
        connection = mysql.connector.connect(
        host=DBhost,         
        database=DBdatabase, 
        user=DBuser,      
        password=DBpassword) 

        #檢查是否註冊過
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM user WHERE username= '%s';" % (ReAccount))
        records = cursor.fetchone()

            
        if (records):
            print("註冊過了")
            return redirect('/error/?message=此帳號已註冊使用')

            

        else:
            print("開始新增資料")
            #指令
            sql = "INSERT INTO user (name, username, password) VALUES (%s, %s, %s);"
            new_data = (ReUser, ReAccount, RePassword)
            cursor = connection.cursor()
            cursor.execute(sql, new_data)
            connection.commit()
            return redirect('/')

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("資料庫連線已關閉")



#登入
@app.route("/signin", methods=["POST"])
def Signin():
    Account=request.form["account"]
    Password=request.form["password"]
    
    try:
        connection = mysql.connector.connect(
        host=DBhost,         
        database=DBdatabase, 
        user=DBuser,      # 資料庫帳號
        password=DBpassword)  # 資料庫密碼

        #檢查是否註冊過
        cursor = connection.cursor()
        cursor.execute("SELECT name,password FROM user WHERE username= '%s';" % (Account))
        records = cursor.fetchone()

            
        if (records):
            print("帳號正確。。開始檢查密碼")
            print(records[0],"的密碼為:"+records[1])

            if (Password==records[1]):
                print("密碼驗證成功")
                session['UserAccount'] = Account
                session['UserName']=records[0]
                return redirect('/menber')
            else:
                print("密碼錯誤")
                return redirect('/error/?message=帳號或密碼輸入錯誤')

        else:
            print("帳號錯誤")
            return redirect('/error/?message=帳號或密碼輸入錯誤')
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("資料庫連線已關閉")


#會員
@app.route("/menber")
def Menber():
    UserAccount = session.get('UserAccount')
    UserName=session.get('UserName')
    if UserAccount:
        return render_template("indexmenber.html",user=UserName)
    else:
        return redirect('/')

#錯誤
@app.route("/error/") #http://127.0.0.1:3000/error/?message=自訂的錯誤訊息
def Error():
    html_text=request.args.get("message","自訂的錯誤訊息")
    
    return render_template("indexerror.html",text=html_text)

#修改會員姓名 API
@app.route("/api/user", methods=["POST"])#http://127.0.0.1:3000/api/user
def MenberUpdateNameApi():
    
    data = request.get_json()
    NewAccountName = data['name']
    print("使用者輸入的名子:",NewAccountName)
#     return jsonify({"姓名": username})  
    
    UserAccount = session.get('UserAccount')  #使用者帳號
    UserName=session.get('UserName') #原本姓名
    
    try:
        connection = mysql.connector.connect(
        host=DBhost,         
        database=DBdatabase, 
        user=DBuser,      
        password=DBpassword) 
        
        #變更
        cursor = connection.cursor()
        cursor.execute("update user set name='%s' where username='%s' ;" % (NewAccountName,UserAccount))
        connection.commit()
        
        
        #檢查新設定的名有無在資料庫
        cursor = connection.cursor()
        cursor.execute("select id from user where name='%s' and username='%s';" % (NewAccountName,UserAccount))
        records = cursor.fetchone()
        print("records",records)
            
        if (records):
            session['UserName']=NewAccountName
            print(session)
            return {"ok":True}


        else:
            return {"error":True}

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("資料庫連線已關閉")



#API
@app.route("/api/users") #http://127.0.0.1:3000/api/users?username=帳號
def MemberAccountAPI():
    MemberAccount=request.args.get("username")
    try:
        connection = mysql.connector.connect(
        host=DBhost,         
        database=DBdatabase, 
        user=DBuser,      # 資料庫帳號
        password=DBpassword)  # 資料庫密碼

        #檢查是否註冊過
        cursor = connection.cursor()
        cursor.execute("SELECT id,name,username FROM user WHERE username= '%s';" % (MemberAccount))
        records = cursor.fetchone()
            
        if (records):
            return {"data":{"id":records[0],"name":records[1],"username":records[2]}}
        else:
            return {"data":records}
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("資料庫連線已關閉")

    
    return str(MemberAccount)

#登出
@app.route("/signout", methods=["GET"])
def Signout():
    session.clear() #清除
#     print("登出")
    return redirect('/')

app.run(port=3000)