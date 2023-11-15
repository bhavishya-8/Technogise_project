import copy
def calculate_gst(units, item_type, initial_price):
    gst_rates = {
        "Food grains" : ["rice", "dal", "wheat"],
        "Furniture" : ["sofa", "table", "chair"],
        "Electronics" : ["tv", "mobile", "laptop"],
        "Cosmetics" : ["perfume", "face cream", "lotion"]
    }
    category = None
    for cat , products in gst_rates.items():
        if item_type in products:
            category = cat
    if category is None:
        return "No Item in the list"
    gst_percentage = {
        "Food grains" : 0,
        "Furniture" : 5,
        "Electronics" : 18,
        "Cosmetics" : 28
    }
    gst_rate  = gst_percentage[category]
    gst_amount = (gst_rate/100)*initial_price
    final_amount = units*(initial_price + gst_amount)
    return [gst_amount, final_amount]

import copy
input_data = input()
copy_data = copy.deepcopy(input_data)
copy_data = copy_data.split(',')
# print(len(copy_data))
if len(copy_data) == 3:
    units, item_type, initial_price = [part.strip() for part in input_data.split(',')]
#     if units.isdigit()
    units = int(units)
    initial_price = float(initial_price)
    item_type = item_type.lower()
    result = calculate_gst(units, item_type, initial_price)
    if isinstance(result, list):
        gst_amount, final_amount = result
        print(gst_amount)
        print(final_amount)
    else:
        print(result)
else:
    print("Not a proper formate!")
