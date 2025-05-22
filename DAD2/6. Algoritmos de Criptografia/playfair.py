def build(keyword:str) -> list:
    keyword = keyword.upper().replace(" ", "")

    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    unique_keyword = ""
    for char in keyword:
        if char in alphabet and char not in unique_keyword:
            unique_keyword += char

    for char in alphabet:
        if char not in unique_keyword:
            unique_keyword += char

    matrix = []
    for i in range(0, 25, 5):
        matrix.append(unique_keyword[i:i + 5])

    return matrix

def find(matrix, char):
    if char == "J":
        char = "I"

    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    
    return None

def decrypt(ciphertext, keyword):
    matrix = build(keyword)
    plaintext = ""

    i = 0

    while i < len(ciphertext) - 1:
        char1, char2 = ciphertext[i], ciphertext[i + 1]

        row1, col1 = find(matrix, char1)
        row2, col2 = find(matrix, char2)

        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5]
            plaintext += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1]
            plaintext += matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += matrix[row1][col2]
            plaintext += matrix[row2][col1]

        i += 2
    
    return plaintext

def main():
    keyword = "SEGURANCA"
    ciphertext = "FDUSFPFACNMENMDSUROSDOMEVFNINATNSNGVGFRV"

    plaintext = decrypt(ciphertext, keyword)
    print("Texto original:", plaintext)

if __name__ == "__main__":
    main()

    def b(k):
    k = k.upper().replace(" ", "")
    a = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    u = ""
    for c in k:
        if c in a and c not in u:
            u += c
    for c in a:
        if c not in u:
            u += c
    m = []
    for i in range(0, 25, 5):
        m.append(u[i:i + 5])
    return m

def f(m, c):
    if c == "J":
        c = "I"
    for i in range(5):
        for j in range(5):
            if m[i][j] == c:
                return i, j
    return None

def d(c, k):
    m = b(k)
    p = ""
    i = 0

    while i < len(c) - 1:
        fl, sl = c[i], c[i + 1]
        fr, fl = f(m, fl)
        sr, sc = f(m, sl)
        if fr == sr:
            p += m[fr][(fl - 1) % 5]
            p += m[sr][(sc - 1) % 5]
        elif fl == sc:
            p += m[(fr - 1) % 5][fl]
            p += m[(sr - 1) % 5][sc]
        else:
            p += m[fr][sc]
            p += m[sr][fl]

        i += 2
    
    return p

def m(k, c):
    print(d(c, k))

if __name__ == "__main__":
    m("SEGURANCA", "FDUSFPFACNMENMDSUROSDOMEVFNINATNSNGVGFRV")