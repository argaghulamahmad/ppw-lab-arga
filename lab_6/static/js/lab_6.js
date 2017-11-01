$(document).ready(function () {
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
});

// Calculator
var print = document.getElementById('print');
var erase = false;

var go = function(x) {
  if (x === 'ac') {
      print.value = "";
  } else if (x === 'eval') {
      print.value = Math.round(evil(print.value) * 10000) / 10000;
      erase = true;
  } else {
    print.value += x;
  }
};

function evil(fn) {
  return new Function('return ' + fn)();
}
// END
