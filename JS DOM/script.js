function changeColor() {
    document.querySelectorAll('p')[0].style.color= "green";
    document.querySelectorAll('p')[1].style.color= "yellow";
    document.querySelectorAll('p')[2].style.color= "red";

};

function changeBackgroundColor(mau){
    document.querySelector('.container').style.backgroundColor=mau;
};


function changeFontSize(x) {
    document.querySelector('.container').style.fontSize=x
};

function copyContent(paragraph1, paragraph2){
    document.getElementById("paragraph1").innerText = document.getElementById("paragraph2").innerText
};

function increaseFontSize(paragraph) {
    var el = document.getElementById('paragraph');
    var style = window.getComputedStyle(el, null).getPropertyValue('font-size');
    var fontSize = parseFloat(style); 
    if (fontSize < 30){
        el.style.fontSize = (fontSize + 1) + 'px';
    }
       
};

function decreaseFontSize(paragraph) {
    var el = document.getElementById('paragraph');
    var style = window.getComputedStyle(el, null).getPropertyValue('font-size');
    var fontSize = parseFloat(style); 
    if (fontSize > 10){
        el.style.fontSize = (fontSize - 1) + 'px';
    }
}