themes = [{"id": 0, "text": "Red", "bcgColor": "#F44336", "fontColor": "#FAFAFA"},
    {"id": 0, "text": "Pink", "bcgColor": "#E91E63", "fontColor": "#FAFAFA"},
    {"id": 0, "text": "Purple", "bcgColor": "#9C27B0", "fontColor": "#FAFAFA"},
    {"id": 0, "text": "Indigo", "bcgColor": "#3F51B5", "fontColor": "#FAFAFA"},
    {"id": 0, "text": "Blue", "bcgColor": "#2196F3", "fontColor": "#212121"},
    {"id": 0, "text": "Teal", "bcgColor": "#009688", "fontColor": "#212121"},
    {"id": 0, "text": "Lime", "bcgColor": "#CDDC39", "fontColor": "#212121"},
    {"id": 0, "text": "Yellow", "bcgColor": "#FFEB3B", "fontColor": "#212121"},
    {"id": 0, "text": "Amber", "bcgColor": "#FFC107", "fontColor": "#212121"},
    {"id": 0, "text": "Orange", "bcgColor": "#FF5722", "fontColor": "#212121"},
    {"id": 0, "text": "Brown", "bcgColor": "#795548", "fontColor": "#FAFAFA"}];

$(document).ready(function () {
    localStorage.setItem("themes", JSON.stringify(themes));

    mySelect = $('.my-select').select2();

    mySelect.select2({
        'data': JSON.parse(localStorage.getItem("themes")
        )
    });

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

    $('#msg-text-area').keypress(function (e) {
        if (e.which === 13) {
            $('#msg-list').append("<li>" + document.getElementById("msg-text-area").value + " </li>");
            $('#msg-text-area').val('');
        }
    });
    //END

    $('.apply-button-class').on('click', function () {  // sesuaikan class button
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
