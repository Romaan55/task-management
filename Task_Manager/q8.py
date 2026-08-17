def num(arr):
    answer = []  #store the values

    for item in arr:  #check every item in list
        if isinstance(item, list):  #check item if it will be in another list
            answer.extend(num(item))
        else:
            answer.append(item) #add the simple values in the answer
    return answer

arr = [1, [2, 3], [4, [5, 6]]]
print(num(arr))