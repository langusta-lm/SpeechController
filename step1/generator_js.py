js_get_elements_with_text = """
// Frazy, których szukamy w elementach
var frazy = ["okno", "Okna"];

// Znajdź wszystkie elementy na stronie
var elements = document.querySelectorAll("*");

// Inicjalizacja listy pasujących elementów
var pasujaceElementy = [];

// Inicjalizacja licznika pasujących wyrazów
var liczbaPasujacychWyrazow = 0;

// Iteracja przez znalezione elementy
for (var i = 0; i < elements.length; i++) {
  var element = elements[i];
  var tekstElementu = element.textContent;

  // Sprawdź, czy tekst elementu jest niepusty ani niezdefiniowany
  if (tekstElementu && tekstElementu.trim() !== "") {
    // Podziel tekst elementu na wyrazy
    var wyrazy = tekstElementu.split(" ");

    // Sprawdź, czy każda fraza występuje w tekście elementu
    if (
      wyrazy.includes(frazy[0]) &&
      wyrazy.includes(frazy[1])
      // Dodaj więcej warunków, jeśli potrzebujesz szukać więcej fraz
    ) {
      pasujaceElementy.push(element);
      liczbaPasujacychWyrazow += frazy.length;
    }
  }
}

// Wyświetl wyniki w konsoli
console.log("Pasujące elementy:");
pasujaceElementy.forEach(function (element) {
  console.log(element.innerText);
});
console.log("Liczba pasujących wyrazów z zdania:", liczbaPasujacychWyrazow);

"""



find_texty="""function find_texty(findableText){
    // findableText = "okno,domek,ziemniak"
    var matchingElements = ["dupa"];
    var phrasesCounter = 0;
    var textElement = document.querySelectorAll("span:not(:empty):not(:has(*)), div:not(:empty):not(:has(*))");
    var phrases = findableText.toLowerCase().trim().split(",");

    for (var i = 0; i < textElement.length; i++) {
      var element = textElement[i];
      var textOfElement = element.textContent.toLowerCase();

//       Sprawdź, czy tekst elementu jest niepusty ani niezdefiniowany
      if (textOfElement && textOfElement.trim() !== "") {

        var textsOfElement = textOfElement.split(" ");
        var allWordsIncluded = phrases.every(function (fraza) {
            return textsOfElement.includes(fraza);
        });
        if (allWordsIncluded) {
          console.log("wszystkie phrases wystepuja:");
          matchingElements.push(element);
          phrasesCounter += phrases.length;
        }

      }
    }

    console.log(phrases,"Liczba pasujących wyrazów z zdania:", phrasesCounter);
    return matchingElements;
};
find_texty(arguments[0]);
"""


porysuj_background ="""
function drawrect(element, color='3px solid red', startTime=1000, endTime=6000){
    // var oldStyleBackgroundColor = element.style.background;
    var oldStyleBorder = element.style.border;

    setTimeout(function(){  // element.style.background = 'blue';
        element.style.border = color;
    }, startTime);

    setTimeout(function(){  // element.style.background = oldStyleBackgroundColor;
        element.style.border = oldStyleBorder;
    }, endTime);
};
drawrect(arguments[0], arguments[1], arguments[2], arguments[3]);

"""