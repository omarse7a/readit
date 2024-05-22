
const borrow_button = document.querySelector(".rent button");
let availability = document.querySelector('.rent small');

document.addEventListener("DOMContentLoaded", () => {
    if (availability.innerHTML != "Available") {
        borrow_button.classList.remove("button")
        borrow_button.classList.add("button-no-hover")
    }
})

//borrow button action

borrow_button.addEventListener("click", () => {
    if (availability.innerHTML = "Available") {
        availability.innerHTML = "Unavailable"
        availability.style.color = "#FF1919"
        borrow_button.classList.remove("button")
        borrow_button.classList.add("button-no-hover")
    }
})