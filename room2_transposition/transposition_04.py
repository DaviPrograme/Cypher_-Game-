string = "SNEJDGNTTEXARONEXXTDAIXXNHHEANRTOIESSXORXDASSEUUO"
matriz_lenght = 7

matriz = []
colum = 0
line = 0
max_colum = 0
for char in string:
    if not colum:
        matriz.append([])
    matriz[line].append(char)
    colum += 1
    if colum >= matriz_lenght:
        max_colum = colum
        colum = 0
        line += 1

answer = ""
line -= 1
min_line = line
last_count = 0
loops = (max_colum * 2) - 2
while loops >= 0:
    if matriz[line][colum] is "X":
        answer = "".join((answer, " "))
    else:
        answer = "".join((answer, matriz[line][colum]))
    if line is matriz_lenght - 1 or colum is matriz_lenght - 1:
        loops -= 1
        if min_line:
            min_line -= 1
        line = min_line
        if not line:
            colum = last_count
            last_count += 1
        else:
            colum = 0
    else:
        line += 1
        colum += 1
    print answer
