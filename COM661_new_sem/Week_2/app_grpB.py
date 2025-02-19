# pip install flask

from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

businesses = [{
    "id": 1,
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
    id = businesses[-1]["id"] + 1
    new_business = {
        "id": id,
        "name": data.get("name"),
        "town": data.get("town"),
        "rating": data.get("rating", 0),
        "review": []
    }
    businesses.append(new_business)
    return make_response(jsonify(new_business), 200)

@app.route('/businesses/<int:biz_id>', methods=['GET'])
def get_one_id_business(biz_id):
    for biz in businesses:
        if biz["id"] == biz_id:
            return make_response(jsonify(biz), 200)
    else:
        return make_response(jsonify({"Error":"Not found"}), 404)
    
    
@app.route('/businesses/<int:biz_id>', methods=['PUT'])
def edit_business(biz_id):
    data = request.form
    for biz in businesses:
        if biz["id"] == biz_id:
            biz["name"] = data.get("name")
            biz["town"] = data.get("town")
            biz["rating"] = data.get("rating")
            break
    return make_response(jsonify(biz), 200)

@app.route('/businesses/<int:biz_id>', methods=['DELETE'])
def delete_business(biz_id):
    for biz in businesses:
        if biz["id"] == biz_id:
            businesses.remove(biz)
            break
    return make_response(jsonify(biz), 200)

@app.route('/businesses/<int:biz_id>/reviews', methods=['GET'])
def get_all_reviews(biz_id):
    for biz in businesses:
        if biz["id"] == biz_id:
            break
    return make_response(jsonify(biz["review"]), 200)
    
@app.route('/businesses/<int:biz_id>/reviews', methods=['POST'])
def add_new_review(biz_id):
    data = request.form
    for biz in businesses:
        if biz["id"] == biz_id:
            if len(biz["review"]) == 0:
                new_review_id = 1
            else:
                new_review_id = biz["review"][-1]["id"] + 1
            new_review = {
                "id": new_review_id,
                "username": data.get("username"),
                "comment": data.get("comment"),
                "star": data.get("star")
            }
            biz["review"].append(new_review)
            break
    return make_response(jsonify(new_review), 200)

if __name__ == '__main__':
    app.run(debug=True)
    
#python app.py