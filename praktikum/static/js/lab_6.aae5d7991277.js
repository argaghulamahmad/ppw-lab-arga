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
    localStorage.setItem("themes", JSON.stringify(themes));

    mySelect = $('.my-select').select2();

    mySelect.select2({
        'data': JSON.parse(localStorage.getItem("themes")
        )
    });

    var arraysOfTheme = JSON.parse(localStorage.getItem("themes");
    var indigoTheme = arraysOfTheme[3];

    $('body').css(
        {
            "background-color": indigoTheme.bcgColor,
            "font-color": indigoTheme.fontColor,
        }
    );

    //Chat box
    var arrowDirection = "down";
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

    $('#msg-text-area').keyup(function (e) {
        if (e.which == 13) {
            $('#msg-text-area').val("");
        }
    });
    //END

    $('.apply-button').on('click', function () {  // sesuaikan class button
        // [TODO] ambil value dari elemen select .my-select

        // [TODO] cocokan ID theme yang dipilih dengan daftar theme yang ada

        // [TODO] ambil object theme yang dipilih

        // [TODO] aplikasikan perubahan ke seluruh elemen HTML yang perlu diubah warnanya

        // [TODO] simpan object theme tadi ke local storage selectedTheme
    })
});

// Calculator
var print = document.getElementById('print');
var erase = false;

var go = function (x) {
    if (x === 'ac') {
        print.value = "";
    } else if (x === 'eval') {
        print.value = Math.round(evil(print.value) * 10000) / 10000;
        erase = true;
    } else if (x === 'sin') {
        print.value = Math.sin(print.value);
        erase = true;
    } else if (x === 'tan') {
        print.value = Math.tan(print.value);
        erase = true;
    } else if (x === 'log') {
        print.value = Math.log(print.value);
        erase = true;
    } else {
        print.value += x;
    }
};

function evil(fn) {
    return new Function('return ' + fn)();
}

// END
