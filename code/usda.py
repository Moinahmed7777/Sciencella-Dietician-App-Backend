import requests
import json
from fuzzywuzzy import fuzz #string matching

#food_list = ['milk','chicken wings','gummy bears','taco']
#
api_key = 'BNAsthPJ1BiAR5gdioRemmVTLLGodKuR4hxd9R63'
USDA_URL = 'https://api.nal.usda.gov/fdc/v1/'
headers={'Content-type':'application/json', 'Accept':'application/json',"x-api-key":api_key}

# Search each entry in top_products_by_aisle by USDA database through API
def fdcID_retrieval(food_to_search: 'food_list', api_key=api_key) -> list:
    '''
    This function uses USDA's REST access API to retrieve
    information from FoodData Central (https://fdc.nal.usda.gov/).
    This function returns the FDCID for the item searched by attempting to
    retrieve the closest match by using Levenshtein distance calculations.
    An API key is required for use and can be acquired for free, here:
    https://fdc.nal.usda.gov/api-key-signup.html
    '''
    # set API details
    requested_url = USDA_URL + 'search?api_key='
    fdcIDs = []  # container for results
    for item in food_to_search:
        data = {"generalSearchInput": item, "requireAllWords": True}
        data_str = json.dumps(data).encode("utf-8")
        response = requests.post(requested_url + api_key, headers=headers, data=data_str)
        parsed = json.loads(response.content)
        # set up metrics for eventual item selection
        best_idx = None
        best_ratio = 0
        # for each item in the generated data
        for idx, i in enumerate(parsed['foods']):
            title = ""
            if i['dataType'] == "Branded":
                title = i['brandOwner'] + ' ' + i['description']
            else:
                title = i['description']
            # use a flexibile levenshtein distance to compare
            curr_ratio = fuzz.token_set_ratio(item, title)
            if curr_ratio > best_ratio:
                best_idx = idx
                best_ratio = curr_ratio
            if best_ratio > 90: #90% the same as the user's query
                break

        # save the best performing item as the most likely match from the db
        fdcIDs.append(parsed['foods'][best_idx]['fdcId'])
    return fdcIDs



def nutrition_retrieval(fdcIDs : list, api_key=api_key, remove_empty_json = False) -> 'json':
    ''' This function collects nutritional data for each FDCID.
    It does so by making calls to the USDA database,
    FoodData Central (https://fdc.nal.usda.gov/), and it
    then retrieves the returned JSON data for the relevant nutritional data.
    Parameters
    ----------
    '''
    nutritional_info = list()
    nutrients_id = {1008,1293,1292,1258,1004,1253,1093,1005,1079,2000,1003,1104,1162,1087,1089,1110}
    index = 0
    #Loop over each item id
    for i in fdcIDs:
        fdcId = str(i)
        requested_url = (USDA_URL + fdcId + '?api_key=' + api_key)
        response = requests.get(requested_url, headers=headers)
        parsed = json.loads(response.content)
        #List of variables needed
        energy = 0
        monounsaturated_fatty_acid = 0
        polyunsaturated_fatty_acid = 0
        saturated_fatty_acid = 0
        cholesterol = 0
        sodium = 0
        carbs = 0
        fiber = 0
        sugars = 0
        protein = 0
        vit_a = 0
        vit_c = 0
        vit_d = 0
        calcium = 0
        iron = 0
        total_lipid = 0

        # Loop over dictionary length to look for desired data
        for j in range(0, len(parsed['foodNutrients'])):
            id = parsed['foodNutrients'][j]['nutrient']['id']
            if id not in nutrients_id:
                continue
            amount = parsed['foodNutrients'][j]['amount']


            if id == 1008:
                energy = amount
            elif id == 1293:
                polyunsaturated_fatty_acid = amount
            elif id == 1292:
                monounsaturated_fatty_acid = amount
            elif id == 1258:
                saturated_fatty_acid = amount
            elif id == 1004:
                total_lipid = amount
            elif id == 1253:
                cholesterol = amount
            elif id == 1093:
                sodium = amount
            elif id == 1005:
                carbs = amount
            elif id == 1079:
                fiber = amount
            elif id == 2000:
                sugars = amount
            elif id == 1003:
                protein = amount
            elif id == 1104:
                vit_a = amount
            elif id == 1162:
                vit_c = amount
            elif id == 1087:
                calcium = amount
            elif id == 1089:
                iron = amount
            elif id == 1110:
                vit_d = amount

        # Convert to JSON
        nutrient_container = {
            "food_name":food_list[index],
            "energy":float(energy),
            "protein": float(protein),
            "total_lipid": float(total_lipid),
            "carbohydrate": float(carbs),
            "fiber": float(fiber),
            "sugar": float(sugars),
            "calcium":float(calcium),
            "iron":float(iron),
            "sodium": float(sodium),
            "vitamin_a":float(vit_a),
            "vitamin_c":float(vit_c),
            "vitamin_d":float(vit_d),
            "saturated_fatty_acid": float(saturated_fatty_acid),
            "monounsaturated_fatty_acid": float(monounsaturated_fatty_acid),
            "polyunsaturated_fatty_acid": float(polyunsaturated_fatty_acid),
            "cholesterol":float(cholesterol)
        }
        m=nutrient_container
        if remove_empty_json:
            nutrient_container = {k: v for k, v in nutrient_container.items() if v != 0}
        nutritional_info.append(nutrient_container)
        index += 1
    return m #json.dumps(nutritional_info, indent = 4)

#food_list=["apple pie"]
#fdcIDs = fdcID_retrieval(food_list)
#nutrient_json = nutrition_retrieval(fdcIDs=fdcIDs, api_key=api_key,remove_empty_json=False)
#print(nutrient_json)

###
from flask_restful import Resource, reqparse
#from models.user import UserModel
#import uuid

###
#class food_nutrient_ret():
"""
    parser = reqparse.RequestParser()
    parser.add_argument('food',
    type=str
    )
"""
food_list=[]
def foodret(food):
    #data = food_nutrient_ret.parser.parse_args()
    
    food_list.append(food)
    #print(food_list)
    fdcIDs = fdcID_retrieval(food_list)
    print(fdcIDs)
    nutrient_json = nutrition_retrieval(fdcIDs=fdcIDs, api_key=api_key,remove_empty_json=False)
    print(nutrient_json)
    return nutrient_json
