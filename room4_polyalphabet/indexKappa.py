#texto = "TEEESRHDEBNAHHEMRE HJWLAEIDNEETTELTE"
#texto = "SHQDOWLHXPDFRLVDWDRLPSRUWDQWHTXHTXHPGHYHULDEDWHUHRSUHVLGHQWHGRFOXEH"
#texto = "JCWSVLIVLVGSJJFJCWCVL"
#texto = "LAFLUIWOYWPADUFHSNBVSWVNDZQDUFRBPLUYQPLWLPHZRLUEDUBSYMIPRDIJHTYQUCUZYLKFRSKHZBUHULUEKPQFOYLYSSAMWOCWHZOLGDTDDPPOFDDTGOPYUDGWOYOSDRYKVVDVLAULRZYGWPLJZYQKYPTWVLJIAFHHSWOMUVDDAPLMJLUEPVLRNPDWFXWMQAFHZSEQCFAGQDFLJFLHLDSWCLMQLFXUBULBDUBVPVWFQHWYUHRHJGSOCUZZXAGFVLILQVAFDARKPQLZCQAGULJBUCZAMPL"
#texto = "CAT"
#texto = "ABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABC"
texto = "QPWKALVRXCQZIKGRBPFAEOMFLJMSDZVDHXCXJYEBIMTRQWNMEAIZRVKCVKVLXNEICFZPZCZZHKMLVZVZIZRRQWDKECHOSNYXXLSPMYKVQXJTDCIOMEEXDQVSRXLRLKZHOV"
ALPHABET_BASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def index_kappa_calculated(crypto, alphabet_base, len_string):
    index_kappa = []
    for char in alphabet_base:
        frequence_char = crypto.count(char)
        kappa_char = float(frequence_char * (frequence_char - 1) / float((len_string * (len_string - 1))))
        index_kappa.append(kappa_char)
    return sum(index_kappa)


def index_coincidence_calculated(crypto, alphabet_base):
    len_string = len(crypto)
    index_kappa_calc = index_kappa_calculated(crypto, alphabet_base, len_string)
    index_coincidence_calc = index_kappa_calc / (1 / float(26))
    return index_coincidence_calc


def index_coincidence_all_country():
    return {"en": 1.73, "fr": 2.02, "pt": 1.94}


def analyzed_lenght_key(crypto, max_length_key):
    step = 1
    len_crypto = len(crypto)
    while step <= max_length_key:
        count = 0
        print "STEP: {}".format(step)
        colum = ""
        start_count = 0
        ic_acumulado = 0
        while start_count < step:
            splited = crypto[count]
            if count + step < len_crypto:
                count += step
            else:
                count = len_crypto
            colum = "".join((colum, splited))
            if count >= len_crypto:
                ic_acumulado += index_coincidence_calculated(colum, ALPHABET_BASE)
                colum = ""
                start_count += 1
                count = start_count
        print "INDICE FINAL DESSE STEP: {}".format(ic_acumulado / float(step))
        print ""
        print ""
        step += 1


#index_coincidence_calculated(texto, ALPHABET_BASE)
analyzed_lenght_key(texto, 17)