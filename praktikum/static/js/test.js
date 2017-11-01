$(document).ready(function () {
    var button_8 = $('button:contains("8")');
    var button_4 = $('button:contains("4")');

    var button_add = $('button:contains("+")');
    var button_sub = $('button:contains("-")');
    var button_mul = $('button:contains("*")');
    var button_div = $('button:contains("/")');

    var button_clear = $('button:contains("AC")');
    var button_res = $('button:contains("=")');

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
});