article = input("Enter your article: ")                      # take article from user    
chunk_size = int(input("Enter character limit per chunk: ")) # take how many chunks in article from user  
overlap = int(input("Enter overlap size: "))                 # take overlap from user  

chunks = []
start = 0
chunk_id = 1

total_length = len(article)

while start < total_length:
    end = start + chunk_size
    text = article[start:end]

    chunks.append({
        "chunk_id": chunk_id,
        "start_index": start,
        "end_index": end,
        "text": text
    })

    start = start + chunk_size - overlap
    chunk_id += 1

for chunk in chunks:
    print("\nChunk ID:", chunk["chunk_id"])
    print("Start Index:", chunk["start_index"])
    print("End Index:", chunk["end_index"])
    print("Text:", chunk["text"])
