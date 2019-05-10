show();
function show() {
  $.ajax({
      url: "tampil/",
      type: "GET",
      dataType: "json",
      success: function(data) {
        var innerHTML = '';
          for(var i = 0; i < data.length; i++){
            var encodedStr_pesan = data[i].Pesan.replace(/[\u00A0-\u9999<>\&]/gim, function(i) {
              return '&#'+i.charCodeAt(0)+';';
            });
             var encodedStr_username = data[i].Username.replace(/[\u00A0-\u9999<>\&]/gim, function(i) {
              return '&#'+i.charCodeAt(0)+';';
            });
            username = '<h2>' + encodedStr_username + '</h2>';
            pesan = '<p>' + encodedStr_pesan + '</p>';
            tanggal_pesan = '<h4>' + data[i].Tanggal_Pesan + '</h4>';

            innerHTML += username + pesan + tanggal_pesan;
          }

        $("#tampilkanTestimoni").html(innerHTML);
      }
  })
}

function buat() {
  $.ajax({
      url : "buat/",
      type: "POST",
      data : {
          pesan:$("#id_Pesan").val(),
          csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(),
      },
      success : function() {
          $("#id_Pesan").val("");
          alert("success")
      }
  });
}

