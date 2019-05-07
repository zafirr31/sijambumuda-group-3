var csrftoken = $('input[name="csrfmiddlewaretoken"]').val();
var username = $("#id_username").val()

$(document).ready(function () {
    $("#id_username").addClass("form-control");
    $("#id_email").addClass("form-control");
    $("#id_password").addClass("form-control");
    $("#id_re_password").addClass("form-control");
});

$("#id_username").change(function () {
    username = $("#id_username").val()
    $.ajaxSetup({
        headers: {
            "X-CSRFToken": csrftoken,
        }
    });
    $.ajax({
        url: '/check-username/',
        type: 'POST',
        data: { 'username': username },
        success: function (data) {
            if (data == "True") {
                $("#usernameSuccess").remove();
                $("#id_username").removeClass("has-error");
                $("#id_username").addClass("has-success").after(`<small id=\"usernameSuccess\" class=\"text-success\">Username available</small>`);;
                $("#usernameError").remove();
            }
            else {
                $("#usernameError").remove();
                $("#id_username").removeClass("has-success")
                $("#id_username").addClass("has-error").after(`<small id=\"usernameError\" class=\"text-danger\">Username already taken</small>`);
                $("#usernameSuccess").remove();
            }
        }
    });
});

$("#id_email").change(function () {
    email = $("#id_email").val()
    $.ajaxSetup({
        headers: {
            "X-CSRFToken": csrftoken,
        }
    });
    $.ajax({
        url: '/check-email/',
        type: 'POST',
        data: { 'email': email },
        success: function (data) {
            if (data == "True") {
                $("#id_email").removeClass("has-error");
                $("#emailError").remove();

            }
            else {
                $("#emailError").remove();
                $("#id_email").addClass("has-error").after(`<small id=\"emailError\" class=\"text-danger\">Email already taken</small>`);
            }
        }
    });
});

$("#id_password").change(function () {
    checkPass();
});
$("#id_re_password").change(function () {
    checkPass();
});

function checkPass() {
    password = $("#id_password").val()
    re_password = $("#id_re_password").val()
    $.ajaxSetup({
        headers: {
            "X-CSRFToken": csrftoken,
        }
    });
    $.ajax({
        url: '/check-password/',
        type: 'POST',
        data: { 'password': password, 're_password': re_password },
        success: function (data) {
            if (data == "True") {
                $("#id_re_password").removeClass("has-error");
                $("#passwordError").remove();
            }
            else {
                $("#passwordError").remove();
                $("#id_re_password").addClass("has-error").after(`<small id=\"passwordError\" class=\"text-danger\">Passwords do not match!</small>`);
            }
        }
    });
}