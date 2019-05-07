$(document).ready(function() {
    $.ajax({
        url: "tampil/",
        type: "GET",
        dataType: "json",
        success: function(data) {
          var innerHTML = ''

          $("#history_buku").html(innerHTML);
        }
    })
});
