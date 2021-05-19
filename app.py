from flask import Flask, jsonify, request
import time

app = Flask(__name__)
@app.route("/bot",methods= ['POST'])

def response():
    query = dict(request.form)['query']
    # if query.lower() == "hi":
    #     result = "Hello, how are you today?"
    # elif query.lower() == "how are you":
    #     result = "I'm good! How are you?"
    # elif query.lower() == "what is your age?":
    #     result = "I am just a session old xD"
    # elif query.lower() == "bye":
    #     result = "It was nice talking to you. Goodbye :)"
    result = query + " " + time.ctime()
    return jsonify({"response":result})


if __name__ == "__main__":
    app.run(debug=True)



