# ZAINSTALOWALEM:
# Pattern
# GENSIM
# NLTK
# import nltk

# nltk.download()
# nltk.download()

# naprawilo wszystko te 3 ponizej
# nltk.download('punkt')
# nltk.download('plwordnet')
# nltk.download('omw-1.4')

zdanie = "NIEDZIALA DO USUNIECIA."


def elo():
    import nltk
    zdanie = "To jest przykładowe zdanie."
    tokeny = nltk.word_tokenize(zdanie)
    print(tokeny)
    etykiety = nltk.pos_tag(tokeny)
    print(etykiety)

    # from nltk.corpus import wordnet
    # slowo = "wpisz"
    # synonimy = wordnet.synsets(slowo, lang="pl-PL")
    # print(synonimy)


def elo1():
    import nltk
    from nltk.corpus import stopwords

    zdanie = "To jest przykładowe zdanie, które zawiera nieistotowe słowa."
    tokeny = nltk.word_tokenize(zdanie)
    tokeny_oczyszczone = [slowo for slowo in tokeny if slowo.lower() not in stopwords.words()]
    print(tokeny_oczyszczone)


def elo2():
    import nltk
    from nltk import FreqDist
    zdanie = "To jest przykład zdania, które zawiera kilka powtórzeń słów."
    tokeny = nltk.word_tokenize(zdanie)
    czestotliwosc = FreqDist(tokeny)
    print(czestotliwosc.most_common(3))


#
# elo()

def test3():
    def wykonaj_klikanie(tekst):
        from nltk.tokenize import word_tokenize, wordpunct_tokenize

        tokeny = word_tokenize(tekst.lower())
        tokeny2 = wordpunct_tokenize(tekst.lower())
        print(tokeny)
        print(tokeny2)
        if 'kliknij' in tokeny or 'klik' in tokeny:
            # Wykonaj funkcję klikania
            print("Kliknięto!")
        else:
            print("Nie znaleziono słowa 'kliknij' ani 'klik'.")

    tekst_1 = "Kliknij tutaj, aby przejść do strony."
    wykonaj_klikanie(tekst_1)

    tekst_2 = "Proszę, kliknij ten przycisk."
    wykonaj_klikanie(tekst_2)


def test4():
    from nltk.tokenize import word_tokenize
    from nltk.tag import pos_tag

    def sprawdz_rzeczownik(tekst, slowo_kliknij):
        from matrix_of_words.word_matrix import mw_stopwords277
        stop_words = set(mw_stopwords277)  # Pobieramy listę zbędnych wyrazów dla języka polskiego

        tekst = tekst.lower()
        slowo_kliknij = slowo_kliknij.lower()
        tokeny = word_tokenize(tekst)
        for ttk in tokeny:
            print(ttk, pos_tag([ttk]))

        tokeny_bez_stopwords = [token for token in tokeny if token.lower() not in stop_words]  # Usuwamy zbędne wyrazy

        # print(tokeny)
        # print(tokeny_bez_stopwords)

        # Znajdujemy indeks wybranego słowa "kliknij"
        indeks_kliknij = tokeny_bez_stopwords.index(slowo_kliknij)
        if indeks_kliknij + 1 < len(tokeny_bez_stopwords):
            kolejny_token = tokeny_bez_stopwords[indeks_kliknij + 1]
            tagi = pos_tag([kolejny_token])
            # print(tagi)
            if tagi[0][1].startswith('N'):  # Sprawdzamy, czy kolejny token jest rzeczownikiem (zaczyna się od 'N')
                print(f"Po słowie '{slowo_kliknij}' znajduje się rzeczownik '{kolejny_token}'.")
            else:
                print(f"Po słowie '{slowo_kliknij}' nie znajduje się rzeczownik.")
        else:
            print(f"Po słowie '{slowo_kliknij}' nie ma kolejnego słowa.")

    # Przykładowe użycie
    tekst_1 = "Kliknij przycisk, aby zatwierdzić."
    slowo_kliknij_1 = "Kliknij"
    sprawdz_rzeczownik(tekst_1, slowo_kliknij_1)

    tekst_2 = "Kliknij na link, aby otworzyć stronę."
    slowo_kliknij_2 = "Kliknij"
    sprawdz_rzeczownik(tekst_2, slowo_kliknij_2)

    tekst_3 = "Kliknij dwa razy, aby uruchomić aplikację."
    slowo_kliknij_3 = "Kliknij"
    sprawdz_rzeczownik(tekst_3, slowo_kliknij_3)


def test5():
    from nltk.tokenize import word_tokenize
    from nltk.tag import pos_tag

    def sprawdz_rzeczownik(tekst, slowo_kliknij):
        tokeny = word_tokenize(tekst)
        indeks_kliknij = tokeny.index(slowo_kliknij)  # Znajdujemy indeks wybranego słowa "kliknij"
        if indeks_kliknij + 1 < len(tokeny):
            kolejny_token = tokeny[indeks_kliknij + 1]
            tagi = pos_tag([kolejny_token])
            if tagi[0][1].startswith('N'):  # Sprawdzamy, czy kolejny token jest rzeczownikiem (zaczyna się od 'N')
                print(f"Po słowie '{slowo_kliknij}' znajduje się rzeczownik '{kolejny_token}'.")
            else:
                print(f"Po słowie '{slowo_kliknij}' nie znajduje się rzeczownik.")
        else:
            print(f"Po słowie '{slowo_kliknij}' nie ma kolejnego słowa.")

    # Przykładowe użycie
    tekst_1 = "Kliknij przycisk, aby zatwierdzić."
    slowo_kliknij_1 = "Kliknij"
    sprawdz_rzeczownik(tekst_1, slowo_kliknij_1)

    tekst_2 = "Kliknij na link, aby otworzyć stronę."
    slowo_kliknij_2 = "Kliknij"
    sprawdz_rzeczownik(tekst_2, slowo_kliknij_2)

    tekst_3 = "Kliknij dwa razy, aby uruchomić aplikację."
    slowo_kliknij_3 = "Kliknij"
    sprawdz_rzeczownik(tekst_3, slowo_kliknij_3)


