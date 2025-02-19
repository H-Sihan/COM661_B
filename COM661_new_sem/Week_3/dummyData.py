from flask import Flask, jsonify, request, make_response
import uuid
import random

app = Flask(__name__)

businesses = {}

def generate_dummy_data():
    towns = ['London', 'Manchester', 'Birmingham', 'Liverpool', 'Glasgow', 'Edinburgh', 'Cardiff', 'Belfast']
    business_dict = {}

    for i in range(100):
        id = str(uuid.uuid4())
        name = "Biz " + str(i)
        town = random.choice(towns)
        rating = random.randint(1, 5)
        business_dict[id] = {
            "name": name,
            "town": town,
            "rating": rating,
            "reviews": []
        }
    return business_dict

@app.route('/businesses', methods=['GET'])
def get_all_business():
    return make_response(jsonify({"Businesses":businesses}), 200)

@app.route('/businesses/<string:biz_id>', methods=['GET'])
def get_business(biz_id):
    if biz_id in businesses:
        return make_response(jsonify(businesses[biz_id]), 200)
    else:
        return make_response(jsonify({"error":"invalid business ID"}), 404)

@app.route('/businesses', methods=['POST'])
def add_business_form():
    data = request.form
    if data and "name" in data and "town" in data and "rating" in data:
        next_id = str(uuid.uuid1())
        new_business = {
            "id": next_id,
            "name": data.get("name"),  
            "town": data.get("town"),
            "rating": int(data.get("rating", 0)),  
            "reviews": {}
        }
        businesses[next_id] = new_business
        return make_response(jsonify({next_id:new_business}), 201)
    else:
        return make_response(jsonify({"error":"Missing data"}), 404)

if __name__ == "__main__":
    businesses = generate_dummy_data()
    app.run(debug=True)