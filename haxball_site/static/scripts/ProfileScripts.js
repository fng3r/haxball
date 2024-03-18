
    let ProfileTabs = document.querySelectorAll('.profile-tabs');
    let firstTab = ProfileTabs[0];
    let secondTab = ProfileTabs[1];

    firstTab.addEventListener("click", function(event){
        document.getElementById('profile-info-tab').style.color = '#000000';
        document.getElementById('profile-achievements-tab').style.color = '#007bff';
    });


    secondTab.addEventListener("click",function(event){
        document.getElementById('profile-achievements-tab').style.color = '#000000';
        document.getElementById('profile-info-tab').style.color = '#007bff';
    });


    let historyNicknamesButton = document.querySelector('.nickname-inline');
    let nicknamesFlag = 1;

    historyNicknamesButton.addEventListener("click",function(event){
        if(nicknamesFlag){
            document.querySelector('.history-nicknames').style.opacity = '0.8';
            document.querySelector('.profile-triangle').style.transform = 'rotate(180deg)';
            nicknamesFlag = 0;
        } else {
            document.querySelector('.history-nicknames').style.opacity = '0';
            document.querySelector('.profile-triangle').style.transform = 'rotate(0deg)';
            nicknamesFlag = 1;
        }


    });