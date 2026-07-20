print('hallo! LIVE Kitchen')
from flask import Flask, render_template,request

app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/roll')
def roll():
    return render_template('dish.html')

# Sample Python dictionary
my_starter = {
    "tomato":"FOR COOKING: Use 1-2 Tomato for 1-2 people servings. ***Tomato is a delightful blend of sweet,and slightly acidic flavors***, Cut into your favorite size pieces.", 
    "onion":"FOR COOKING: Use 1-2 Onion for 1-2 people servings. ***Onion is a blend of mild sweet,and sulfurous flavors*** , Cut into your favorite size pieces. " ,
    "ginger":"FOR COOKING: Use 1 small piece for 1-2 people servings. ***Ginger is a woody,spicy,and earthy flavours***, IMPORTANT- Use(grind / crush)Ginger, It enhance taste and flavorful.",
    "garlic":"FOR COOKING: Use 3-5 pieces for 1-2 people servings. ***Garlic  is a pugency,nutty,and savory flavours***, (grind / chopping / crush)Garlic, It enhance taste,aroma, and flavourful. ",
    "curry leaf":"FOR COOKING: Use 1/2(half) cup curry leaf for 1-2 people servings. ***Curry leaf have a strong aroma,and flavourful*** some studys suggest its promote hair growth and prevent hair loss." 
}
my_veg = {
    
    "carrot":"FOR COOKING: Use 1-2 carrot for 1-2 people servings. ***Carrot typically have sweet flavor slightly bitternes***, Cut into small pieces for better taste.  ",
    "potato":"FOR COOKING: Use 3-4 small potatos for 1-2 people servings. ***Potato is little bit sweet,earthy flavours***, Cut into (Round slices) or (small cubes) for better softer texture. ",
    "cauliflower":"FOR COOKING: Use 2 cup of cauliflower for 1-2 people servings. ***Cauliflower is slightly sweet,and nutty flavor*** , Remove core & stems, Before cutting wash well is important, Then Cut into medium pieces for better cook. ",
    "beans":"FOR COOKING :Use 1 hand pick of beans for 1-2 people servings. ***Bean is a earthy,nutty, and starchy flavours***, Trim the both ends, and Cut into (small) or (medium) pieces. ",
    "mushroom":"FOR COOKING: Use 8-10 full mushroom for 1-2 people servings. ***Mushroom is a earthy,nutty, and umami flavours***, Before cutting wash and clean well, Then Cut into half pieces or leave it full size pieces.",
    "drum stick":"FOR COOKING: Use 2-3 Drum stick for 1-2 people servings. ***Drum Stick is almost grassy,slightly bitter,and grascy flavours***, Remove both ends, diagonal(cylinder) cut for better boil and taste. ",
    "green chili":"FOR COOKING: Use 1-2nos for 1-2 people servings. ***Green Chilies add a sharp, pungent(spicy) kick to dishes***, It gives hot&spicy flavour blended in any dishes.",
}
my_powder={
    "red chili":"FOR COOKING: Use 1/2(half)- 1 table spoons for 1-2 people servings. **Red Chili**, It keeps spicy in meidum level. NOTE*(use RED CHILI or CHILI MIX any one to control your spicy level in dish)*",
    "chili mix":"FOR COOKING: Use 1-2 table spoons,for 1-2 people servings. **Chili Mix is known as (Kolambu Milaga Podi)**,The special chili mix used allover india a blend taste of spices mix. NOTE(use CHILI MIX or RED CHILI any one to control your spicy level in dish)",
    "garam":"FOR COOKING: Use 1- 1&1/2 table spoons, for 1-2 people servings. **Garam a blended spices mix**, NOTE: It's complex mixture of (7- Types of ground spices of mixed taste)  ",
    "turmeric":"FOR COOKING: Use 1/4(quarter) for 1-2 people servings. **Turmeric is a antioxidant,bitter flavor and color**, It has more health benifits and colour flavour.",
    "fennel":"FOR COOKING: Use 1/4(quarter)-1/2(half) table spoons for 1-2 people servings. **Fennel powder is licorice-like flavour**, It gives a good smell,aroma flavorful.",
    "cumin":"FOR COOKING: Use 1/4(quarter)-1/2(half) table spoons for 1-2 people servings. **Cumin powder is good digestiver and earthy flavour**, It gives a good smell flavorful",
    "coriander":"FOR COOKING: Use 1/2(half)- 1 table spoons for 1-2 people servings. **Coriander is a unique flavour profile and health benefits**, It controll you diet incorporating. ",

}
my_liquid={
    "coconut":"FOR COOKING: Use 3-4 table spoons for 1-2 people servings. **Coconut oil gives subtle,unique flavor to any dishes**.",
    "peanut":"FOR COOKING: Use 5-7 table spoons for 1-2 people servings. **peanut oil is rich in monounsaturated fatty acid good for heart health**.",
    "sunflower":"FOR COOKING: Use 4-5 table spoons for 1-2 people servings. **Sunflower oil rich in linoleic acid can help lower bad cholesterol**.",
    "palm":"FOR COOKING: Use 2-4 table spoons for 1-2 people servings. **Palm oil contains vitamins E,K, and antioxidants**. ",
    "gingelly":"FOR COOKING: Use 4-6 table spoons for 1-2 people servings. **Gingelly() oil rich in monounsaturated fatty acid helps lower bad colesterol**.",
    "ghee":"FOR COOKING: Use 1/2 (half)- 1 table spoons for 1-2 people servings . **Ghee is good source of vitamins A,D,E, and K**,It gives good aroma and taste for any dishes.",
    "butter":"FOR COOKING: Use 10-20gm cubes for 1-2 people servings. **Butter contains vitamins A,D,and K**, It gives creamy, saucey, good aroma to any dishes.",
    "cheese":"FOR COOKING: Use 10-15gm for 1-2 people servings. **Cheese is good source of protein,calcium,and vitamin B12**, It gives good aroma to any dishes.",
}
my_spices={
    "dry chili":"FOR COOKING: Use 3-5nos for 1-2 people servings. **Dry Red chili for its pungent flavor and helth benifits**, It gives a spicy taste for your buds.",
    "pepper":"FOR COOKING: Use 1/2(half) table spoons for 1-2 people servings. **Pepper for its pungent flavor and aroma**, It gives strong spicy and aroma to dishes.",
    "clove":"FOR COOKING: Use 1-3nos for 1-2 people servings. **Clove a flavorful and caused by free radicals**, It gives strong aromatic flavor to any dishes.",
    "star anise":"FOR COOKING: Use 1-nos for 1-2 people servings. **Star anise contain antimicrobial properties its helps fight infections**, It gives licorice-flavor and good aroma.",
    "cinnamon":"FOR COOKING: Use 1-2 small pieces. **Cinnamon help regulate blood sugar levels,reduce inflammation**, It gives strong aroma and distinctive sweet flavor. ",
    "bay leaf":"FOR COOKING: Use 1 leaf for 1-2 people servings. **Bay leaf adds a sbutle,earthy aroma to dishes**, Do not EAT bay leaf its use for only food aroma.",
    "cardamom":"FOR COOKING: Use 2-3nos for 1-2 people servings. **Cardamom help relieve indigestion,and gas**, It give aromatic flavor citrusy to dishes.",
    "fennel":"FOR COOKING: Use 1/2(half) table spoons for 1-2 people servings. **Fennel seeds can help increase milk in breastfeeding mothers**, It gives licorice flavor and helth benefits.",
    "cumin":"FOR COOKING: Use 1/2(half) table spoons for 1-2 people servings. **cumin(jeera) help to digestive,weight loss,and sugar control**, It gives earthy flavor,good in taste.",
    "mustard":"FOR COOKING: Use 1/4(quarter) table spoons for 1-2 people servings. **Mustard seeds help to pain relief,and antioxidant**, It gives unique spicy touch to your dish.",
}


