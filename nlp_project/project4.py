from langchain_text_splitters import RecursiveCharacterTextSplitter

article = input("Enter your article: ")
chunk_size = int(input("Enter character limit per chunk: "))
overlap = int(input("Enter overlap size: "))

splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=overlap
)

chunks = splitter.split_text(article)

chunk_id = 1
start_index = 0

for chunk in chunks:
    start_index = article.find(chunk, start_index)
    end_index = start_index + len(chunk)

    print("Chunk ID:", chunk_id)
    print("Start Index:", start_index)
    print("End Index:", end_index)
    print("Text:", chunk)

    start_index = end_index - overlap
    chunk_id += 1