def compress_string(s):
    result = ""
    count = 1 #start from 1 to count

    for i in range(len(s)):    #check each character
        if i + 1 < len(s) and s[i] == s[i + 1]:    #check if next character is same
            count += 1
        else:
            result += s[i] + str(count)#add character and its count
            count = 1

    if len(result) < len(s):   #if it short return compress string
        return result
    else:
        return s
    
print(compress_string("aaabbccccd"))
print(compress_string("abc"))