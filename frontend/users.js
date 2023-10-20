const domain = 'http://127.0.0.1:8000/';

let list = document.getElementById('list');
let listLoader = new XMLHttpRequest();

listLoader.addEventListener('readystatechange', () => {
    if (listLoader.readyState == 4) {
        if (listLoader.status == 200) {
            let data = JSON.parse(listLoader.responseText);
            let s = '<ul>', d;
            for (let i = 0; i < data.length; i++) {
                d = data[i];
                s += '<li> Username: ' + d.username + '<br> email:' + d.email + '</li><br>';
            }
            s += '</ul>';
            list.innerHTML = s;
        } else window.alert(listLoader.statusText);
    }
});

function listLoad() {
    listLoader.open('GET', domain + 'auth/api/v1/users/', true);
    listLoader.send();
}

listLoad();