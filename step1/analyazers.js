


function drawrect(element, color='red'){
    // var oldStyleBackgroundColor = element.style.background;
    var oldStyleBorder = element.style.border;

    setTimeout(function(){  // element.style.background = 'blue';
        element.style.border = '3px solid '+color;
    }, 1000);

    setTimeout(function(){  // element.style.background = oldStyleBackgroundColor;
        element.style.border = oldStyleBorder;
    }, 6000);
};


function find_texty(findableText){
    // findableText = "okno,domek,ziemniak"
    var matchingElements = [];
    var phrasesCounter = 0;
    var textElement = document.querySelectorAll("span:not(:empty):not(:has(*)), div:not(:empty):not(:has(*))");
    var phrases = findableText.toLowerCase().trim().split(",");

    for (var i = 0; i < textElement.length; i++) {
      var element = textElement[i];
      var textOfElement = element.textContent.toLowerCase();

//   Sprawdź, czy tekst elementu jest niepusty ani niezdefiniowany
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


var ell = [1,2,3,4]
if length(ell) == 3 {

}