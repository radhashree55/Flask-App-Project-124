from flask import Flask, jsonify, request

app = Flask(__name__)
contacts = [{"id": 1, "Name": "Kim Namjoon", "Contact": "02-312-3456", "done": False}]


@app.route("/addData", methods=["POST"])
def addTask():
    if not request.json:
        return jsonify({"status": "error", "message": "Please provide the data!"}, 400)
    contact = {
        "id": contacts[-1]["id"] + 1,
        "Name": request.json["Name"],
        "Contact": request.json.get("Contact", ""),
        "done": False,
    }
    contacts.append(contact)
    return jsonify({"status": "Success", "message": "Contact added Successfully"})


@app.route("/getData")
def getContacts():
    return jsonify({"data": contacts})


if __name__ == "__main__":
    app.run(debug=True)
