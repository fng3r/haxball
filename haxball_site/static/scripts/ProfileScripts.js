
    let ProfileTabs = document.querySelectorAll('.profile-tabs');
    let firstElement = ProfileTabs[0];
    let secondElement = ProfileTabs[1];

    firstElement.addEventListener("click", function(event){
        document.getElementById('profile-info-tab').style.color = '#000000';
        document.getElementById('profile-achievements-tab').style.color = '#007bff';
    });


    secondElement.addEventListener("click",function(event){
        document.getElementById('profile-achievements-tab').style.color = '#000000';
        document.getElementById('profile-info-tab').style.color = '#007bff';
    });
