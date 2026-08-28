import math                                                      #math module
query = [1, 2, 3]                                                # query vector
documents = [                                                    # document vector
    [7, 8, 9],        
    [2, 4, 6],        
    [1, 3, 5]        
]        
        
query_magnitude = 0                                              # Query magnitude
        
for i in range(len(query)):                                      # Check every document
    query_magnitude = query_magnitude + query[i] ** 2            # add square of each component
query_magnitude = math.sqrt(query_magnitude)                     # calculate square root
        
        
best_score = -1                                                  # store highest cosine similarity
best_index = -1                                                  # store index of best matching document
        
for i in range(len(documents)):                                  # check every document
  document = documents[i]                                        # select current document
        
dot_product = 0                                                  # calculate dot product
for i in range(len(query)):                                      # loop through vector components
    dot_product = dot_product + (query[i] * document[i])         # multiply and add components
        
document_magnitude = 0                                           # Calculate document magnitude
        
for i in range(len(document)):                                   # loop through document components
    document_magnitude = document_magnitude + document[i] ** 2   # add square of each component
document_magnitude = math.sqrt(document_magnitude)               # calculate square root

cosine = dot_product / (query_magnitude * document_magnitude)    # Calculate cosine similarity

if cosine > best_score:                                     
    best_index = i         # update best document index
    best_score = cosine    # update highest score


print("Cosine", cosine)                           # print the values
print("Best Index",best_index)                    # print the values
print("Query Magnitude:", query_magnitude)        # print the values
print("Dot Product:", dot_product)                # print the values
print("Document Magnitude:", document_magnitude)  # print the values
