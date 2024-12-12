from flask import Flask, request
app = Flask(__name__)
@app.route("/")
def home():
    return "hello world"

@app.route("/calculate")
def calculator(methods=['GET']):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    c = request.args.get('c')
    answer = 0
    # add , subtact, divide, multiply
    if c == "%2B":
        answer = a+b
    elif c == "subtract":
        answer = a-b
    elif c == "multiply":
        answer = a*b
    elif c == "divide":
        answer = a/b
    else:  
        return "invalid operation"

    return f"answer is {answer}"
if __name__ == "__main__":
    app.run(port= 5000, debug=True)


'''
    GET-> to get info/data from user
    POST-> TO SUBMIT/STORE DATA IN DB
    PUT -> TO COMPLETELY UPDATE THE DATA
    PATCH -> TO PARTIALLY UPDATE THE DATA
    DELETE -> IT IS USE TO DELETE THE DATA
'''