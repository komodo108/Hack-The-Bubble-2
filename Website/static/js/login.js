// JavaScript Document

$(document).ready(function(){
                  $("#submit").bind("click", validate);
                  });

//Validates a username and password
function validate() {
    var booking = getCookie("booking");
    
    var jsondata;
    if(booking) {
        jsondata = { "username": $("#username").val(), "password": $("#password").val(), "booking": 0 };
    } else {
        jsondata = { "username": $("#username").val(), "password": $("#password").val(), "booking": 1 };    
    }

            $.ajax({type: "POST",
                    url: "/api/get/session",
                    dataType: "json",
                    contentType: "application/json",
                    data: JSON.stringify(jsondata),
                    success: function(result) {
                        //Store session to check for later and redirect
                        if(!booking){
                            setCookie("booking", JSON.parse(result).booking, 7);
                        }
                        location.assign(location.protocol + "/loungers");
                    },
                    error: function() {
                        $("#submit").prop('disabled', false);
                        $("#submit").html("Sign In");
                        add_alert("Bad", "Username or password was incorrect!");
                    }});
}

//Sets a cookie on the document name to value for days daya
function setCookie(name,value,days) {
    var expires = "";
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toUTCString();
    } document.cookie = name + "=" + (value || "")  + expires + "; path=/";
}

//Get's the cookie with name name
function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
    } return null;
}