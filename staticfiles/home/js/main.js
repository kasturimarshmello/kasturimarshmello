
var csrf = document.getElementById('csrf').value

function login(){
    var username = document.getElementById('username_log').value
    var password = document.getElementById('password_log').value

    if(username == '' || password == ''){
        alert('You must enter username and password')
    }

    var data = {
        'username' : username,
        'password' : password
    }

    fetch('/api/login/' , {
        method : 'POST',
        headers : {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : csrf
        },
        'body' : JSON.stringify(data)
    }).then(result => result.json())
    .then(response => {
        if(response.status == 200){
            window.location.href = '/'
        }
        else{
            $('#log-error-msg').addClass('show')
            $('#log-error-msg').removeClass('noshow')
            $('#log-error-msg').text(response.message)
        }
        console.log(response)
    })
}




function register(){
    var username = document.getElementById('username_reg').value
    var email = document.getElementById('email_reg').value
    var password = document.getElementById('password_reg').value

    if(username == '' || email == '' || password == ''){
        alert('You must enter username and password')
    }

    var data = {
        'username' : username,
        'email' : email,
        'password' : password
    }

    fetch('/api/register/' , {
        method : 'POST',
        headers : {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : csrf
        },
        'body' : JSON.stringify(data)
    }).then(result => result.json())
    .then(response => {
        $('#reg-error-msg').addClass('show')
        $('#reg-error-msg').removeClass('noshow')
        $('#reg-error-msg').text(response.message)
    })
}