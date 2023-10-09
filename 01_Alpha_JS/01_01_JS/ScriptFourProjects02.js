const prompt = require("prompt-sync")();

const target = 10 + Math.round(Math.random() * 90); // Or you can write as "const target = Math.round(Math.random() * 100);" //

let guesses = 0;
console.log(target);

while (true) {
  guesses++;

  const guess = Number(prompt("Guess a number between 1 and 100: "));
  if(guess > target) {
  console.log("Too high, try again");
  } else if (guess < target) {
  console.log("Too low, try again");
  } else {
    console.log("You guessed it");
    break;
  }
}

console.log("You guessed it in", guesses, "tries!");