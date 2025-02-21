# pip install flask

from flask import Flask, jsonify, request, make_response
import uuid

app = Flask(__name__)

businesses = [{
    "id": "ac77db10-eeb5-11ef-9915-763f9cc447a6",
    "name": "Bikram Collections",
    "town": "Woolwich",
    "rating": "5",
    "review": []
},
{
    "id": 2,
    "name": "Umang Collections",
    "town": "Woolwich",
    "rating": "5",
    "review": []
},
{
    "id": 3,
    "name": "Suhabul Collections",
    "town": "Benthal Green",
    "rating": "5",
    "review": []
}]



@app.route('/', methods=['GET'])
def home():
    return jsonify({"messgae":"Welcome to COM661"})

@app.route('/businesses', methods=['GET'])
def get_all_business():
    return make_response(jsonify({"Businesses":businesses}), 200)

@app.route('/businesses', methods=['POST'])
def add_business():
    data = request.form
    id = str(uuid.uuid1())
    if data and "name" in data and "town" and "rating" in data:
        new_business = {
            "id": id,
            "name": data.get("name"),
            "town": data.get("town"),
            "rating": data.get("rating", 0),
            "review": []
        }
        businesses.append(new_business)
        return make_response(jsonify(new_business), 200)
    else:
        return make_response(jsonify({"Error":"Missing data"}), 404)

@app.route('/businesses/<string:biz_id>', methods=['GET'])
def get_one_id_business(biz_id):
    for biz in businesses:
        if biz["id"] == biz_id:
            return make_response(jsonify(biz), 200)
    else:
        return make_response(jsonify({"Error":"Not found"}), 404)
    
    
@app.route('/businesses/<string:biz_id>', methods=['PUT'])
def edit_business(biz_id):
    data = request.form
    for biz in businesses:
        if biz["id"] == biz_id:
            biz["name"] = data.get("name")
            biz["town"] = data.get("town")
            biz["rating"] = data.get("rating")
            break
    return make_response(jsonify(biz), 200)

@app.route('/businesses/<string:biz_id>', methods=['DELETE'])
def delete_business(biz_id):
    for biz in businesses:
        if biz["id"] == biz_id:
            businesses.remove(biz)
            break
    return make_response(jsonify(biz), 200)

@app.route('/businesses/<string:biz_id>/reviews', methods=['GET'])
def get_all_reviews(biz_id):
    for biz in businesses:
        if biz["id"] == biz_id:
            break
    return make_response(jsonify(biz["review"]), 200)
    
@app.route('/businesses/<string:biz_id>/reviews', methods=['POST'])
def add_new_review(biz_id):
    data = request.form
    
    # Required fields
    if not data.get("username") or not data.get("comment"):
        return make_response(jsonify({"Error":"Missing required text"}), 404)
    
    # Validate stars
    try:
        stars = int(data["star"])
        if stars < 1 or stars > 5:
            return make_response(jsonify({"Error":"Stars should be 1-5"}), 400)
    except(ValueError, TypeError):
        return make_response(jsonify({"Error":"Should be a number"}), 400)
    
    # Validate business
    business = None
    for biz in businesses:
        if biz["id"] == biz_id:
            business = biz
            break
    if not business:
        return make_response(jsonify({"Error":"Business ID not found"}), 404)                
    
    new_review_id = str(uuid.uuid1())
    new_review = {
        "id": new_review_id,
        "username": data.get("username"),
        "comment": data.get("comment"),
        "star": data.get("star")
        }
    business["review"].append(new_review)
    return make_response(jsonify(new_review), 200)

if __name__ == '__main__':
    app.run(debug=True)
    
#python app.py