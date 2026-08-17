def two_sum(arr,target):
    dic = {}  #store number 
    for i in range(len(arr)):  #check each number in the list
        require = target - arr[i]
    
        if require in dic: #if required number is already exist in list
            return [dic[require], i]

        dic[arr[i]] = i  #store current number
    return None

print(two_sum([2,8,7,4,11,15], 15))