def test6():
    def kategoryzuj_czesci_mowy(zdanie):
        from nltk.tokenize import word_tokenize
        from nltk.tag import pos_tag
        tokeny = word_tokenize(zdanie)
        tagi = pos_tag(tokeny)
        return tagi

    def translate_tags(tags):
        from matrix_of_words.word_matrix import part_of_speech
        for token, tag in tags:
            print("%s - %s" % (token, part_of_speech[tag]))

    zdanie = "Dzięki takiemu algorytmowi można dokonywać analizy składniowej i kategoryzacji zdania na podstawie jego części mowy."
    res = kategoryzuj_czesci_mowy(zdanie)

    print(res)
    translate_tags(res)


test4()


######################################################################
def znajdz_synonim(slowa="cześć"):
    # import plwordnet
    # plwn = plwordnet.load('./drivers/plwordnet_3_0/plwordnet-3.0.xml')
    from nltk.corpus import wordnet as wn
    import re

    # Znalezienie synsetów dla danego słowa
    for slowo in re.split(r"[,  !?]", slowa):
        synsety = wn.synsets(slowo, lang='pol')
        lemmm = wn.lemmas(slowo, lang='pol')
        # print(lemmm)
        if synsety:
            print(f"Synonimy dla słowa '{slowo}':")
            for synset in synsety:
                synonimy = [lemma.name() for lemma in synset.lemmas(lang='pol')]
                print(synonimy)
        else:
            print(f"Nie znaleziono synonimów dla słowa '{slowo}'.")


# sprawdzenie czy zdanie jest twierdzace lub zaprzeczające
def test8():
    """from nltk.sentiment import SentimentIntensityAnalyzer

    def sprawdz_zdanie(zdanie):
        sid = SentimentIntensityAnalyzer()
        wynik = sid.polarity_scores(zdanie)
        compound_score = wynik['compound']

        if compound_score >= 0.05:
            return "Twierdzenie"
        elif compound_score <= -0.05:
            return "Przeczenie"
        else:
            print(compound_score)
            return "Neutralne"

    # Przykładowe zdania do sprawdzenia
    zdanie1 = "To jest bardzo dobre."
    zdanie2 = "To nie jest prawda."
    zdanie3 = "Jestem zadowolony z wyniku."

    # Sprawdzenie pierwszego zdania
    wynik1 = sprawdz_zdanie(zdanie1)
    print(f"Zdanie 1: {zdanie1} ({wynik1})")

    # Sprawdzenie drugiego zdania
    wynik2 = sprawdz_zdanie(zdanie2)
    print(f"Zdanie 2: {zdanie2} ({wynik2})")

    # Sprawdzenie trzeciego zdania
    wynik3 = sprawdz_zdanie(zdanie3)
    print(f"Zdanie 3: {zdanie3} ({wynik3})")
    """
    import nltk
    from nltk.tokenize import word_tokenize

    def sprawdz_zdanie(zdanie):
        tokeny = word_tokenize(zdanie)
        tagi = nltk.pos_tag(tokeny)

        # Sprawdzenie, czy zdanie zawiera przeczenie
        if 'not' in tokeny or 'nie' in tokeny:
            return "Przeczenie"

        # Sprawdzenie, czy zdanie zaczyna się od czasownika
        if tagi[0][1].startswith('V'):
            return "Twierdzenie"

        return "Neutralne"

    # Przykładowe zdania do sprawdzenia
    zdanie1 = "To jest bardzo dobre."
    zdanie2 = "To nie jest prawda."
    zdanie3 = "Jestem zadowolony z wyniku."

    # Sprawdzenie pierwszego zdania
    wynik1 = sprawdz_zdanie(zdanie1)
    print(f"Zdanie 1: {zdanie1} ({wynik1})")

    # Sprawdzenie drugiego zdania
    wynik2 = sprawdz_zdanie(zdanie2)
    print(f"Zdanie 2: {zdanie2} ({wynik2})")

    # Sprawdzenie trzeciego zdania
    wynik3 = sprawdz_zdanie(zdanie3)
    print(f"Zdanie 3: {zdanie3} ({wynik3})")


# nltk.download("vader_lexicon")
def test9():
    from nltk.sentiment import SentimentIntensityAnalyzer

    sia = SentimentIntensityAnalyzer()

    def dostosuj_wyniki(wynik):
        # Modyfikowanie wartości sentymentu
        wynik['pos'] += 0.1
        wynik['neg'] -= 0.1

        # Normalizacja wartości sentymentu
        suma = wynik['pos'] + wynik['neg'] + wynik['neu']
        wynik['pos'] /= suma
        wynik['neg'] /= suma
        wynik['neu'] /= suma

        return wynik

    tekst = "To jest bardzo dobre."

    wynik = sia.polarity_scores(tekst)
    wynik_dostosowany = dostosuj_wyniki(wynik)

    print("Oryginalne wyniki:")
    print(wynik)

    print("\nDostosowane wyniki:")
    print(wynik_dostosowany)


def test10():
    import plwordnet
    wn = plwordnet.load('plwordnet_4_2.xml')
    print(wn)

    for lu in wn.find('leśny'):
        for s, p, o in wn.lexical_relations_where(subject=lu):
            print(p.format(s, o))


def test11():
    pass

# test10()
# znajdz_synonim('niezdefiniowany')
