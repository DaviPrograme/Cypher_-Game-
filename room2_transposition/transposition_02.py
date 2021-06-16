texto = "TEEESRHDEBNAHHEMRE HJWLAEIDNEETTELTE"

splited = texto.split(" ")
string = ""
num = 0
for c1 in splited[0]:
    string = "".join((string, c1))
    if (num < len(splited[1])):
        string  = "".join((string, splited[1][num]))
    num += 1

print string