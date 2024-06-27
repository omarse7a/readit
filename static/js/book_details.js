let borrow_button = document.querySelector(".rent button");
let availability = document.querySelector('.rent small');

document.addEventListener("DOMContentLoaded", () => {
    if (availability.innerHTML == "Unavailable") {
        borrow_button.disabled = true;
        borrow_button.classList.remove("button")
        borrow_button.classList.add("button-no-hover")
    }
})

// //borrow button action
// borrow_button.addEventListener("click", () => {
//     if (availability.innerHTML = "Available") {
//         borrow_button.disabled = true;
//         borrow_button.classList.remove("button")
//         borrow_button.classList.add("button-no-hover")
//     }
// })