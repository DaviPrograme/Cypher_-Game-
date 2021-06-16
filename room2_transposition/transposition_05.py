string = "QRTSQEKIQDTAQNWA"

splited = string.split("Q")
answer = ""
for substr in splited:
    answer = "".join((answer, substr[::-1]))
print answer