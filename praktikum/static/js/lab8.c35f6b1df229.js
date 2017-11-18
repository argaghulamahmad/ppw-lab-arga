// FB initiation function
// Menginisiasi dan meload terhadap js sdk secara async
window.fbAsyncInit = () => {
    FB.init({
        appId: '498316760531733',
        cookie: true,
        xfbml: true,
        version: 'v2.11'
    });

    // fungsi yang melakukan cek status login (getLoginStatus)
    loginStatus = getLoginStatus();
    console.log("Login Status : ");
    console.log(loginStatus);

    // panggil fungsi render dengan parameter loginStatus agar ketika web dibuka,
    // dan ternyata sudah login, maka secara otomatis akan ditampilkan view sudah login
    console.log("--- Render ---");
    render(loginStatus);
};

// Call init facebook. default dari facebook
(function (d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) {
        return;
    }
    js = d.createElement(s);
    js.id = id;
    js.src = "https://connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));

// Fungsi Render, menerima parameter loginFlag yang menentukan apakah harus
// merender atau membuat tampilan html untuk yang sudah login atau belum
const render = loginFlag => {
    console.log("Render function: ");
    console.log(loginFlag);
    if (loginFlag) {
        console.log("LoginFlag: " + loginFlag);
        // Jika yang akan dirender adalah tampilan sudah login
        // Panggil Method getUserData yang anda implementasi dengan fungsi callback
        // yang menerima object user sebagai parameter.

        // Object user ini merupakan object hasil response dari pemanggilan API Facebook.
        console.log("--- Get User Data ---");
        getUserData(user => {
            console.log("--- Display User Data ---");
            // Render tampilan profil, form input post, tombol post status, dan tombol logout
            $('#lab8').html(
                '<div class="profile">' +
                '<img class="cover" src="' + user.cover.source + '" alt="cover" />' +
                '<img class="picture" src="' + user.picture.data.url + '" alt="profpic" />' +
                '<div class="data">' +
                '<h1>' + user.name + '</h1>' +
                '<h2>' + user.about + '</h2>' +
                '<h3>' + user.email + ' - ' + user.gender + '</h3>' +
                '</div>' +
                '</div>' +
                '<input id="postInput" type="text" class="post" placeholder="Ketik Status Anda" />' +
                '<button class="postStatus" onclick="postStatus()">Post ke Facebook</button>' +
                '<button class="logout" onclick="facebookLogout()">Logout</button>'
            );

            // Setelah merender tampilan diatas, dapatkan data home feed dari akun yang login
            // dengan memanggil method getUserFeed yang kalian implementasi sendiri.
            // Method itu harus menerima parameter berupa fungsi callback, dimana fungsi callback
            // ini akan menerima parameter object feed yang merupakan response dari pemanggilan API Facebook
            console.log("--- Get User Feed ---");
            getUserFeed(feed => {
                console.log("--- Display User Feed ---");
                feed.data.map(value => {
                    // Render feed, kustomisasi sesuai kebutuhan.
                    if (value.message && value.story) {
                        $('#lab8').append(
                            '<div class="feed">' +
                            '<h1>' + value.message + '</h1>' +
                            '<h2>' + value.story + '</h2>' +
                            '</div>'
                        );
                    } else if (value.message) {
                        $('#lab8').append(
                            '<div class="feed">' +
                            '<h1>' + value.message + '</h1>' +
                            '</div>'
                        );
                    } else if (value.story) {
                        $('#lab8').append(
                            '<div class="feed">' +
                            '<h2>' + value.story + '</h2>' +
                            '</div>'
                        );
                    }
                });
            });
        });
    } else {
        // Tampilan ketika belum login
        console.log("LoginFlag: " + loginFlag);
        $('#lab8').html('<button class="login" onclick="facebookLogin()">Login</button>');
    }
};

const facebookLogin = () => {
    // Pastikan method memiliki callback yang akan memanggil fungsi render tampilan sudah login
    // ketika login sukses, serta juga fungsi ini memiliki segala permission yang dibutuhkan
    // pada scope yang ada.

    FB.login(function (response) {
        console.log("Facebook Login :");
        console.log(response);
        status = response['status'];
        console.log(response['status']);
        if (status === 'connected') {
            render(true);
        } else {
            render(false);
        }
    }, {scope: 'public_profile,user_posts,publish_actions,email,user_about_me'})
};

const facebookLogout = (call) => {
    // Pastikan method memiliki callback yang akan memanggil fungsi render tampilan belum login
    // ketika logout sukses.

    console.log("Facebook Logout : ");
    FB.getLoginStatus(function (response) {
        if (response.status === 'connected') {
            FB.logout();
            call(false);
            console.log("Logout Success!")
        }
    });
};

const getUserData = (call) => {
    // Pastikan method ini menerima parameter berupa fungsi callback, lalu merequest data User dari akun
    // yang sedang login dengan semua fields yang dibutuhkan di method render, dan memanggil fungsi callback
    // tersebut setelah selesai melakukan request dan meneruskan response yang didapat ke fungsi callback
    // tersebut

    console.log("--- Get User Data ---");
    FB.getLoginStatus(function (response) {
        if (response.status === 'connected') {
            FB.api('/me?fields=id,name,email,cover,picture,gender,about', 'GET', function (response) {
                console.log("User Data :");
                console.log(response);
                call(response);
            });
        }
    });
};

const getUserFeed = () => {
    // Pastikan method ini menerima parameter berupa fungsi callback, lalu merequest data Home Feed dari akun
    // yang sedang login dengan semua fields yang dibutuhkan di method render, dan memanggil fungsi callback
    // tersebut setelah selesai melakukan request dan meneruskan response yang didapat ke fungsi callback
    // tersebut
};

const postFeed = () => {
    // Pastikan method ini menerima parameter berupa string message dan melakukan Request POST ke Feed
    // Melalui API Facebook dengan message yang diterima dari parameter.
};

const postStatus = () => {
    const message = $('#postInput').val();
    postFeed(message);
};

// fungsi untuk mengecek apakah user sudah login
const getLoginStatus = (response) => {
    console.log("--- Get Login Status ---");
    FB.getLoginStatus(function (response) {
        if (response.status === 'connected') {
            // the user is logged in and has authenticated your
            // app, and response.authResponse supplies
            // the user's ID, a valid access token, a signed
            // request, and the time the access token
            // and signed request each expire
            let uid = response.authResponse.userID;
            let accessToken = response.authResponse.accessToken;
            console.log("Login Success!");
            console.log("Login Status :");
            console.log("uid: " + uid);
            console.log("access token: " + accessToken);
            return true;
        } else if (response.status === 'not_authorized') {
            // the user is logged in to Facebook,
            // but has not authenticated your app
            console.log("User Not Authorized!");
            return false;
        } else {
            // the user isn't logged in to Facebook.
            console.log("User Not Logged!");
            return false;
        }
    });
};