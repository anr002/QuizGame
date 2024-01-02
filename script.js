import gods from './godsData.js';

let currentGodAbilities = []; // Declare and initialize at the top of your script or inside DOMContentLoaded
let currentGodIndex = 0;
let currentQuestionNumber = 0;
let score = 0;
let hintCount = 0;
    
// Use the DOMContentLoaded event to ensure the DOM is fully loaded before running code that interacts with it
document.addEventListener('DOMContentLoaded', (event) => {
  // Retrieve the final score from localStorage
  const finalScore = localStorage.getItem('finalScore');

  
  // Display the final score
  const finalScoreElement = document.getElementById('final-score');
  
  if (finalScoreElement) {
      finalScoreElement.textContent = finalScore;
  }
    const endQuizButton = document.getElementById('end-quiz-button');
    if (endQuizButton) {
        endQuizButton.addEventListener('click', endQuiz);
    }
    const mode1Button = document.getElementById('mode1');
if (mode1Button) {
    mode1Button.addEventListener('click', function() {
        resetGame();
        startGameMode1();
    });
}

const mode2Button = document.getElementById('mode2');
if (mode2Button) {
    mode2Button.addEventListener('click', function() {
        resetGame();
        startGameMode2();
    });
}

const hintButton = document.getElementById('hint-button');
if (hintButton) {
    hintButton.addEventListener('click', handleHint);
}

    // Start the game
    startGameMode1();
});
    
function endQuiz() {
  console.log('Ending the game. Final score:', score);

  // Save the score in localStorage
  localStorage.setItem('finalScore', score);


  window.location.href = 'endQuiz.html';
}




function resetGame() {
    // Reset the game state if necessary
    // This could include resetting the score, the current question number, etc.
    // You may also want to clear any existing buttons or images
}

function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        let j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}


function getRandomGods(correctGod) {
    let incorrectGods = [];
    while (incorrectGods.length < 3) {
        let randomGod = gods[Math.floor(Math.random() * gods.length)];
        if (randomGod.name !== correctGod.name && !incorrectGods.includes(randomGod)) {
            incorrectGods.push(randomGod);
        }
    }
    return incorrectGods;
}


    function toggleDarkMode() {
        document.body.classList.toggle('dark-mode');
    }
    
    document.getElementById('dark-mode-toggle').addEventListener('click', function() {
        toggleDarkMode();
    });

// Declare these variables outside of the function so they can be accessed by other functions

function startGameMode1() {
  // Hide abilities
  const hintButton = document.getElementById('hint-button');
  if (hintButton) {
    hintButton.classList.remove('hint-button-visible');
    hintButton.classList.add('hint-button-hidden');
  }

  const abilityContainer = document.querySelector('.ability-container');
  if (abilityContainer) {
    abilityContainer.style.display = 'none';
  }

  let abilities = document.querySelectorAll('.ability');
  abilities.forEach(ability => {
      ability.style.display = 'none';
  });

  // Show the god icon
    const gameImage = document.getElementById('game-image');
    if (gameImage) {
        gameImage.style.display = 'block';
    }

  // Shuffle the gods array
  shuffleArray(gods);

  // Reset variables
  currentGodIndex = 0;
  currentQuestionNumber = 0;
  score = 0;
  
  // Call loadQuestionMode1 to start the game
  loadQuestionMode1();
}


function loadQuestionMode1() {
  // Get the current god
  let correctGod = gods[currentGodIndex];

  // Get three random gods that are not the correct god
  let incorrectGods = getRandomGods(correctGod);

  // Combine the correct god with the incorrect ones and shuffle
  let options = [correctGod, ...incorrectGods];
  shuffleArray(options);

  // Set the question image
  const gameImage = document.getElementById('game-image');
  if (gameImage) {
      gameImage.src = correctGod.icon;
  }
  const questionCounter = document.getElementById('question-counter');
  if (questionCounter) {
      questionCounter.textContent = `Question: ${currentQuestionNumber + 1} / ${gods.length}`;
  } 

  const scoreElement = document.getElementById('score');
  if (scoreElement) {
      scoreElement.textContent = `Score: ${score}`;
  }
  // Clear old buttons and create new ones
    const buttonContainer = document.getElementById('button-container');
    if (buttonContainer) {
        buttonContainer.innerHTML = '';
        // ... rest of your code that uses buttonContainer ...
    }
  options.forEach(option => {
      const btn = document.createElement('button');
      btn.className = 'btn btn-primary mx-3 mb-2';
      btn.type = 'button';
      btn.textContent = option.name;
      btn.onclick = () => {
          if (option.name === correctGod.name) {
              // Correct answer
              score++;
          }
          currentQuestionNumber++;
          if (currentQuestionNumber < gods.length) {
              loadQuestionMode1();
          } else {
              // Game over
              document.getElementById('final-score').textContent = score;
              document.getElementById('total-questions').textContent = gods.length;
              //$('#gameOverModal').modal('show');
          }
      };
      buttonContainer.appendChild(btn);
  });

  // Increment currentGodIndex and reset if necessary
  currentGodIndex++;
  if (currentGodIndex === gods.length) {
      currentGodIndex = 0;
  }
}



