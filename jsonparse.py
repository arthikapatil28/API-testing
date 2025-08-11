import json
with open("test.json") as f:
    data=json.load(f)
    print(data)
    print(type(data))
    #to fetch the site in json file."site": "http://rahulshettyacademy.com" from course
    #print(data["courses"][2][0])
    lt=data["courses"][1]['details']['site']
    print(lt)
    print(type(lt))
    #to fetch the website from dashboard
    web=data["dashboard"]['website']
    print(web)
    print(type(web))
    # tp fetch the price of the RPA title using for loop
    prc=data["courses"]
    print(type(prc))
    for each in prc:
        #print(each)
        if each['title']=="RPA":
            print(each["price"])
            assert each["price"]==45
# compare two differnet Json files
with open("test2.json") as f1:
    data2=json.load(f1)
    print(data==data2)  # print boolean value

