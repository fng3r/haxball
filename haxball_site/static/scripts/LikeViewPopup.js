
    let tabPopupLike = document.querySelector('.popup-tab-like');
    let tabPopupDisLike = document.querySelector('.popup-tab-dislike');

    tabPopupLike.addEventListener("click", function(event){
        document.querySelector('.popup-tab-like').style.boxShadow = '0px 0px 5px #00FF00';
        document.querySelector('.popup-tab-dislike').style.boxShadow = '0px 0px 3px #fbd784';
        $('.vote-dislike').fadeOut(0);
        $('.vote-like').fadeIn(0);
    });


    tabPopupDisLike.addEventListener("click", function(event){
        document.querySelector('.popup-tab-dislike').style.boxShadow = '0px 0px 5px #bd2130';
        document.querySelector('.popup-tab-like').style.boxShadow = '0px 0px 3px #fbd784';
        $('.vote-like').fadeOut(0);
        $('.vote-dislike').fadeIn(0);

    });

