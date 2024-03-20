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
//function to start the chat box at the bottom
document.addEventListener('DOMContentLoaded', function() {
    var scrollContainer = document.querySelector('.chat-room');
    
    // Scroll to the bottom on page load
    scrollContainer.scrollTop = scrollContainer.scrollHeight;
  
    // Additional code for dynamic content or user interaction
  });
  
window.onload = sportsOffered;

function updateChatRoom(messages) {
    const request = new XMLHttpRequest();
    request.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200){
            document.addEventListener('DOMContentLoaded', function() {
                var scrollContainer = document.querySelector('.chat-room');
                
                // Scroll to the bottom on page load
                scrollContainer.scrollTop = scrollContainer.scrollHeight;
              
                // Additional code for dynamic content or user interaction
              });
            const message = JSON.parse(this.response);
            messages = message['messages'];
            var chatRoom = document.getElementById('chat-room');
            chatRoom.innerHTML = ''; // Clear existing messages

            // Append the new messages to the chat room
            messages.forEach(function(message) {
                var paragraph = document.createElement('p');
                paragraph.className = 'user-message';
                paragraph.textContent = message[1] + ' | Team ' + message[2] + ': ' + message[3];
                chatRoom.appendChild(paragraph);
            });
        }
    }
    request.open("GET","/chat-update");
    request.send();
}

function pollChat() {
   updateChatRoom(); 
}

setInterval(pollChat, 2000);
pollChat();