def num(arr):
    answer = []

    for item in arr:
        if isinstance(item, list):
            answer.extend(num(item))
        else:
            answer.append(item)
    return answer

arr = [1, [2, 3], [4, [5, 6]]]
print(num(arr))