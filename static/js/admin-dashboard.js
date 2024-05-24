//closing and opening sidebar
const menuBtn = document.querySelector('.bx-menu');
const sideBar = document.querySelector('.sidebar');
const mainElement = document.querySelector('main');
const readitLogo = document.querySelector('.readit');

function coSideBar() {
  if(! (sideBar.classList.contains('close'))){ // to close
    sideBar.classList.add('close');
    mainElement.classList.add('expanded');
    readitLogo.innerHTML = "<i class='bx bxs-book'></i>";

  }
  else { // to open
    sideBar.classList.remove('close');
    mainElement.classList.remove('expanded');
    readitLogo.innerHTML = "<span>readIt</span>";

  }
}
menuBtn.addEventListener("click" , coSideBar);

// ------------------------------------------------------------------------------
//swap the active calss over the sidebar elements
const sideBarItems = document.querySelectorAll('.side-menu li');

function moveActive() {
  //Remove active class from all the items 
  sideBarItems.forEach(item => {
    item.classList.remove('active');
  });
  // then add active class to the hovered one
  this.classList.add('active');
}

sideBarItems.forEach(item => {
  item.addEventListener("mouseover", moveActive);
});
// ------------------------------------------------------------------------------
//For Dark Mode

const bodyElement = document.querySelector('body');
const darkLight = document.querySelector('.dark-mode');
const darkIcon = document.querySelector(".bx.bx-sun");




function darkMode (){
  document.body.classList.toggle("dark");
  darkIcon.classList.toggle("bx-moon");
  darkIcon.classList.toggle("bx-sun");
  if(bodyElement.classList.contains('dark'))
    localStorage.setItem("mode" , "dark");
  else
    localStorage.setItem("mode" , "");
}

darkLight.addEventListener("click" ,darkMode);

function handleDark() {
  var mode = localStorage.getItem("mode");
  bodyElement.classList.add(mode);
}

addEventListener('DOMContentLoaded', handleDark);

//----------------------------------------------------------------------------


  