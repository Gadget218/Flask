from flask import Flask, request, jsonify
 
 #create flask application
app = Flask(__name__)

#decorator
@app.route("/get-user/<user_id>")#url after /, <> is a path paramter which is a dynamic value that you can pass in the path of a URL.
# def home():
#     return "Home"
def get_user(user_id):
    user_data={
        "user_id":user_id,
        "name":"John Doe",
        "email":"john.doe@example.com"
        }
    #Query parameter:
    extra = request.args.get("extra")
    if extra:
        user_data["extra"]=extra
    
    return jsonify(user_data), 200#json is gonna be used whenever we wanna return data. 200 is the default status code, you can pass other status codes as well.

@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()

    return jsonify(data),201


#run flask application
if __name__=="__main__":
    app.run(debug=True)