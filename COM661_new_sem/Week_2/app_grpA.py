#pip install flask
from flask import Flask, request, jsonify, make_response
import uuid

app = Flask(__name__)

businesses = [
    {
        "id":"1",
        "name": "Sam's",
        "town": "London",
        "rating": 4,
        "review": [{
            "id":1,
            "username": "Pizza Hub",
            "comment": "Camden",
            "star": 3,
        }]
    },
    {
        "id":"a",
        "name": "Pizza Hub",
        "town": "Camden",
        "rating": 3,
        "review": []
    },
    {
        "id":3,
        "name": "Dominos",
        "town": "London",
        "rating": 4,
        "review": []
    }
]

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message":"Welcom to Flask API"})

@app.route('/business', methods=['GET'])
def get_business():
    return make_response(jsonify({"businesses":businesses}))

@app.route('/business/<string:id>', methods=['GET'])
def get_one_business(id):
    for biz in businesses:
        if biz["id"] == id:
            return make_response(jsonify(biz), 200)
        else:
            return make_response(jsonify({"Error" : "Invalid ID"}), 404)

@app.route('/business', methods=['POST'])
def add_business():
    data = request.form
    if data and "name" in data and "town" and "rating" in data:
        id = str(uuid.uuid1())
        new_business = {
            "id":id,
            "name": data.get("name"),
            "town": data.get("town"),
            "rating": data.get("rating", 0),
            "review": {}
        }
        businesses.append(new_business)
        return make_response(jsonify(new_business), 200)
    else:
        return make_response(jsonify({"Error":"Missing data"}), 404)

@app.route('/businesses/<int:id>', methods=['PUT'])
def update_business(id):
    data = request.form
    for business in businesses:
        if business['id'] == id:
            business["name"] = data.get("name"),
            business["town"] = data.get("town"),
            business["rating"] = data.get("rating")
            break
    return make_response(jsonify(business), 200)

@app.route('/businesses/<int:id>', methods=['DELETE'])
def delete_business(id):
    for business in businesses:
        if business["id"] == id:
            businesses.remove(business)
            break
    return make_response(jsonify({"Message":"Business deleted"}), 200)

@app.route('/businesses/<int:id>/reviews', methods=['GET'])
def get_all_reviews(id):
    for business in businesses:
        if business["id"] == id:
            break
    return make_response(jsonify(business["review"]))


@app.route('/businesses/<int:id>/reviews', methods=['POST'])
def add_new_review(id):
    data = request.form
    for business in businesses:
        if business["id"] == id:
            if len(business["review"]) == 0:
                new_review_id = 1
            else:
                new_review_id = business["review"][-1]["id"] + 1
            new_review = {
                "id":new_review_id,
                "username": data.get("username"),
                "comment": data.get("comment"),
                "star": data.get("star")
                }
            business["review"].append(new_review)
    return make_response(jsonify(new_review), 200)

@app.route('/businesses/<int:id>/reviews/<int:r_id>', methods=['GET'])
def get_one_reviews(id,r_id):
    for business in businesses:
        if business["id"] == id:
            for review in businesses:
                if review["id"] == r_id:
                    return make_response(jsonify(review), 200)
    return make_response(jsonify({"error":"Review not found"}), 404)

@app.route('/businesses/<int:id>/reviews/<int:r_id>', methods=['PUT'])
def update_reviews(id,r_id):
    data = request.form
    for business in businesses:
        if business["id"] == id:
            for review in businesses["review"]:
                if review["id"] == r_id:
                    review["username"] = data.get("username"),
                    review["comment"] = data.get("comment"),
                    review["star"] = data.get("star")
                    break
            break
    return make_response(jsonify(review), 200)


if __name__ == '__main__':
    app.run(debug=True)