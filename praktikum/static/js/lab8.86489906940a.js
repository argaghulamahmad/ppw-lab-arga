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
        getUserData(user => {
            console.log("--- Display User Data ---");
            // Render tampilan profil, form input post, tombol post status, dan tombol logout
            $('#login-jumbotron').remove();

            // tampilkan data yang didapatkan pada template
            $('#user-name').html(user.name);
            $('#user-description').html(user.about);
            $('#cover-image').attr('src', user.cover.source);
            $('#profile-image').attr('src', user.picture.data.url);
            $('#login-button').remove();
            $('.fb-profile').show();
            $('#lab8-main-area').html('');
            $('#lab8-main-area').append(
                '<div id="form-update-status-area">' +
                '<div class="form-group" id="form-update-status">' +
                '<label for="status">' + 'Update Status' + '</label>' +
                '<textarea id="postInput" class="form-control" rows="5" id="comment"></textarea>' +
                '</div>' +
                '<button id="postStatus" class="btn btn-success" onclick="postStatus()">Post ke Facebook</button>' +
                '</div>'
            );

            // memilih ikon gender sesuai data yang didapatkan
            var gender_info = "";
            if (user.gender === 'male') {
                gender_info = '<li class="list-group-item"><i class="fa fa-mars" aria-hidden="true"></i>' + " Male" + '</li>';
            } else if (user.gender === 'female') {
                gender_info = '<li class="list-group-item"><i class="fa fa-venus" aria-hidden="true"></i>' + " Female" + user.gender + '</li>'
            }

            $('#menu-navbar').html("");
            $('#menu-navbar').append(
                '<li>' + '<a href="#" class="card-link">' + '<button class="btn btn-primary render" onclick="render(true)">Re Render</button>' + '</a>' +'</li>' +
                '<li>' + '<a href="#" class="card-link">' + '<button class="btn btn-danger logout" onclick="facebookLogout(render())">Logout</button>' + '</a>' + '</li>'
            );

            $('#lab8-side-area').html("");
            $('#lab8-side-area').append(
                '<div id="bio-card" class="card">' +
                '<div class="card-block">' +
                '<h4 class="card-title center" id="sidebar-title"> Biography </h4>' +
                '</div>' +
                '<ul class="list-group list-group-flush center">' +
                '<li class="list-group-item"><i class="fa fa-envelope" aria-hidden="true"></i>' + " " + user.email + '</li>' +
                gender_info +
                '</ul>' +
                '<div class="card-block">' +
                '</div>' +
                '</div>'
            );

            // Setelah merender tampilan diatas, dapatkan data home feed dari akun yang login
            // dengan memanggil method getUserFeed yang kalian implementasi sendiri.
            // Method itu harus menerima parameter berupa fungsi callback, dimana fungsi callback
            // ini akan menerima parameter object feed yang merupakan response dari pemanggilan API Facebook
            getUserFeed(feed => {
                console.log("--- Display User Feed ---");
                feed.data.map(value => {
                    // Render feed, kustomisasi sesuai kebutuhan.
                    if (value.message && value.story) {
                        $('#lab8-main-area').append(
                            '<div value="" class="panel panel-primary">' +
                            '<div class="panel-heading">Message & Story</div>' +
                            '<div class="panel-body">' + value.message + '</div>' +
                            '<div class="panel-body info">' + value.story + '</div>' +
                            '<div class="panel-footer">' + '<button onclick="deletePost(\'' + value.id + '\')" class="btn btn-danger"">Delete Post</button>' + '</div>' +
                            '</div>'
                        );
                    } else if (value.message) {
                        $('#lab8-main-area').append(
                            '<div value="" class="panel panel-primary">' +
                            '<div class="panel-heading">Message</div>' +
                            '<div class="panel-body">' + value.message + '</div>' +
                            '<div class="panel-footer">' + '<button onclick="deletePost(\'' + value.id + '\')" class="btn btn-danger">Delete Post</button>' + '</div>' +
                            '</div>'
                        );
                    } else if (value.story) {
                        $('#lab8-main-area').append(
                            '<div value="" class="panel panel-primary">' +
                            '<div class="panel-heading">Message & Story</div>' +
                            '<div class="panel-body">' + value.story + '</div>' +
                            '<div class="panel-footer">' + '<button onclick="deletePost(\'' + value.id + '\')" class="btn btn-danger")">Delete Post</button>' + '</div>' +
                            '</div>'
                        );
                    }
                });
            });
        });
    } else {
        // Tampilan ketika belum login
        console.log("LoginFlag: " + loginFlag);
        $('#lab8-main-area').html("");
        $('#lab8-side-area').html("");
        $('#lab8').html("");
        $('#menu-navbar').html("");
        $('#lab8').append(
            '<div id="login-jumbotron" class="jumbotron">' +
            '<h1 class="display-3">Hello, Guest!</h1>' +
            '<p class="lead">This is Arga Ghulam Ahmad\'s APP PPW-LAB-8.</p>' +
            '<hr class="my-4">' +
            '<p class="lead">' +
            '<button id="login-button" class="login btn btn-success" onclick="facebookLogin()">Login with your Facebook accout.</button>' +
            '</p>' +
            '</div>'
        );
        $('.fb-profile').hide();
    }
};

