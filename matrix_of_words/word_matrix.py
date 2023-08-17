mw_scroll_down = ["przewiń w dół"]
mw_scroll_up = ["przewiń w górę"]
mw_back = ["cofnij strone"]
mw_next = [""]
mw_localize = ["znajdź", "pokaż", "zlokalizuj", "lokalizuj", "wykryj"]
mw_type = ["wpisz tekst", "napisz", "wpisz"]
mw_remove = ["wpisz tekst", "napisz", "wpisz"]
mw_click = ["kliknij", "naciśnij", "wciśnij"]
mw_browse = ["wyszukaj", "otwórz strone", "przejdź pod adres"]
mw_finish = ["zakończ", "wyjdź"]

mw_stopwords277 = "a, aby, ach, acz, aczkolwiek, aj, albo, ale, ależ, ani, aż, bardziej, bardzo, bo, bowiem, by, byli, bynajmniej, być, był, była, było, były, będzie, będą, cali, cała, cały, ci, cię, ciebie, co, cokolwiek, coś, czasami, czasem, czemu, czy, czyli, daleko, dla, dlaczego, dlatego, do, dobrze, dokąd, dość, dużo, dwaj, dwie, dwoje, dziś, dzisiaj, gdy, gdyby, gdyż, gdzie, gdziekolwiek, gdzieś, go, i, ich, ile, im, inna, inne, inny, innych, iż, ja, ją, jak, jakaś, jakby, jaki, jakichś, jakie, jakiś, jakiż, jakkolwiek, jako, jakoś, je, jeden, jedna, jedno, jednak, jednakże, jego, jej, jemu, jest, jestem, jeszcze, jeśli, jeżeli, już, ją, każdy, kiedy, kilka, kimś, kto, ktokolwiek, ktoś, która, które, którego, której, który, których, którym, którzy, ku, lat, lecz, lub, ma, mają, mało, mam, mi, mimo, między, mną, mnie, mogą, moi, moim, moja, moje, może, możliwe, można, mój, mu, musi, my, na, nad, nam, nami, nas, nasi, nasz, nasza, nasze, naszego, naszych, natomiast, natychmiast, nawet, nią, nic, nich, nie, niech, niego, niej, niemu, nigdy, nim, nimi, niż, no, o, obok, od, około, on, ona, one, oni, ono, oraz, oto, owszem, pan, pana, pani, po, pod, podczas, pomimo, ponad, ponieważ, powinien, powinna, powinni, powinno, poza, prawie, przecież, przed, przede, przedtem, przez, przy, roku, również, sam, sama, są, się, skąd, sobie, sobą, sposób, swoje, ta, tak, taka, taki, takie, także, tam, te, tego, tej, temu, ten, teraz, też, to, tobą, tobie, toteż, trzeba, tu, tutaj, twoi, twoim, twoja, twoje, twym, twój, ty, tych, tylko, tym, u, w, wam, wami, was, wasz, wasza, wasze, we, według, wiele, wielu, więc, więcej, wszyscy, wszystkich, wszystkie, wszystkim, wszystko, wtedy, wy, właśnie, z, za, zapewne, zawsze, ze, zł, znowu, znów, został, żaden, żadna, żadne, żadnych, że, żeby".split(', ')
part_of_speech = {
    '.': '.',
    ',': ',',
    'CC': 'Spójnik współrzędny',
    'CD': 'Liczebnik główny',
    'DT': 'Określnik',
    'EX': 'Rzeczownik egzystencjalny',
    'FW': 'Wyraz obcy',
    'IN': 'Przyimek lub spójnik podrzędny',
    'JJ': 'Przymiotnik',
    'JJR': 'Przymiotnik, stopień wyższy',
    'JJS': 'Przymiotnik, stopień najwyższy',
    'LS': 'Znacznik elementu listy',
    'MD': 'Czasownik modalny',
    'NN': 'Rzeczownik, pojedyncza lub zbiorowa forma',
    'NNS': 'Rzeczownik, liczba mnoga',
    'NNP': 'Rzeczownik własny, pojedyncza forma',
    'NNPS': 'Rzeczownik własny, liczba mnoga',
    'PDT': 'Określnik poprzedzający',
    'POS': 'Zakończenie dzierżawcze',
    'PRP': 'Zaimek osobowy',
    'PRP$': 'Zaimek dzierżawczy',
    'RB': 'Przysłówek',
    'RBR': 'Przysłówek, stopień wyższy',
    'RBS': 'Przysłówek, stopień najwyższy',
    'RP': 'Cząstka',
    'SYM': 'Symbol',
    'TO': 'do',
    'UH': 'Wykrzyknik',
    'VB': 'Czasownik w formie podstawowej',
    'VBD': 'Czasownik w czasie przeszłym',
    'VBG': 'Czasownik w formie imiesłowu czasu teraźniejszego',
    'VBN': 'Czasownik w formie imiesłowu czasu przeszłego',
    'VBP': 'Czasownik w teraźniejszym czasie, poza 3. osobą liczby pojedynczej',
    'VBZ': 'Czasownik w teraźniejszym czasie, 3. osoba liczby pojedynczej',
    'WDT': 'Określnik pytający',
    'WP': 'Zaimek pytający',
    'WP$': 'Zaimek dzierżawczy pytający',
    'WRB': 'Przysłówek pytający'
}