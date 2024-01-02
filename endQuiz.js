document.addEventListener('DOMContentLoaded', (event) => {
    const finalScore = localStorage.getItem('finalScore');
    const finalScoreElement = document.getElementById('final-score');
    if (finalScoreElement) {
        finalScoreElement.textContent = finalScore;
    }
});