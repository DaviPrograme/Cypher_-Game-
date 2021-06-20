
def cifra_vigenere(alphabet, table_cypher=True):
    count_chars = len(alphabet)
    table = []
    limit_loops = count_chars
    count_loops = 0
    while count_loops < limit_loops:
        table.append([])
        if table_cypher:
            count_rows = 1
            while count_rows <= count_chars:
                table[count_loops].append(alphabet[(count_loops + count_rows) % 26])
                count_rows += 1
        else:
            count_rows = 0
            while count_rows < count_chars:
                table[count_loops].append(alphabet[(count_loops + count_rows) % 26])
                count_rows += 1
        count_loops += 1
    return table


def index_key_word(keyword, alphabet):
    list_index = []
    for char in keyword:
        index = 0
        while alphabet[index] != char:
            index += 1
        list_index.append(index)
    return list_index


def view_vigenere(table):
    linha = 1
    for alpha in table:
        print "line: {:0>2} | alpha: {}".format(linha, alpha)
        linha += 1


def enigma2021(pwd, crypt, alphabet, cypher_table=True):
    matriz = cifra_vigenere(alphabet, cypher_table)
    index_key = 0
    answer = ""
    keys = index_key_word(pwd, alphabet)
    for c in crypt:
        colum = 0
        if index_key >= len(keys):
            index_key = 0
        while matriz[keys[index_key]][colum] != c:
            colum += 1
        answer = "".join((answer, alphabet[colum]))
        index_key += 1
    return answer