@app.route('/livecooking', methods=['GET'])
def index():
    # Default messages in case no keys are submitted
    message_01 =""
    message_011 =""
    message_0111 =""
    message_1 = ""
    message_11 = ""
    message_111 = ""
    message_2 = ""
    message_22 = ""
    message_222 = ""
    message_3 = ""
    message_33 = ""
    message_333 = ""
    message_4 = ""
    message_44 = ""
    message_444 = ""
    
    # Get the dictionary keys from the query parameters for both forms
    key_0 = request.args.get('key0')
    key_00 = request.args.get('key00')
    key_000 = request.args.get('key000')
    # key_0000 = request.args.get('key0000')
    key_1 = request.args.get('key1')
    key_11 = request.args.get('key11')
    key_111 = request.args.get('key111')
    key_2 = request.args.get('key2')
    key_22 = request.args.get('key22')
    key_222 = request.args.get('key222')
    key_3 = request.args.get('key3')
    key_33 = request.args.get('key33')
    key_333 = request.args.get('key333')
    key_4 = request.args.get('key4')
    key_44 = request.args.get('key44')
    key_444 = request.args.get('key444')
    
    # Lookup for the first key
    if key_0:
        if key_0 in my_starter:
            result_0 = my_starter[key_0]
            message_01 = f"'{key_0}' : {result_0}"
        else:
            message_01 = f"Key '{key_0}' not found in the Starter List."

    if key_00:
        if key_00 in my_starter:
            result_00 = my_starter[key_00]
            message_011 = f"'{key_00}' : {result_00}"
        else:
            message_011 = f"Key '{key_00}' not found in the Starter List."

    if key_000:
        if key_000 in my_starter:
            result_000 = my_starter[key_000]
            message_0111 = f"'{key_000}' : {result_000}"
        else:
            message_0111 = f"Key '{key_000}' not found in the Starter List."        

    if key_1:
        if key_1 in my_veg:
            result_1 = my_veg[key_1]
            message_1 = f"'{key_1}' : {result_1}"
        else:
            message_1 = f"Key '{key_1}' not found in the Vegitables List."
    
    if key_11:
        if key_11 in my_veg:
            result_11 = my_veg[key_11]
            message_11 = f"'{key_11}' : {result_11}"
        else:
            message_11 = f"Key '{key_11}' not found in the Vegitables List ."

    if key_111:
        if key_111 in my_veg:
            result_111 = my_veg[key_111]
            message_111 = f" '{key_111}' : {result_111}"
        else:
            message_111 = f"Key '{key_111}' not found in the Vegitables List."        
    
    
    # Lookup for the second key
    if key_2:
        if key_2 in my_powder:
            result_2 = my_powder[key_2]
            message_2 = f" '{key_2}' : {result_2}"
        else:
            message_2 = f"Key '{key_2}' not found in the Masalas list."

    if key_22:
        if key_22 in my_powder:
            result_22 = my_powder[key_22]
            message_22 = f"'{key_22}' : {result_22}"
        else:
            message_22 = f"Key '{key_22}' not found in the Masalas list."

    if key_222:
        if key_222 in my_powder:
            result_222 = my_powder[key_222]
            message_222 = f"'{key_222}' : {result_222}"
        else:
            message_222 = f"Key '{key_222}' not found in the Masalas list."



 # Lookup for the third key
    
    if key_3:
        if key_3 in my_liquid:
            result_3 = my_liquid[key_3]
            message_3 = f"'{key_3}' : {result_3}"
        else:
            message_3 = f"Key '{key_3}' not found in the Cooking Oils List."        
    
    if key_33:
        if key_33 in my_liquid:
            result_33 = my_liquid[key_33]
            message_33 = f"'{key_33}' : {result_33}"
        else:
            message_33 = f"Key '{key_33}' not found in the Cooking Oils List."

    if key_333:
        if key_333 in my_liquid:
            result_333 = my_liquid[key_333]
            message_333 = f"'{key_333}' : {result_333}"
        else:
            message_333 = f"Key '{key_333}' not found in the Cooking Oils List."


 # Lookup for the Fourth key
    if key_4:
        if key_4 in my_spices:
            result_4 = my_spices[key_4]
            message_4 = f"'{key_4}' : {result_4}"
        else:
            message_4 = f"Key '{key_4}' not found in the Raw Spices List."
    
    if key_44:
        if key_44 in my_spices:
            result_44 = my_spices[key_44]
            message_44 = f"'{key_44}' : {result_44}"
        else:
            message_44 = f"Key '{key_44}' not found in the Raw Spices List."

    if key_444:
        if key_444 in my_spices:
            result_444 = my_spices[key_444]
            message_444 = f"'{key_444}' : {result_444}"
        else:
            message_444 = f"Key '{key_444}' not found in the Raw Spices List."


 # Render HTML with the results
    return render_template('live.html',key_0=key_0,key_00=key_00,key_000=key_000,key_1=key_1,key_11=key_11,key_111=key_111,
                           key_2=key_2,key_22=key_22,key_222=key_222,key_3=key_3,key_33=key_33,key_333=key_333,key_4=key_4,key_44=key_44,key_444=key_444,
                           message_01=message_01,message_011=message_011,message_0111=message_0111, message_1=message_1,message_11=message_11,message_111=message_111,
                           message_2=message_2,message_22=message_22,message_222=message_222,
                           message_3=message_3,message_33=message_33,message_333=message_333,
                           message_4=message_4,message_44=message_44,message_444=message_444)



if __name__=='__main__':
    app.run(debug=True)