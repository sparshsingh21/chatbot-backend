from flask import Flask, json, jsonify, request
import time

app = Flask(__name__)
@app.route("/bot",methods= ['POST'])

def response():
    query = request.get_json()
    # query = jsonquery["query"] + str(time.ctime())
    if query["query"].lower() == "hi":
        result = "Hello, how are you today?"
    elif query["query"].lower() == "how are you":
        result = "I'm good! How are you?"
    elif query["query"].lower() == "what is your age?":
        result = "I am just a session old xD"
    elif query["query"].lower() == "bye":
        result = "It was nice talking to you. Goodbye :)"
    # result = query + " " + time.ctime()
    return jsonify({"response": result})


if __name__ == "__main__":
    app.run(debug=True)



