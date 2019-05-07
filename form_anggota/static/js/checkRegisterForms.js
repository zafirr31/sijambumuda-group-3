

var csrftoken = $ ('input[name="csrfmiddlewaretoken"]').val();
var username = $("#id_username").val()

$(document).ready(function()	{
	$("#id_username").addClass("form-control");
	$("#id_email").addClass("form-control");
	$("#id_password").addClass("form-control");
	$("#id_re_password").addClass("form-control");
});

$("#id_username").change(function()	{
	username = $("#id_username").val()
	$.ajaxSetup({
        headers: { 
        	"X-CSRFToken": csrftoken,
        }
    });
    $.ajax({
    		url: '/check-username/',
    		type: 'POST',
    		data: {'username': username},
    		success: function (data) {
    			if(data == "True")	{
    				$("#id_username").removeClass("is-invalid");
    				$("#usernameError").remove();
    				
    			}
    			else	{
    				$("#id_username").addClass("is-invalid").after(`<small id=\"usernameError\" class=\"text-danger\">Username already taken</small>`);
    			}
    		}
    	});
});

$("#id_email").change(function()	{
	email = $("#id_email").val()
	$.ajaxSetup({
        headers: { 
        	"X-CSRFToken": csrftoken,
        }
    });
    $.ajax({
    		url: '/check-email/',
    		type: 'POST',
    		data: {'email': email},
    		success: function (data) {
    			console.log(data)
    			if(data == "True")	{
    				$("#id_email").removeClass("is-invalid");
    				$("#emailError").remove();
    				
    			}
    			else	{
    				$("#id_email").addClass("is-invalid").after(`<small id=\"emailError\" class=\"text-danger\">Email already taken</small>`);
    			}
    		}
    	});
});