// Fungsi yang menangani proses login
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
    }, {scope: 'public_profile,user_posts,publish_actions,email,user_about_me,user_birthday,user_hometown,user_education_history'})
};

// Fungsi yang menangani proses logout
const facebookLogout = () => {
    // Method memiliki callback yang akan memanggil fungsi render tampilan belum login
    // ketika logout sukses.

    console.log("Facebook Logout : ");
    FB.getLoginStatus(function (response) {
        if (response.status === 'connected') {
            FB.logout();
            console.log("Logout Success!")
        }
    });
};

// Apakah yang dimaksud dengan fungsi callback?
// fungsi callback adalah fungsi yang dijalankan didalam fungsi lain ketika fungsi tersebut selesai di eksekusi

// Fungsi yang menangani proses mendapatkan data pengguna yang sudah login
const getUserData = (call) => {
    // Pastikan method ini menerima parameter berupa fungsi callback, lalu merequest data User dari akun
    // yang sedang login dengan semua fields yang dibutuhkan di method render, dan memanggil fungsi callback
    // tersebut setelah selesai melakukan request dan meneruskan response yang didapat ke fungsi callback
    // tersebut

    console.log("--- Get User Data ---");
    FB.getLoginStatus(function (response) {
        if (response.status === 'connected') {
            FB.api('/me?fields=id,name,email,cover.type(large),picture.type(large),gender,about', 'GET', function (response) {
                console.log("User Data :");
                console.log(response);
                call(response);
            });
        }
    });
};

// Fungsi yang menangani proses mendapatkan post pengguna
const getUserFeed = (call) => {
    // Pastikan method ini menerima parameter berupa fungsi callback, lalu merequest data Home Feed dari akun
    // yang sedang login dengan semua fields yang dibutuhkan di method render, dan memanggil fungsi callback
    // tersebut setelah selesai melakukan request dan meneruskan response yang didapat ke fungsi callback
    // tersebut

    console.log("--- Get User Feed ---");
    FB.api(
        "/me/feed",
        function (response) {
            if (response && !response.error) {
                console.log(response);
                call(response);
            }
        }
    );
};

// Fungsi yang menangani proses memposting status
const postFeed = (msg) => {
    // Pastikan method ini menerima parameter berupa string message dan melakukan Request POST ke Feed
    // Melalui API Facebook dengan message yang diterima dari parameter.
    console.log("Post Feed: " + msg);
    FB.api('/me/feed', 'post', {message: msg}, function (response) {
        if (!response || response.error) {
            alert('Error occured');
        } else {
            alert('Posted! - Post ID: ' + response.id);
            render(true);
        }
    });
};

// method helper post status
const postStatus = () => {
    const message = $('#postInput').val();
    console.log("Post Status: " + message);
    postFeed(message);
    render(true);
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

// Fungsi yang menangani proses delete post berdasarkan id post tersebut
const deletePost = (id) => {
    console.log("Delete Post: ");
    console.log(id);
    FB.api('/' + id, 'DELETE', function (response) {
        console.log(response);
        if (response.success) {
            render(true);
            console.log(id + "Post Deleted!");
        } else {
            alert("Tidak dapat menghapus post yang tidak di post melalui aplikasi ini!");
            console.log("Delete Failed!")
        }

    });
};

