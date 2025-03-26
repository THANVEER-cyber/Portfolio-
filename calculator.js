document.querySelectorAll(".btn").forEach(button => {
    button.addEventListener("click", () => {
        const display = document.getElementById("display");
        const value = button.getAttribute("data-value");
        if (value === "C") {
            display.textContent = "0";
        } else if (value === "=") {
            try {
                display.textContent = eval(display.textContent);
            } catch {
                display.textContent = "Error";
            }
        } else {
            if (display.textContent === "0") {
                display.textContent = value;
            } else {
                display.textContent += value;
            }
        }
    });
});