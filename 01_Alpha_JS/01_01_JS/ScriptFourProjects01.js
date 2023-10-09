const prompt = require("prompt-sync")();

console.log("Welcome to the Brain Games!");

let correctAnswers = 0;
let TotalQuestions = 3;

const answer1 = prompt("What is the brain of a computer? ");
const correctAnswer1 = "CPU";

if (answer1.toUpperCase() === correctAnswer1) {
  console.log("You've got it correct");
  correctAnswers ++;
  // correctAnswers = correctAnswers + 1 //
  // correctAnswers += 1 //
} else {
  console.log("You've got it wrong");
}

const answer2 = prompt("Which one is better a 3090ti or a 4060? ");
const correctAnswer2 = "3090ti";

if (answer2.toLowerCase() === correctAnswer2) {
  console.log("You've got it correct");
  correctAnswers ++;
  // correctAnswers = correctAnswers + 1 //
  // correctAnswers += 1 //
} else {
  console.log("You've got it wrong");
}

const answer3 = prompt("What is the recommended RAM in 2023? (8GB or 16GB or 32GB)" );
const correctAnswer3 = "16GB";

if (answer3.toUpperCase() === correctAnswer3) {
  console.log("You've got it correct");
  correctAnswers ++;
  // correctAnswers = correctAnswers + 1 //
  // correctAnswers += 1 //
} else {
  console.log("You've got it wrong");
}

console.log("You got " + correctAnswers + " correct answers out of " +TotalQuestions);

const percent = Math.round((correctAnswers / TotalQuestions) * 100);
console.log("You scored", percent.toString() + "%"); // Converted the variable / percent to a string, then added another string "%" to it //




