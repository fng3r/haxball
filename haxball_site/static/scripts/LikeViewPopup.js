document.querySelectorAll('.popup-tab').forEach(popupTab => {
    let popupTabLike = popupTab.querySelector('.popup-tab-like');
    let popupTabDisLike = popupTab.querySelector('.popup-tab-dislike');

    popupTabLike.addEventListener("click", function(event) {
        popupTabLike.style.boxShadow = '0px 0px 5px #00FF00';
        popupTabDisLike.style.boxShadow = '0px 0px 3px #fbd784';
        $('.vote-dislike').fadeOut(0);
        $('.vote-like').fadeIn(0);
    });

    popupTabDisLike.addEventListener("click", function(event){
        popupTabDisLike.style.boxShadow = '0px 0px 5px #bd2130';
        popupTabLike.style.boxShadow = '0px 0px 3px #fbd784';
        $('.vote-like').fadeOut(0);
        $('.vote-dislike').fadeIn(0);
    });
});

