def group_by(data, key):
    result = {} #for result store
    for item in data:
        value = item[key]
        if value not in result:
            result[value] = []

        result[value].append(item)
        return result

users = [
    {"name": "Ali", "city": "Lahore"},
    {"name": "Sara", "city": "Lahore"},     #user data
    {"name": "Ahmed", "city": "Karachi"}   
]
print(group_by(users, "city"))