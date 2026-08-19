import string
vocabulary = {}                            #store vocabulory
reversed_vocabulary = {}                   #store reverse vocabulory

sentence = input("Enter the sentense : ")  # take input from user
sentence = sentence.lower()                # lower the word
for p in string.punctuation:               # check each punctuation mark
    sentence = sentence.replace(p, "")     # remove punctuation from sentence
    words = sentence.split()               # remove spaces from word

id = 1     

for word in words:                         # check the word in sentense
    if word not in vocabulary:             # if word is in vocabulary
        vocabulary[word] = id              # give unique word
        id += 1                            # add word in id
for word, id in vocabulary.items():        # get each word and its ID 
    reversed_vocabulary[id] = word         # ID back to the word
    
def encode(sentence):                      # function
    encoded = []                           # for store id
    words = sentence.split()               # split the sentence
        
    for word in words:                     # find word id
        id = vocabulary[word]              # take id from word
        encoded.append(id)                 # add id into encoded list  
    return encoded                         # return encode
    
encoded_text = encode(sentence)            # call encode function
    
    
    
def decoded(encoded):                       # decode function
    decoded = []                            # store decode sentence
    for id in encoded:                      # pick each id from encoded through loop
        word = reversed_vocabulary[id]      # covert Id into words
        decoded.append(word)                # add word into decorded list
    return " ".join(decoded)                # join the sentence
decoded_text = decoded(encoded_text)        # call encode function
    
    
print("Vocabulary:", vocabulary)            # make sentence encode
print("Encoded:", encoded_text)             # print encoded
print("Decoded:", decoded_text)             # print decoded

        
    





    