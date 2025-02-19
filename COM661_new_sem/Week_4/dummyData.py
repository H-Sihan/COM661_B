import random
import json

def generate_dummy_data():
    towns = ['London', 'Birmingham', 'Belfast',
             'Liverpool', 'Manchester', 'Bristol', 'Ilford',
             'York', 'Portsmouth', 'Richmond']
    
    business_list = []
    
    for i in range(100):
        name = "Biz " + str(i)
        town = random.choice(towns)  # More efficient way to pick a random town
        rating = random.randint(1, 5)
        business_list.append({
            "name": name,
            "town": town,
            "rating": rating,
            "reviews": []
        })
    
    return business_list

# Generate data
businesses = generate_dummy_data()

# Write data to a JSON file
with open("data.json", "w") as fout:
    json.dump(businesses, fout, indent=4)  # Adding indent for better readability
