lijst = ["speedfight","cbr650r","tzr50","mt5","r6","runner","zip-t3","typhoon","tomos","skr125"]
lijst = shuffle(lijst);
function shuffle(array) {
    let currentIndex = array.length,  randomIndex;
  
    // While there remain elements to shuffle.
    while (currentIndex != 0) {
  
      // Pick a remaining element.
      randomIndex = Math.floor(Math.random() * currentIndex);
      currentIndex--;
  
      // And swap it with the current element.
      [array[currentIndex], array[randomIndex]] = [
        array[randomIndex], array[currentIndex]];
    }
  
    return array;
}

for (let i=0; i <20;i++){

const image = document.createElement("img");
image.src = "images/background.png";

buttons.appendChild(image);
}