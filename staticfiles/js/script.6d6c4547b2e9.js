$(document).ready(function () {
    $("#0, #valor").keyup(function () {
        if ($("#0").val() === "") {
            $("#final").val($("#valor").val())

        } else {
            var real = $("#0").val();
            var real1 = $("#valor").val();
            var total = parseFloat(real) * parseFloat(real1);
            $("#final").val(total.toFixed(2));
        };
    });
});