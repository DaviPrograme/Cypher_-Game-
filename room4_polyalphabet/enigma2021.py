ALPHABET_BASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CRYPTO = "ZTVGLKDBGLRUHABTUOZ"
PWD = "FLASH"


def cifra_vigenere():
    count_chars = len(ALPHABET_BASE)
    table = []
    limit_loops = count_chars
    count_loops = 0
    while count_loops < limit_loops:
        table.append([])
        count_rows = 1
        while count_rows <= count_chars:
            if count_loops + count_rows < count_chars:
                table[count_loops].append(ALPHABET_BASE[count_loops + count_rows])
            else:
                table[count_loops].append(ALPHABET_BASE[count_loops + count_rows - count_chars])
            count_rows += 1
        count_loops += 1
    return table


def index_key_word(keyword):
    list_index = []
    for char in keyword:
        index = 0
        while ALPHABET_BASE[index] != char:
            index += 1
        list_index.append(index)
    return list_index


def view_vigenere(table):
    linha = 1
    for alpha in table:
        print "line: {:0>2} | alpha: {}".format(linha, alpha)
        linha += 1


def enigma2021():
    matriz = cifra_vigenere()
    index_key = 0
    answer = ""
    keys = index_key_word(PWD)
    for c in CRYPTO:
        colum = 0
        if index_key >= len(keys):
            index_key = 0
        while matriz[keys[index_key]][colum] != c:
            colum += 1
        answer = "".join((answer, ALPHABET_BASE[colum]))
        index_key += 1
    print answer


enigma2021()