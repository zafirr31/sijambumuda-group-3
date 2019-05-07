$(document).ready(function() {
    $.ajax({
        url: "json/",
        type: "GET",
        dataType: "json",
        success: function(data) {
            var innerHTML = "<p>Jumlah buku yang dipinjam : " + data.length + "</p>";
            for (var i = 0; i < data.length; i++) {
                innerHTML += "<li>" + data[i].nomor_buku + " " + data[i].judul_buku + " " + data[i].pengarang + " " +
                data[i].penerbit + " " + data[i].tanggal_pinjam + "</li>";
            }
            $("#history_buku").html(innerHTML);
        }
    })
});