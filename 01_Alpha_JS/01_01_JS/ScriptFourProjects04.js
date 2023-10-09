const prompt = require("prompt-sync")();

const answer = prompt("Would you like to play? (y/n) ");

if (answer.toLowerCase() !== "y" && answer.toLowerCase() !== "n") {
  console.log("Please enter a valid answer.");
}
if (answer.toLowerCase() === "y") {
  while (true) {
    const answer2 = prompt("Would you like to go left or right? (l/r) ");
    if (answer2.toLowerCase() !== "l" && answer2.toLowerCase() !== "r") {
    console.log("Please enter a valid answer.");
    continue;
    }
    if (answer2.toLowerCase() === "l") {
      console.log("You are safe at this moment. You just turned right, and are in front of a gate");
    } else {
      console.log("You turned right... Bad choice... You just died!Bye");
      break;
    }
      const answer3 = prompt("Would you like to enter the gate and explore (y/n) ");
      if (answer3.toLowerCase() !== "y" && answer3.toLowerCase() !== "n") {
      console.log("Please enter a valid answer.");
      continue;
    }
      if (answer3.toLowerCase() === "y") {
        console.log("Let's roll! The Gate is now open!");
      } else {
        console.log("You just missed your chance to explore inside the gate! You are officially unadventurous! Bye now. Play again!")
        break;
      }
      const answer4 = prompt("You are now in the gate. Would you like to yell loudly? (y/n) ");
        if (answer4.toLowerCase() !== "y" && answer4.toLowerCase() !== "n") {
      console.log("Please enter a valid answer.");
      continue;
    }
      if (answer4.toLowerCase() === "y") {
        console.log("You just yelled loudly and a group of bats came out and bit you, and you died! ")
      }
      else {
        console.log("You ventured in about 100 metres inside the gate! Great Job! That is it for now. Let's wait for verison 2." );
        break;
    }
  }
}
console.log("Thanks for playing!");