$(document).ready(function () {
    let currentbg = $(".container-fluid").css("background-color");
    let currenttopborder = $(".data-border").css("border-top-color");
    let currentleftborder = $(".data-border").css("border-left-color");
    let currentrightborder = $(".data-border").css("border-right-color");
    let currentbottomborder = $(".data-border").css("border-bottom-color");
    let currentbutton = $(".btn-primary").css("background-color");

    let expectbg = "rgb(255, 108, 99)";
    let expecttopborder = "rgb(255, 108, 99)";
    let expectleftborder = "rgb(255, 108, 99)";
    let expectrightborder = "rgb(255, 108, 99)";
    let expectbottomborder = "rgb(255, 108, 99)";
    let expectbutton = "rgb(255, 108, 99)";

    // $(".loader")
    //     .delay(600)
    //     .fadeOut();

    $("#switch").mouseenter(function () {
        $(".container-fluid").css("background-color", expectbg);
        $(".data-border").css("border-top-color", expecttopborder);
        $(".data-border").css("border-left-color", expectleftborder);
        $(".data-border").css("border-right-color", expectrightborder);
        $(".data-border").css("border-bottom-color", expectbottomborder);
        $(".btn-primary").css("background-color", expectbutton);
    });

    $("#switch").mouseleave(function () {
        $(".container-fluid").css("background-color", currentbg);
        $(".data-border").css("border-top-color", currenttopborder);
        $(".data-border").css("border-left-color", currentleftborder);
        $(".data-border").css("border-right-color", currentrightborder);
        $(".data-border").css("border-bottom-color", currentbottomborder);
        $(".btn-primary").css("background-color", currentbutton);
    });

    $("#switch").click(function () {
        $(".container-fluid").css("background-color", expectbg);
        $(".data-border").css("border-top-color", expecttopborder);
        $(".data-border").css("border-left-color", expectleftborder);
        $(".data-border").css("border-right-color", expectrightborder);
        $(".data-border").css("border-bottom-color", expectbottomborder);
        $(".btn-primary").css("background-color", expectbutton);
        if (expectbg == "rgb(255, 108, 99)") {
            expectbg = "rgb(108, 99, 255)";
            expecttopborder = "rgb(108, 99, 255)";
            expectleftborder = "rgb(108, 99, 255)";
            expectrightborder = "rgb(108, 99, 255)";
            expectbottomborder = "rgb(108, 99, 255)";
            expectbutton = "rgb(108, 99, 255)";
            currentbg = "rgb(255, 108, 99)";
            currenttopborder = "rgb(255, 108, 99)";
            currentleftborder = "rgb(255, 108, 99)";
            currentrightborder = "rgb(255, 108, 99)";
            currentbottomborder ="rgb(255, 108, 99)";
            currentbutton = "rgb(255, 108, 99)";
        } else {
            currentbg = "rgb(108, 99, 255)";
            currenttopborder = "rgb(108, 99, 255)";
            currentleftborder = "rgb(108, 99, 255)";
            currentrightborder = "rgb(108, 99, 255)";
            currentbottomborder = "rgb(108, 99, 255)";
            currentbutton = "rgb(108, 99, 255)";
            expectbg = "rgb(255, 108, 99)";
            expecttopborder = "rgb(255, 108, 99)";
            expectleftborder = "rgb(255, 108, 99)";
            expectrightborder = "rgb(255, 108, 99)";
            expectbottomborder ="rgb(255, 108, 99)";
            expectbutton = "rgb(255, 108, 99)";
        }
    });
});