function startGameMode2() {
    // Show abilities
    document.getElementById('hint-button').classList.remove('hint-button-hidden');
    document.getElementById('hint-button').classList.add('hint-button-visible');

    document.querySelector('.ability-container').style.display = 'flex';
    // Hide the god icon
    document.getElementById('game-image').style.display = 'none';
    // Reset variables
    score = 0;
    currentQuestionNumber = 0;
    // Start the game
    loadQuestionBasedOnAbilities();
}

function handleHint() {
  if (hintCount < 4) {
      hintCount++;
      let abilityElement = document.getElementById(`ability${hintCount}`);
      if (abilityElement && currentGodAbilities[hintCount - 1]) {
          abilityElement.src = currentGodAbilities[hintCount - 1];
          abilityElement.style.display = 'block';
      } else {
          console.error(`No ability found for hint count: ${hintCount}`);
      }
  }
}



function loadQuestionBasedOnAbilities() {
  hintCount = 1; // Reset hintCount for each new question

  // Randomly select a god
  let correctGod = gods[Math.floor(Math.random() * gods.length)];
  // Get the god's abilities and store them in the currentGodAbilities variable
  currentGodAbilities = correctGod.abilities;

  // Initially, only display the first ability to the player
  for (let i = 0; i < 4; i++) {
      let abilityElement = document.getElementById(`ability${i + 1}`);
      if (abilityElement) {
          if (i === 0 && currentGodAbilities[i]) { // Only the first ability is displayed initially
              abilityElement.src = currentGodAbilities[i];
              abilityElement.style.display = 'block';
          } else {
              abilityElement.style.display = 'none'; // Hide the other abilities
          }
      } else {
          console.error(`Element with ID ability${i + 1} not found.`);
      }
  }

    // Clear old buttons and create new ones
    const buttonContainer = document.getElementById('button-container');
    buttonContainer.innerHTML = '';
    let options = [correctGod, ...getRandomGods(correctGod)];
    shuffleArray(options);
    options.forEach(option => {
        const btn = document.createElement('button');
        btn.className = 'btn btn-primary mx-3 mb-2';
        btn.type = 'button';
        btn.textContent = option.name;
        // In your button click handler
        btn.onclick = () => {
          if (option.name === correctGod.name) {
              // Correct answer
              // Decrease the score increment based on the number of hints used
              let scoreIncrement = 1; // Full points if no hints were used
              if (hintCount === 2) {
                  scoreIncrement = 0.75; // 75% of points if 1 hint was used
              } else if (hintCount === 3) {
                  scoreIncrement = 0.5; // 50% of points if 2 hints were used
              } else if (hintCount >= 4) {
                  scoreIncrement = 0.25; // 25% of points if 3 or more hints were used
              }
              score += scoreIncrement;
          }
            currentQuestionNumber++;
            if (currentQuestionNumber <= gods.length) {
                loadQuestionBasedOnAbilities();
            } else {
                // Game over
                document.getElementById('final-score').textContent = score;
                document.getElementById('total-questions').textContent = gods.length;
                //$('#gameOverModal').modal('show');
            }
        };
        buttonContainer.appendChild(btn);
    });

    // Update the score and question counter


    
    document.getElementById('score').textContent = `Score: ${score}`;
    document.getElementById('question-counter').textContent = `Question: ${currentQuestionNumber + 1} / ${gods.length}`;

}