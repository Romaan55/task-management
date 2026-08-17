def second_largest(arr):
    largest = None
    second = None
    for num in arr:
        if largest is None or num > largest:
            second = largest
            largest = num
        elif num != largest and (second is None or num > second):
            second = num

    return second #second value return ki ha

print(second_largest([10, 5, 8, 10, 3]))  #second large is 8
print(second_largest([10, 10, 5, 5]))     #second large is5
print(second_largest([10, 10, 10]))       #None is second largest
