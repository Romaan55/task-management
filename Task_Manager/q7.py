def first_letter(s):
    for i in range(len(s)): #check each letter
        count = 0

        for j in range(len(s)): #Compare the present letter with every letter
            if s[i] == s[j]:
                count += 1
        if count == 1:
            return s[i]
        return None    #no letther found return none

answer = first_letter("swiiss")
print(answer)