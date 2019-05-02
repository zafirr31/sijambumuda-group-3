$(document).ready(function() {
    $.ajax({
        url: "json/",
        type: "GET",
        dataType: "json",
        success: function(data) {
            var innerHTML = "";
            for (var i = 0; i < data.length; i++) {
                nomorBuku = "<p>Nomor Buku : " + data[i].nomor_buku + "</p>";
                judulBuku = "<p>Judul Buku : " + data[i].judul_buku + "</p>";
                namaPengarang = "<p>Pengarang : " + data[i].pengarang + "</p>";
                namaPenerbit = "<p>Penerbit : " + data[i].penerbit + "</p>";
                tanggalPinjam = "<p>Tanggal Peminjaman : " + data[i].tanggal_pinjam  + "</p>"; 
                innerHTML += "<li>" + nomorBuku + judulBuku + namaPengarang + namaPenerbit + tanggalPinjam + "</li>";
            }
            $("#history_buku").html(innerHTML);
        }
    })
});