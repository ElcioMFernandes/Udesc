# Implementar uma tabela hash com os métodos de sondagem
# linear, sondagem quadrática e duplo hash
# − Considere uma tabela de 7 posições
# − Inicialize a tabela com None
# − Insira os itens 14, 15, 1, 35 e 18 (nessa ordem) testando:
# ● Inserção sem sondagem e exiba a tabela
# ● Inserção com sondagem linear e exiba a tabela
# ● Inserção com sondagem quadrática e exiba a tabela
# ● Inserção com sondagem duplo hash e exiba a tabela
# − Descreva o que ocorre em cada tipo de inserção e verifique se
# todos os itens foram inseridos na tabela corretamente

# Função que insere os itens da tabela hash sem sondagem
# def insert(hashtable, item):
#     index = item % len(hashtable)
#     if hashtable[index] is not None:
#         print(f"Posição {index} já ocupada por {hashtable[index]}")
#     else:
#         hashtable[index] = item
#         print(f"Item {item} inserido na posição {index}")
#     print(hashtable)
# Resultado:
# Item 14 inserido na posição 0
# [14, None, None, None, None, None, None]
# Item 15 inserido na posição 1
# [14, 15, None, None, None, None, None]
# Posição 1 já ocupada por 15
# [14, 15, None, None, None, None, None]
# Posição 0 já ocupada por 14
# [14, 15, None, None, None, None, None]
# Item 18 inserido na posição 4
# [14, 15, None, None, 18, None, None]
#
# Os itens não foram totalmente inseridos na tabela hash, isso acontece porque os itens 14, 15 e 18 ocuparam as posições 0, 1 e 4. O item 1 não foi inserido porque a posição 1 já estava ocupada pelo item 15. O item 35 não foi inserido porque a posição 0 já estava ocupada pelo item 14. Portanto, a tabela hash ficou com os itens 14, 15 e 18 nas posições 0, 1 e 4 respectivamente.

# Função que insere os itens da tabela hash com sondagem linear
# def insert(hashtable, item):
#     index = item % len(hashtable)
#     original = index
#     while hashtable[index] is not None:
#         print(f"Posição {index} já ocupada por {hashtable[index]}")
#         index = (index + 1) % len(hashtable)
#         if index == original:
#             print("Tabela cheia")
#             return
#     hashtable[index] = item
#     print(f"Item {item} inserido na posição {index}")
#     print(hashtable)
#
# Resultado:
# Item 14 inserido na posição 0
# [14, None, None, None, None, None, None]
# Item 15 inserido na posição 1
# [14, 15, None, None, None, None, None]
# Posição 1 já ocupada por 15
# Item 1 inserido na posição 2
# [14, 15, 1, None, None, None, None]
# Posição 0 já ocupada por 14
# Posição 1 já ocupada por 15
# Posição 2 já ocupada por 1
# Item 35 inserido na posição 3
# [14, 15, 1, 35, None, None, None]
# Item 18 inserido na posição 4
# [14, 15, 1, 35, 18, None, None]
#
# Os itens novamente não foram totalmente inseridos na tabela hash, isso acontece porque os itens 14, 15, 1, 35 e 18 ocuparam as posições 0, 1, 2, 3 e 4. Portanto, a tabela hash ficou com os itens 14, 15, 1, 35 e 18 nas posições 0, 1, 2, 3 e 4.

# Função que insere os itens da tabela hash com sondagem quadrática
# def insert(hashtable, item):
#     index = item % len(hashtable)
#     original = index
#     i = 1
#     while hashtable[index] is not None:
#         print(f"Posição {index} já ocupada por {hashtable[index]}")
#         index = (original + i * i) % len(hashtable)
#         i += 1
#         if index == original:
#             print("Tabela cheia")
#             return
#     hashtable[index] = item
#     print(f"Item {item} inserido na posição {index}")
#     print(hashtable)

# Resultado:
# Item 14 inserido na posição 0
# [14, None, None, None, None, None, None]
# Item 15 inserido na posição 1
# [14, 15, None, None, None, None, None]
# Posição 1 já ocupada por 15
# Item 1 inserido na posição 2
# [14, 15, 1, None, None, None, None]
# Posição 0 já ocupada por 14
# Posição 1 já ocupada por 15
# Item 35 inserido na posição 4
# [14, 15, 1, None, 35, None, None]
# Posição 4 já ocupada por 35
# Item 18 inserido na posição 5
# [14, 15, 1, None, 35, 18, None]
#
# Os itens não foram totalmente inseridos na tabela hash, isso acontece porque os itens 14, 15, 1, 35 e 18 ocuparam as posições 0, 1, 2, 4 e 5. Portanto, a tabela hash ficou com os itens 14, 15, 1, 35 e 18 nas posições 0, 1, 2, 4 e 5.

# Função que insere os itens da tabela hash com duplo hash
def insert(hashtable, item):
    index = item % len(hashtable)
    original = index
    step = 1 + (item % (len(hashtable) - 1))

    while hashtable[index] is not None:
        print(f"Posição {index} já ocupada por {hashtable[index]}")
        index = (index + step) % len(hashtable)
        if index == original:
            print("Tabela cheia")
            return
    hashtable[index] = item
    print(f"Item {item} inserido na posição {index}")
    print(hashtable)

# Resultado:
# Item 14 inserido na posição 0
# [14, None, None, None, None, None, None]
# Item 15 inserido na posição 1
# [14, 15, None, None, None, None, None]
# Posição 1 já ocupada por 15
# Item 1 inserido na posição 3
# [14, 15, None, 1, None, None, None]
# Posição 0 já ocupada por 14
# Item 35 inserido na posição 6
# [14, 15, None, 1, None, None, 35]
# Item 18 inserido na posição 4
# [14, 15, None, 1, 18, None, 35]
#
# Os itens foram totalmente inseridos na tabela hash, isso acontece porque os itens 14, 15, 1, 35 e 18 ocuparam as posições 0, 1, 3, 6 e 4. Portanto, a tabela hash ficou com os itens 14, 15, 1, 35 e 18 nas posições 0, 1, 3, 6 e 4.

def main():
    hashtable = [None] * 7

    items = [14, 15, 1, 35, 18]
    # Inserção sem sondagem
    for item in items:
        insert(hashtable, item)

main()