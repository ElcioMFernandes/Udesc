# Lista invertida básica

docs = {
    "doc1.txt": "Água mole, pedra dura, tanto bate até que fura",
    "doc2.txt": "Três pratos de trigo para três tigres tristes",
    "doc3.txt": "A aranha arranha a rã, a rã arranha a aranha",
    "doc4.txt": "O rato roeu a roupa do rei de Roma",
    "doc5.txt": "O sabiá não sabia que o sábio sabia que o sabiá não sabia",
    "doc6.txt": "A vaca malhada foi molhada por outra vaca malhada",
}

index = {}

for doc, text in docs.items():
    for char in text.split():
        char_lower = char.lower()
        if char_lower not in index:
            index[char_lower] = {}
        if doc not in index[char_lower]:
            index[char_lower][doc] = 0
        index[char_lower][doc] += 1


doc_names = list(docs.keys())
header = ["Palavra"] + doc_names
print("{:<15}".format(header[0]), end=" | ")
for doc in header[1:]:
    print("{:<10}".format(doc), end=" | ")
print()

for char in sorted(index.keys()):
    print("{:<15}".format(char), end=" | ")
    for doc in doc_names:
        print("{:<10}".format(index[char].get(doc, 0)), end=" | ")
    print()