

const main_section = document.querySelector("#main-sec");


// Delete button action
const delete_button = document.querySelector(".alter .delete");
delete_button.addEventListener("click", () => {
    delete_button.innerHTML = "Deleted"
    delete_button.classList.remove("button")
    delete_button.classList.add("deleted")
})



// else if (!isAdmin) {
//     navList.innerHTML = `
//     <li><a href="available-books.html">View books</a></li>
//     <li><a href="User Section/borrowed-books.html">Dashboard</a></li>`;

//     main_section.innerHTML = userHtml;

//     const availability = document.querySelector('.rent small');
//     const borrow_button = document.querySelector(".rent button");
//     if (book.status == "Unavailable") {
//         availability.innerHTML = "Unavailable"
//         availability.style.color = "#FF1919"
//         borrow_button.classList.remove("button")
//         borrow_button.classList.add("button-no-hover")
//     }

//     //borrow button action
//     borrow_button.addEventListener("click", () => {
//         if (availability.innerHTML = "Available") {
//             availability.innerHTML = "Unavailable"
//             availability.style.color = "#FF1919"
//             borrow_button.classList.remove("button")
//             borrow_button.classList.add("button-no-hover")
//             book.status = "Unavailable"

//             //For Dashboard
//             var counter = localStorage.getItem('borrowedBooksCount');
//             counter = counter ? parseInt(counter) + 1 : 1;
//             localStorage.setItem('borrowedBooksCount', counter);

//             //Increment earnings
//             var earnings = localStorage.getItem('earningsThisMonth');
//             if (earnings !== null && !isNaN(earnings)) {
//                 earnings = parseInt(earnings) + 50;
//             } else {
//                 earnings = 50; // Set initial value if earnings is not valid
//             }
//             localStorage.setItem('earningsThisMonth', earnings);
//         }
//     })
// }