const domain = 'http://127.0.0.1:8000/';
let username = '';
let password = '';
let credentials = null;

let list = document.getElementById('list');
let listLoader = new XMLHttpRequest();

let form = document.querySelector('#bbuser_form');
let userName = document.querySelector('#username');
let userEmail = document.querySelector('#email');
let userPassword1 = document.querySelector('#password1');
let userPassword2 = document.querySelector('#password2');
let rubricUpdater = new XMLHttpRequest();

let rubricDeleter = new XMLHttpRequest();

let login = document.querySelector('#login');
let usersUsername = document.querySelector('#users_username');
let usersPassword = document.querySelector('#users_password');
let usersButton = document.querySelector('#users_button');


function checkUser(username, password) {
    if (username == "" || password == "") {
        list.style = 'display: none;';
        form.style = 'display: none;';
        login.style = 'display: block;';
    } else {
        list.style = 'display: block;';
        form.style = 'display: block;';
        login.style = 'display: none;';
    }
}


usersButton.addEventListener('click', () => {
    username = usersUsername.value;
    password = usersPassword.value;
    credentials = window.btoa(username + ':' + password);
    checkUser(username, password);
    listLoad();
});

listLoader.addEventListener('readystatechange', () => {
    if (listLoader.readyState == 4) {
        if (listLoader.status == 200) {
            let data = JSON.parse(listLoader.responseText);
            let s = '<ul>', d;
            for (let i = 0; i < data.length; i++) {
                d = data[i];
                s += '<li> Username: ' + d.username + '<br> email:' + d.email + '<br> <a href="' + domain + 'auth/api/v1/users/' + d.username + '/" class="delete">Удалить</a></li><br>';
            }
            s += '</ul>';
            list.innerHTML = s;
            links = list.querySelectorAll('ul li a.delete');
            links.forEach((link) => {
                link.addEventListener('click', rubricDelete);
            });
        } else window.alert(listLoader.statusText);
    }
});

rubricUpdater.addEventListener('readystatechange', () => {
    if (rubricUpdater.readyState == 4) {
        if ((rubricUpdater.status == 200) || (rubricUpdater.status == 201)) {
            listLoad();
            userName.form.reset();
            userEmail.form.reset();
            userPassword1.form.reset();
            userPassword2.form.reset();
        } else
            window.alert(rubricUpdater.statusText);
    }
});

userName.form.addEventListener('submit', (evt) => {
    evt.preventDefault();

    url = 'auth/api/v1/users/';
    method = 'POST';

    let data = JSON.stringify({
        username: userName.value, 
        email: userEmail.value, 
        password1: userPassword1.value, 
        password2: userPassword2.value
    });

    rubricUpdater.open(method, domain + url, true);
    rubricUpdater.setRequestHeader('Content-Type', 'application/json');
    rubricUpdater.send(data);
});

rubricDeleter.addEventListener('readystatechange', () => {
    if (rubricDeleter.readyState == 4) {
        if (rubricDeleter.status = 204)
            listLoad();
        else
            window.alert(rubricDeleter.statusText);
    }
});        


function listLoad() {
    listLoader.open('GET', domain + 'auth/api/v1/users/', true);
    listLoader.setRequestHeader('Authorization', 'Basic ' + credentials);
    listLoader.send();
}


function rubricDelete(evt) {
    evt.preventDefault();
    rubricDeleter.open('DELETE', evt.target.href, true);
    rubricDeleter.send();
}    

checkUser(username, password);
