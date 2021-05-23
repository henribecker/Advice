$(document).ready(function(){
    $(".real, .real1").keyup(function(){
        var real = $(".real").val();
        var real1 = $(".real1").val();
        var total = parseFloat(real) * parseFloat(real1);
            $(".real1").val(total);
    });
});