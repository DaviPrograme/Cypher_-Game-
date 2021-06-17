from enigma2021 import enigma2021

CRYPTO = "JCWSVLIVLVGSJJFJCWCVL"
ALPHABET_BASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for char1 in ALPHABET_BASE:
    for char2 in ALPHABET_BASE:
        for char3 in ALPHABET_BASE:
            pwd_test = []
            pwd_test.append(char1)
            pwd_test.append(char2)
            pwd_test.append(char3)
            answer = enigma2021(pwd_test, CRYPTO, ALPHABET_BASE)
            if "THE" in answer:
                print pwd_test
                print answer
                print ""