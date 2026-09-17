documents = [
    {"doc_id": "doc_1", "text": "ai is used in worldwide"},
    {"doc_id": "doc_2", "text": "python is also used in AI"},
    {"doc_id": "doc_3", "text": "linux is used in System Administration"},
    {"doc_id": "doc_4", "text": "python is Programming Language"}
]

inverted_index = {}
# Inverted Index
for document in documents:
    doc_id = document["doc_id"]
    text = document["text"]
    words = text.lower().split()
for word in words:
    if word not in inverted_index:
        inverted_index[word] = []
    if doc_id not in inverted_index[word]:
        inverted_index[word].append(doc_id)

# Query Matching
query = input("Enter the query: ") 
query_words = query.lower().split()

results = []

for word in query_words:
    if word in inverted_index:
        print("Word:", word)
        print("Documents:", inverted_index[word])

        for doc_id in inverted_index[word]:
            if doc_id not in results:
                results.append(doc_id)
    else:
        print("Word:", word)
        print("Word is not available in documents")

print("Matching Documents:", results)
# TF Calculation
for doc_id in results:
    for document in documents:
        if document["doc_id"] == doc_id:
            text = document["text"].lower()
            words = text.split()
            total_words = len(words)
    for word in query_words:
        frequency = words.count(word)
        tf = frequency / total_words
           
        print("Word:", word)
        print("Document:", doc_id)
        print("TF:", tf)
        print("Frequency",frequency)
        