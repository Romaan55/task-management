def check_bracket(text):
    list = []
    for bracket in text:

        if bracket == '(' or bracket == '[' or bracket == '{':
            list.append(bracket)
        else:
            if len(list) == 0:
                return False
            last = list.pop()
            if bracket == ')' and last != '(':
                return False
            if bracket == ']' and last != '[':
                return False
            if bracket == '}' and last != '{':
                return False

    if len(list) == 0:
        return True
    else:
        return False
    
print(check_bracket("{[()]}"))
print(check_bracket("{[(])]}"))