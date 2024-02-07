
    console.log("страница загружена");
    let buttonProfileInfo = document.querySelector('.profile-tabs');
    let buttonProfileAchievements = document.querySelectorAll('.profile-tabs');
    let secondElement = buttonProfileAchievements[1];
    console.log(secondElement);

    buttonProfileInfo.addEventListener("click", function(event){
        document.getElementById('profile-info-tab').style.color = 'black';
        document.getElementById('profile-achievements-tab').style.color = '#007bff';
    });


    secondElement.addEventListener("click",function(event){
        document.getElementById('profile-achievements-tab').style.color = 'black';
        document.getElementById('profile-info-tab').style.color = '#007bff';
    });
