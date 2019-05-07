show();
function show() {
  $.ajax({
      url: "tampil/",
      type: "GET",
      dataType: "json",
      success: function(data) {
        var innerHTML = '';
          for(var i = 0; i < data.length; i++){
            username = '<h2>' + data[i].Username + '</h2>';
            pesan = '<p>' + data[i].Pesan + '</p>';
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
