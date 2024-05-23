function redirectToBookDetails(bookId) {
    // Store the book ID in local storage
    localStorage.setItem('selectedBookIndex', bookId);

    // Perform actions with the book ID here
    console.log("Book ID:", bookId);

    const bookDetailsURL = `../book_details.html?index=${bookId}`;

    // Redirect to the book details page
    window.location.href = bookDetailsURL;
}
let booksArray = JSON.parse(localStorage.getItem("Books"));

function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min)) + min;
}

let recommendedBook = booksArray[getRandomInt(0, 11)];

const bookHTML = `<a id="img-link" href=""><img id="book4" src="${recommendedBook.cover}" alt="Book Cover"></a>
                    <div class="book-details">
                        <p id="recommended-title"><a href="">${recommendedBook.title}</a></p>
                        <p id="recommended-author">By: ${recommendedBook.author}</p>
                        <div id="recommended-ratings">
                            <p>219 reviews • 504 ratings </p>
                            <span class="fa fa-star checked"></span>
                            <span class="fa fa-star checked"></span>
                            <span class="fa fa-star checked"></span>
                            <span class="fa fa-star checked"></span>
                            <span class="fa fa-star unchecked"></span>
                        </div>
                        <p id="available">Status: <span id="stock">Available</span></p>
                        <p id="price">Renting Price: <span>29.99 EGP</span></p>
                        <div id="actions">
                            <button id="rentButton">Rent</button>
                            <button id="viewDetails">View Book</button>
                        </div>
                    </div>`;
document.querySelector("#recommended").innerHTML = bookHTML;


let book1 = booksArray[getRandomInt(0, 5)];
if (book1.id = "2") {
    book1 = booksArray[getRandomInt(0, 5)];
}
// while(book1 === recommendedBook){
//     book1 = booksArray[getRandomInt(3, 7)];
// }
let book2 = booksArray[getRandomInt(5, 9)];
// while(book2 === recommendedBook || book2 === book2){
//     book2 = booksArray[getRandomInt(0, 11)];
// }
let book3 = booksArray[getRandomInt(9, 11)];
// while(book3 === recommendedBook || book3 === book2 || book3 === book2){
//     book4 = booksArray[getRandomInt(0, 11)];
// }


borrowedHTML = `<h2>Recent Borrows</h2>
                <div id="book1">
                    <img src="${book1.cover}" alt="${book1.title}">
                    <div class="book-description">
                        <p class="name">${book1.title}</p>
                        <p class="author">By: ${book1.author}</p>
                        <div class="rating">
                            <p>84 reviews • 448 ratings</p>
                            <span class="fa fa-star checked"></span>
                            <span class="fa fa-star checked"></span>
                            <span class="fa fa-star checked"></span>
                            <span class="fa fa-star-half-o"></span>
                            <span class="fa fa-star"></span>
                        </div>
                    </div>
                    </div>
                    <div id="book2">
                    <img src="${book2.cover}" alt="${book2.title}">
                    <div class="book-description">
                        <p class="name">${book2.title}</p>
                        <p class="author">By: ${book2.author}</p>
                        <div class="rating">
                            <p>40 reviews • 308 ratings</p>
                            <span class="fa fa-star checked"></span>
                            <span class="fa fa-star checked"></span>
                            <span class="fa fa-star checked"></span>
                            <span class="fa fa-star"></span>
                            <span class="fa fa-star"></span>
                        </div>
                    </div>
                    </div>
                    <div id="book3">
                    <img src="${book3.cover}" alt="${book3.title}">
                    <div class="book-description">
                        <p class="name">${book3.title}</p>
                        <p class="author">By: ${book3.author}</p>
                        <div class="rating">
                            <p>16 reviews • 124 ratings </p>
                            <span class="fa fa-star checked"></span>
                            <span class="fa fa-star checked"></span>
                            <span class="fa fa-star-half-o"></span>
                            <span class="fa fa-star"></span>
                            <span class="fa fa-star"></span>
                        </div>
                    </div>  
                </div>`;
document.querySelector(".recent-borrows").innerHTML = borrowedHTML;

const RbookDetailsURL = `../book_details.html?index=${recommendedBook.id}`;
document.querySelector("#img-link").href = RbookDetailsURL

document.querySelector("#viewDetails").addEventListener(`click`, function () {
    redirectToBookDetails(recommendedBook.id);
});

var stockSpan = document.getElementById("stock");
var rentButton = document.getElementById("rentButton");

rentButton.addEventListener("click", function () {
    if (!rentButton.disabled) {
        // Change the text content and style of the span
        stockSpan.textContent = "Unavailable";
        stockSpan.style.color = "red";

        // Disable the button
        rentButton.disabled = true;
        // Grey out the button (optional)
        rentButton.style.opacity = "0.5";
    }
});