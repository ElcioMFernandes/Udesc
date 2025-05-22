table = {}

def compress(data):

    dictionary = {chr(i): i for i in range(256)}
    next_code = 256

    result = []
    w = ""

    for c in data:
        wc = w + c

        if wc in dictionary:
            w = wc

        else:
            result.append(dictionary[w])

            dictionary[wc] = next_code
            next_code += 1
            w = c
    if w:
        result.append(dictionary[w])

    return result

def decompress(data):
    dictionary = {i: chr(i) for i in range(256)}
    next_code = 256

    w = chr(data[0])
    result = [w]

    for k in data[1:]:
        if k in dictionary:
            entry = dictionary[k]
        elif k == next_code:
            entry = w + w[0]
        else:
            raise ValueError("Invalid compressed data")

        result.append(entry)

        if next_code < 4096:
            dictionary[next_code] = w + entry[0]
            next_code += 1

        w = entry

    return ''.join(result)

result = compress("Olá, meu nome é Élcio Mateus Fernandes")
print(result)
decompressed = decompress(result)
print(decompressed)