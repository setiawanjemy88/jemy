data_pribadi = {
    "nama_lengkap": "Jemy Setiawan",
    "tanggal_lahir": "1980-10-22",
    "email": "setiawanjemy88@gmail.com",
    "nomor_telepon": "+6281617222831",
    "alamat_lengkap": "Perum GCC 2 Blok H24/40",
    "profesi": "Marketing Manager",
    "pendidikan": [
        {
            "jenjang": "SMK",
            "jurusan": "Accounting",
            "institusi": "SMKN 2 BEKASI",
            "tahun_lulus": 1998
        }
    ],
    "profil_online": {
        "google": "https://plus.google.com/personal-info",
        "github": "https://github.com/setiawanjemy88/jemy",
        "facebook": "https://facebook.com/jemysetiawan88",
        "telegram": "https://t.me/jemysetiawan"
    }
}
# Contoh akses data
print("Nama:", data_pribadi["nama_lengkap"])
print("google:",data_pribadi["profil_online"]["google"])
print("GitHub:", data_pribadi["profil_online"]["github"])
print("facebook:",data_pribadi["profil_online"]["facebook"])
print("telegram:",data_pribadi["profil_online"]["telegram"])