$(document).ready(function () {
    var button_8 = $('button:contains("8")');
    var button_4 = $('button:contains("4")');

    var button_add = $('button:contains("+")');
    var button_sub = $('button:contains("-")');
    var button_mul = $('button:contains("*")');
    var button_div = $('button:contains("/")');

    var button_clear = $('button:contains("AC")');
    var button_res = $('button:contains("=")');

    var button_sin = $('button:contains("sin")');
    var button_log = $('button:contains("log")');
    var button_tan = $('button:contains("tan")');

    var button_open_bracket = $('button:contains("(")');
    var button_close_bracket = $('button:contains(")")');

    QUnit.test("Addition Test", function (assert) {
        button_8.click();
        button_add.click();
        button_4.click();
        button_res.click();
        assert.equal($('#print').val(), 12, "8 + 4 must be 12");
        button_clear.click();
    });

    QUnit.test("Substraction Test", function (assert) {
        button_8.click();
        button_sub.click();
        button_4.click();
        button_res.click();
        assert.equal($('#print').val(), 4, "8 - 4 must be 4");
        button_clear.click();
    });

    QUnit.test("Multiply Test", function (assert) {
        button_8.click();
        button_mul.click();
        button_4.click();
        button_res.click();
        assert.equal($('#print').val(), 32, "8 * 4 must be 32");
        button_clear.click();
    });

    QUnit.test("Division Test", function (assert) {
        button_8.click();
        button_div.click();
        button_4.click();
        button_res.click();
        assert.equal($('#print').val(), 2, "8 / 4 must be 2");
        button_clear.click();
    });

    QUnit.test("Sin Test", function (assert) {
        button_sin.click();
        button_open_bracket.click();
        button_8.click();
        button_close_bracket.click();
        button_res.click();
        assert.equal($('#print').val(), 0.9893582466233818, "sin 8 must be 0.9893582466233818");
        button_clear.click();
    });

    QUnit.test("Tan Test", function (assert) {
        button_tan.click();
        button_open_bracket.click();
        button_8.click();
        button_close_bracket.click();
        button_res.click();
        assert.equal($('#print').val(), -6.799711455220379, "tan 8 must be -6.799711455220379");
        button_clear.click();
    });

    QUnit.test("Log Test", function (assert) {
        button_log.click();
        button_open_bracket.click();
        button_8.click();
        button_close_bracket.click();
        button_res.click();
        assert.equal($('#print').val(), 2.0794415416798357, "log 8 must be 2.0794415416798357");
        button_clear.click();
    });
});