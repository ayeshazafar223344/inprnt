let menu = document.querySelector('#menu-btn');
let navbar = document.querySelector('.header .navbar');
menu.onclick = () => {
    menu.classList.toggle('fas-times');
    navbar.classList.toggle('active');
}
window.onscroll = () => {
    menu.classList.remove('fas-times');
    navbar.classList.remove('active');
}
let shop = document.querySelector('#h1');
let submenu = document.querySelector('.shop .sub-menu-1 ul');
shop.onclick = () => {
    shop.classList.toggle('fas-times');
    submenu.classList.toggle('active');
}
window.onscroll = () => {
    shop.classList.remove('fas-times');
    submenu.classList.remove('active');
}
var counter=1;
setInterval(function(){
    document.getElementById('radio' + counter).checked=true;
    counter++;
    if(counter > 4){
        counter=1;
    }
},5000)