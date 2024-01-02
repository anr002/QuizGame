document.addEventListener('DOMContentLoaded', (event) => {
    const finalScore = localStorage.getItem('finalScore');
    const finalScoreElement = document.getElementById('final-score');
    if (finalScoreElement) {
        finalScoreElement.textContent = finalScore;
    }
});

function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
}

document.getElementById('dark-mode-toggle').addEventListener('click', function() {
    toggleDarkMode();
});