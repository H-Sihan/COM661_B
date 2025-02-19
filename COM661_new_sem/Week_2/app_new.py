from flask import Flask, jsonify, request, make_response
import uuid

app = Flask(__name__)

businesses = [
    {
        "id": 1,
        "name": "Coffee House",
        "town": "London",
        "rating": 4,
        "reviews": []
    },
    {
        "id": 2,
        "name": "Tech Solutions",
        "town": "Manchester",
        "rating": 5,
        "reviews": []
    }
]

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Business Directory API (COM661)"})

@app.route('/businesses', methods=['GET'])
def get_businesses():
    return jsonify({"businesses": businesses})

@app.route('/businesses/raw', methods=['POST'])
def add_business():
    data = request.get_json()
    new_business = {
        "id": str(uuid.uuid4()),
        "name": data["name"],
        "town": data["town"],
        "rating": data.get("rating", 0),
        "reviews": []
    }
    businesses.append(new_business)
    return make_response(jsonify(new_business), 201)

@app.route('/businesses', methods=['POST'])
def add_business_form():
    data = request.form
    next_id = businesses[-1]["id"] + 1
    new_business = {
        "id": next_id,
        "name": data.get("name"),  # Use .get() to prevent KeyError
        "town": data.get("town"),
        "rating": int(data.get("rating", 0)),  # Convert rating to integer
        "reviews": []
    }
    businesses.append(new_business)
    return make_response(jsonify(new_business), 201)

@app.route('/businesses/<int:biz_id>', methods=['GET'])
def get_business(biz_id):
    for biz in businesses:
        if biz["id"] == biz_id:
            return make_response(jsonify(biz), 200)
    else:
        return make_response(jsonify({"error": "Business not found"}), 404)
    
    
@app.route('/businesses/<int:biz_id>', methods=['PUT'])
def edit_business(biz_id):
    data = request.form
    for business in businesses:
        if business["id"] == biz_id:
            business["name"] = data.get("name")
            business["town"] = data.get("town")
            business["rating"] = data.get("rating")
            break
    return make_response(jsonify(business), 200)
        
@app.route('/businesses/<int:biz_id>', methods=['DELETE'])
def delete_business(biz_id):
    for business in businesses:
        if business["id"] == biz_id:
            businesses.remove(business)
            break
    return make_response(jsonify(business), 200)

@app.route('/businesses/<int:biz_id>/reviews', methods=['GET'])
def get_all_reviews(biz_id):
    for business in businesses:
        if business["id"] == biz_id:
            break
    return make_response(jsonify(business["reviews"]), 200)

@app.route('/businesses/<int:biz_id>/reviews', methods=['POST'])
def add_new_review(biz_id):
    data = request.form
    for business in businesses:
        if business["id"] == biz_id:
            if len(business["reviews"]) == 0:
                new_review_id = 1
            else:
                new_review_id = business["reviews"][-1]["id"] + 1
            new_review = {
                "id" : new_review_id,
                "username" : data.get("username"),
                "comment" : data.get("comment"),
                "stars" : data.get("stars")
            }
            business["reviews"].append(new_review)
            break
    return make_response(jsonify(new_review), 200)

@app.route('/businesses/<int:biz_id>/reviews/<int:r_id>', methods=['GET'])
def get_business_reviews(biz_id, r_id):
    for business in businesses:
        if business["id"] == biz_id:  
            for review in business["reviews"]:  
                if review["id"] == r_id:  
                    return make_response(jsonify(review), 200)
                
    return make_response(jsonify({"error": "Review not found"}), 404)  # Handle missing review      

@app.route('/businesses/<int:biz_id>/reviews/<int:r_id>', methods=['PUT'])
def edit_review(biz_id, r_id):
    data = request.form
    for business in businesses:
        if business["id"] == biz_id:
            for review in business["reviews"]:
                if review["id"] == r_id:
                    review["username"] = data.get("username")
                    review["comment"] = data.get("comment")
                    review["stars"] = data.get("stars")
                    break
            break
    return make_response(jsonify(review), 200)

@app.route('/businesses/<int:biz_id>/reviews/<int:r_id>', methods=['DELETE'])
def delete_review(biz_id, r_id):
    for business in businesses:
        if business["id"] == biz_id:
            for review in business["reviews"]:
                if review["id"] == r_id:
                    business["reviews"].remove(review)
                    break
            break
    return make_response(jsonify({}), 200)

if __name__ == '__main__':
    app.run(debug=True)