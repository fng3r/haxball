
    let ProfileTabs = document.querySelectorAll('.profile-tabs');
    let firstElement = ProfileTabs[0];
    let secondElement = ProfileTabs[1];
    let historyNicknamesButton = document.querySelector('.nickname-inline');
    let nicknamesFlag = 1;

    firstElement.addEventListener("click", function(event){
        document.getElementById('profile-info-tab').style.color = '#000000';
        document.getElementById('profile-achievements-tab').style.color = '#007bff';
    });

    secondElement.addEventListener("click",function(event){
        document.getElementById('profile-achievements-tab').style.color = '#000000';
        document.getElementById('profile-info-tab').style.color = '#007bff';
    });

    /*historyNicknamesButton.addEventListener("mouseover", function(event){
        document.querySelector('.history-nicknames').style.opacity = '0.8';
    });

    historyNicknamesButton.addEventListener("mouseout", function(event){
        document.querySelector('.history-nicknames').style.opacity = '0';
    });*/

    historyNicknamesButton.addEventListener("click",function(event){
        if(nicknamesFlag){
            document.querySelector('.history-nicknames').style.opacity = '0.8';
            document.querySelector('.profile-treangle').style.transform = 'rotate(180deg)';
            nicknamesFlag = 0;
        } else {
            document.querySelector('.history-nicknames').style.opacity = '0';
            document.querySelector('.profile-treangle').style.transform = 'rotate(0deg)';
            nicknamesFlag = 1;
        }


    });

