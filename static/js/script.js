
const body = document.body;

// ======================================================
// DARK MODE
// ======================================================

function toggleTheme(){

    body.classList.toggle("dark-mode");

    localStorage.setItem(
        "theme",
        body.classList.contains("dark-mode")
        ? "dark"
        : "light"
    );

}

// ======================================================
// LOAD THEME
// ======================================================

window.addEventListener("load", () => {

    const savedTheme = localStorage.getItem("theme");

    if(savedTheme === "dark"){
        body.classList.add("dark-mode");
    }

    generateMatrix(); // 🔥 penting biar matrix langsung muncul

});

// ======================================================
// MOBILE SIDEBAR
// ======================================================

function toggleSidebar(){

    const sidebar = document.querySelector(".sidebar");

    sidebar.classList.toggle("active");

}

// ======================================================
// COPY RESULT
// ======================================================

function copyResult(){

    const result = document.getElementById("resultText");

    navigator.clipboard.writeText(result.innerText);

    alert("Hasil berhasil disalin!");

}

// ======================================================
// LOADING BUTTON
// ======================================================

function showLoading(button){

    button.innerHTML = `
        <span class="spinner-border spinner-border-sm"></span>
        Processing...
    `;

}

// ======================================================
// HISTORY PANEL
// ======================================================

function toggleHistory() {
    document.getElementById("historyPanel").classList.toggle("active");
}

// ======================================================
// AUTO HIDE ALERT
// ======================================================

setTimeout(() => {

    const alertBox = document.querySelector(".auto-hide");

    if(alertBox){
        alertBox.style.display = "none";
    }

}, 4000);

// ======================================================
// ANIMATION CARD
// ======================================================

const cards = document.querySelectorAll(".crypto-card");

cards.forEach((card, index) => {

    card.style.animationDelay = `${index * 0.1}s`;

});

// ======================================================
// MATRIX GENERATOR (FIX UTAMA HILL)
// ======================================================

function generateMatrix() {

    let size = document.getElementById("matrixSize").value;
    let container = document.getElementById("matrixContainer");

    container.innerHTML = "";

    let index = 0;

    for (let i = 0; i < size; i++) {

        let row = document.createElement("div");

        for (let j = 0; j < size; j++) {

            let input = document.createElement("input");

            input.type = "number";
            input.name = "m" + index;
            input.value = "0";   // 🔥 FIX ERROR KOSONG
            input.required = true;

            input.classList.add("form-control");
            input.style.width = "70px";
            input.style.display = "inline-block";
            input.style.margin = "3px";

            row.appendChild(input);

            index++;
        }

        container.appendChild(row);
    }
}