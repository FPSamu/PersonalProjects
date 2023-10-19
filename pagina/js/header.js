let mainLoc = window.pageYOffset;
window.onscroll = function(){
    let locScroll = window.pageYOffset;
    if(mainLoc>=550){
        document.getElementById('navbar').style.top='0';
    }
    else{
        document.getElementById('navbar').style.top='-12vh';
    }
    mainLoc = locScroll;
}