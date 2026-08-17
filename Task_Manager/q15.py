def deepMerge(target, source):
    result = target.copy()
    for key in source:
        if key in result:
            if type(result[key]) == dict:   #Check if target value is a dictionary
                if type(source[key]) == dict: #Check if source value is also a dictionary
                    result[key] = deepMerge(result[key], source[key])#merge data
        else:
            result[key] = source[key]
    return result
target = {
    "name": "Ali",#user data
    "address": {
        "city": "Lahore",
        "country": "Pakistan",
        "Sub-continent": "Asia"
    }
}
source = {
    "age": 20,
    "address": {          
        "city": "Karachi"#data
    }
}
result = deepMerge(target, source)#store result
print(result)