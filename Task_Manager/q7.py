def first_letter(s):
    for i in range(len(s)):
        count = 0

        for j in range(len(s)):
            if s[i] == s[j]:
                count += 1
        if count == 1:
            return s[i]
        
        return None

answer = first_letter("swiiss")
print(answer)