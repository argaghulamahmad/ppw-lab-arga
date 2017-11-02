themes = [{"id": 0, "text": "Red", "bcgColor": "#F44336", "fontColor": "#FAFAFA"},
    {"id": 1, "text": "Pink", "bcgColor": "#E91E63", "fontColor": "#FAFAFA"},
    {"id": 2, "text": "Purple", "bcgColor": "#9C27B0", "fontColor": "#FAFAFA"},
    {"id": 3, "text": "Indigo", "bcgColor": "#3F51B5", "fontColor": "#FAFAFA"},
    {"id": 4, "text": "Blue", "bcgColor": "#2196F3", "fontColor": "#212121"},
    {"id": 5, "text": "Teal", "bcgColor": "#009688", "fontColor": "#212121"},
    {"id": 6, "text": "Lime", "bcgColor": "#CDDC39", "fontColor": "#212121"},
    {"id": 7, "text": "Yellow", "bcgColor": "#FFEB3B", "fontColor": "#212121"},
    {"id": 8, "text": "Amber", "bcgColor": "#FFC107", "fontColor": "#212121"},
    {"id": 9, "text": "Orange", "bcgColor": "#FF5722", "fontColor": "#212121"},
    {"id": 10, "text": "Brown", "bcgColor": "#795548", "fontColor": "#FAFAFA"}];

$(document).ready(function () {
    //menambahkan json yang berisi array themes
    localStorage.setItem("themes", JSON.stringify(themes));

    //inisiasi variabel mySelect
    mySelect = $('.my-select').select2();

    //populate data pada mySelect
    mySelect.select2({
        'data': JSON.parse(localStorage.getItem("themes")
        )
    });

    //ambil dan parsing data 'themes' dari localStorage
    var arraysOfTheme = JSON.parse(localStorage.getItem("themes"));
    var indigoTheme = arraysOfTheme[3]; //defaultTheme
    var defaultTheme = indigoTheme;
    var selectedTheme = defaultTheme;

    //kalo sebelumnya localStorage udah nyimpen selectedTheme pake yang lama
    if (localStorage.getItem("selectedTheme") !== null) {
        var chacedTheme = JSON.parse(localStorage.getItem("selectedTheme"));
    }

    //pake yang chacedTheme
    selectedTheme = chacedTheme;

    //ganti css sesuai theme yang dipilih (selectedTheme)
    $('body').css(
        {
            "background-color": selectedTheme.bcgColor,
            "font-color": selectedTheme.fontColor
        }
    );

    //Chat box
    var arrowDirection = "down";
    //animasi biar bisa ke atas dan ke bawah chatbox nya
    $('#expand-arrow-button').click(function () {
        $('.chat-body').toggle();
        if (arrowDirection === "down") {
            $('#expand-arrow-button').attr({src: "https://maxcdn.icons8.com/windows10/PNG/16/Arrows/angle_up-16.png"});
            arrowDirection = "up";
        }
        else {
            $('#expand-arrow-button').attr({src: "https://maxcdn.icons8.com/windows10/PNG/16/Arrows/angle_down-16.png"});
            arrowDirection = "down";
        }
    });

    var cls = "msg-receive";
    //nambahin chat text setelah di tekan 'enter'
    $('#msg-text-area').keypress(function (e) {
        if (e.which == 13) {
            var msg = $('#msg-text-area').val();
            var old = $('.msg-insert').html();
            if (msg.length === 0) {
                alert("Message kosong");
            }
            else {
                cls = (cls == "msg-send") ? "msg-receive" : "msg-send"
                $('.msg-insert').html(old + '<p class=' + cls + '>' + msg + '</p>')
                $('#msg-text-area').val("");

            }
        }
    });

    //reset ulang text-area chat setelah enter
    $('#msg-text-area').keyup(function (e) {
        if (e.which == 13) {
            $('#msg-text-area').val("");
        }
    });
    //END

    //terapkan tema apabila tombol 'apply' ditekan
    $('.apply-button').on('click', function () {
        //id theme yang dipilih
        var idThemeChoosed = mySelect.val();

        //bila cocok
        if (idThemeChoosed < arraysOfTheme.length) {
            selectedTheme = arraysOfTheme[idThemeChoosed];
        }

        //ganti css sesuai theme yang dipilih
        $('body').css(
            {
                "background-color": selectedTheme.bcgColor,
                "font-color": selectedTheme.fontColor
            }
        );

        //simpan 'selectedTheme' di localStorage
        localStorage.setItem("selectedTheme", JSON.stringify(selectedTheme));
    })
});

// Calculator
var print = document.getElementById('print');
var erase = false;

var go = function (x) {
    if (x === 'ac') {
        print.value = "";
    } else if (x === 'eval') {
        if (print.value.includes('sin') || print.value.includes('tan') || print.value.includes('log')) {
            var idxOpen = print.value.indexOf('(');
            var idxClose = print.value.indexOf(')');
            if (print.value.includes('sin')) {
                print.value = Math.sin(print.value.substring(idxOpen+1, idxClose));
            } else if (print.value.includes('tan')) {
                print.value = Math.tan(print.value.substring(idxOpen+1, idxClose));
            } else if (print.value.includes('log')) {
                print.value = Math.log(print.value.substring(idxOpen+1, idxClose));
            }
            erase = true;
        } else {
            print.value = Math.round(evil(print.value) * 10000) / 10000;
            erase = true;
        }

    } else {
        if (erase) {
            print.value = "";
            erase = false;
        }
        print.value += x;
    }
};

function evil(fn) {
    return new Function('return ' + fn)();
}
// END