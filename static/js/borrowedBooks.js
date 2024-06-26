let booksArray = [];
let borrowedbooksArray = [];
var userID = document.getElementById("user-id").dataset.userId;
// console.log("User ID:", userID);

function fetchBooks() {
    return fetch('/borrowed-books/api/books/')
        .then(response => response.json())
        .then(data => {
            booksArray = data;
            return data; // Return the data to pass it to the next .then() in the chain
        })
        .catch(error => {
            console.error('Error fetching books:', error);
            throw error; // Throw the error to propagate it to the next .catch() in the chain
        });
}

function fetchBorrowedBooks() {
    return fetch('/borrowed-books/api/borrowed-books/')
        .then(response => response.json())
        .then(data => {
            // console.log('Fetched Data: ', data);
            borrowedbooksArray = data;
            // console.log('Borrowed BooksArray: ', borrowedbooksArray);
            return data; // Return the data to pass it to the next .then() in the chain
        })
        .catch(error => {
            console.error('Error fetching books:', error);
            throw error; // Throw the error to propagate it to the next .catch() in the chain
        });
}

document.addEventListener("DOMContentLoaded", function(){
    fetchBooks()
    .then(fetchBorrowedBooks)
    .then(handleBookData);
});

function handleBookData(){
    // console.log("Array: ", booksArray);
    function redirectToBookDetails(bookId) {
        // Store the book ID in local storage
        // localStorage.setItem('selectedBookIndex', bookId);
    
        // Perform actions with the book ID here
        // console.log("Book ID:", bookId);
    
        // const bookDetailsURL = `../books/book/${bookId}`;
        const bookDetailsURL = `../books/book/${bookId}`;
    
        // Redirect to the book details page
        window.location.href = bookDetailsURL;
    }
    
    function getRandomInt(min, max) {
        min = Math.ceil(min);
        max = Math.floor(max);
        return Math.floor(Math.random() * (max - min)) + min;
    }


    let bookSize = booksArray.length;
    let recommendedBook = booksArray[getRandomInt(0,bookSize)];
    // console.log(recommendedBook.id, recommendedBook.title, recommendedBook.cover);
    // console.log(recommendedBook.cover);
    const bookHTML = `<a id="img-link" href=""><img id="book4" src="http://127.0.0.1:8000/media/${recommendedBook.cover}" alt="Book Cover"></a>
                        <div class="book-details">
                            <p id="recommended-title"><a href="../books/book/${recommendedBook.id}">${recommendedBook.title}</a></p>
                            <p id="recommended-author">By: ${recommendedBook.author}</p>
                            <div id="recommended-ratings">
                                <p>${recommendedBook.reviews} reviews • ${recommendedBook.ratings} ratings </p>
                                <span class="fa fa-star checked"></span>
                                <span class="fa fa-star checked"></span>
                                <span class="fa fa-star checked"></span>
                                <span class="fa fa-star checked"></span>
                                <span class="fa fa-star unchecked"></span>
                            </div>
                            <p id="available">Status: <span id="stock">Available</span></p>
                            <p id="price">Renting Price: <span>${recommendedBook.price}</span></p>
                            <div id="actions">
                                <button id="viewDetails">View Book</button>
                            </div>
                        </div>`;
        document.querySelector("#recommended").innerHTML = bookHTML;
        
    
    let booksOfSpecificUser = borrowedbooksArray.filter(book => book.user_id == userID);
    console.log("Array: ", booksOfSpecificUser);

    // let book1ID = booksOfSpecificUser[0].book_id;
    // let book2ID = booksOfSpecificUser[1].book_id;
    // let book3ID = booksOfSpecificUser[2].book_id;
    // let book1 = booksArray.filter(book=>book.id == book1ID)[0];
    // let book2 = booksArray.filter(book=>book.id == book2ID)[0];
    // let book3 = booksArray.filter(book=>book.id == book3ID)[0];
    // console.log(book1);
    // console.log(book2);
    // console.log(book3);       
    function generateStars(rating) {
        let starsHTML = '';
        let fullStars = Math.floor(rating);
        let halfStars = rating % 1 >= 0.5 ? 1 : 0;
        let emptyStars = 5 - fullStars - halfStars;
    
        // Add full stars
        for (let i = 0; i < fullStars; i++) {
            starsHTML += '<span class="fa fa-star checked"></span>';
        }
        // Add half star if needed
        if (halfStars) {
            starsHTML += '<span class="fa fa-star-half-o checked"></span>';
        }
        // Add empty stars
        for (let i = 0; i < emptyStars; i++) {
            starsHTML += '<span class="fa fa-star"></span>';
        }
    
        return starsHTML;
    }


    let borrowedHTML = `<h2>Recent Borrows</h2>`
    if (booksOfSpecificUser.length === 0) {
        borrowedHTML += `<p>No borrowed books.</p>`;
    } 
    else {
        // Loop through the borrowed books and create HTML for each
        let ctr = 3;
        for (let i = booksOfSpecificUser.length - 1; i >= 0; i-- && ctr--) {
            let bookID = booksOfSpecificUser[i].book_id;
            let book = booksArray.filter(book => book.id == bookID)[0];
    
            borrowedHTML += `<div id="book${i + 1}">
                                <img src="http://127.0.0.1:8000/media/${book.cover}" alt="${book.title}">
                                <div class="book-description">
                                    <p class="name">${book.title}</p>
                                    <p class="author">By: ${book.author}</p>
                                    <div class="rating">
                                        <p>${book.reviews} reviews • ${book.ratings} ratings</p>
                                        ${generateStars(book.ratings)}
                                    </div>
                                </div>
                            </div>`;
        }
    }

    

    // borrowedHTML = `
    //                 <div id="book1">
    //                     <img src="http://127.0.0.1:8000/media/${book1.cover}" alt="${book1.title}">
    //                     <div class="book-description">
    //                         <p class="name">${book1.title}</p>
    //                         <p class="author">By: ${book1.author}</p>
    //                         <div class="rating">
    //                             <p>84 reviews • 448 ratings</p>
    //                             <span class="fa fa-star checked"></span>
    //                             <span class="fa fa-star checked"></span>
    //                             <span class="fa fa-star checked"></span>
    //                             <span class="fa fa-star-half-o"></span>
    //                             <span class="fa fa-star"></span>
    //                         </div>
    //                     </div>
    //                     </div>
    //                     <div id="book2">
    //                     <img src="http://127.0.0.1:8000/media/${book2.cover}" alt="${book2.title}">
    //                     <div class="book-description">
    //                         <p class="name">${book2.title}</p>
    //                         <p class="author">By: ${book2.author}</p>
    //                         <div class="rating">
    //                             <p>40 reviews • 308 ratings</p>
    //                             <span class="fa fa-star checked"></span>
    //                             <span class="fa fa-star checked"></span>
    //                             <span class="fa fa-star checked"></span>
    //                             <span class="fa fa-star"></span>
    //                             <span class="fa fa-star"></span>
    //                         </div>
    //                     </div>
    //                     </div>
    //                     <div id="book3">
    //                     <img src="http://127.0.0.1:8000/media/${book3.cover}" alt="${book3.title}">
    //                     <div class="book-description">
    //                         <p class="name">${book3.title}</p>
    //                         <p class="author">By: ${book3.author}</p>
    //                         <div class="rating">
    //                             <p>16 reviews • 124 ratings </p>
    //                             <span class="fa fa-star checked"></span>
    //                             <span class="fa fa-star checked"></span>
    //                             <span class="fa fa-star-half-o"></span>
    //                             <span class="fa fa-star"></span>
    //                             <span class="fa fa-star"></span>
    //                         </div>
    //                     </div>  
    //                 </div>`;
    document.querySelector(".recent-borrows").innerHTML = borrowedHTML;
    
    const RbookDetailsURL = `../books/book/${recommendedBook.id}`;
    document.querySelector("#img-link").href = RbookDetailsURL
    
    document.querySelector("#viewDetails").addEventListener(`click`, function () {
        redirectToBookDetails(recommendedBook.id);
    });
    
    var stockSpan = document.getElementById("stock");
    var rentButton = document.getElementById("rentButton");

    
    
    // console.log(recommendedBook.title);
    // console.log(book1.title);
    // console.log(book2.title);
    // console.log(book3.title);
    // console.log(recommendedBook.title == book1[0].title || recommendedBook.title == book2[0].title || recommendedBook.title == book3[0].title);
    
    
}
