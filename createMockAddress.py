import json

# Creates a adress dictionary tied to an address for a WAWA in Orlando
def writeToJson():
    my_dict = {
            "line1":"3100 S Orange Ave",
            "city": "Orlando",
            "state": "FL",
            "postal_code": "32806",
            "country": "US",
            }

    # Opens the address JSON file, wipes it, writes the adress dictionary
    with open('address.json', 'w') as json_file:
        json.dump(my_dict, json_file)