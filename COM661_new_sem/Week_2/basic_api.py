import json

business_directory = {
    "message": "Welcome to the Business Directory API",
    "businesses": [
        {"id": 1, "name": "Coffee House", "town": "London", "rating": 4},
        {"id": 2, "name": "Tech Solutions", "town": "Manchester", "rating": 5}
    ]
}

json_response = json.dumps(business_directory, indent=4)
print(json_response)

@app.route("/businesses/<string:id>", methods=["GET"])
def show_one_business(id):
    return make_response( jsonify( businesses[id] ), 200) 