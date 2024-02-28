//function to display all of the sports that you can pick from
function sportsOffered(){
    var array = ["Basketball", "Soccer", "Volleyball","Hockey","Football"];
    var dropdown = document.getElementById("dropdown");
    for(let i=0;i<array.length;i++){
        var option = document.createElement("li");
        option.textContent = array[i];
        dropdown.appendChild(option);
    }
}

window.onload = sportsOffered;

function logout() {
    const request = new XMLHttpRequest();
    request.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 302) {
            console.log(this.responseText);
            
        }
    };
    request.open("POST", "/logout");
    request.send();
    location.reload(true);
}