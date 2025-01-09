import datetime

def parse_nik(nik):
    """
    Parse NIK (Nomor Induk Kependudukan) Indonesia.
    
    Parameters:
    nik (str): NIK 16 digit.
    
    Returns:
    dict: Informasi tentang pemilik NIK.
    """
    
    if len(nik) != 16 or not nik.isdigit():
        return "NIK harus terdiri dari 16 angka"
    
    provinsi_kabupaten_kecamatan = nik[:6]
    tanggal_lahir = nik[6:12]
    jenis_kelamin_code = int(nik[12:14])
    nomor_urut = nik[14:]
    
    try:
        tanggal = datetime.datetime.strptime(tanggal_lahir, "%y%m%d")
        tanggal_lahir_baru = tanggal.strftime("%d-%m-%Y")
    except ValueError:
        return "Tanggal lahir tidak valid"
    
    jenis_kelamin = "Pria" if jenis_kelamin_code <= 5 else "Wanita"
    
    return {
        "Provinsi, Kab/Kota, Kecamatan": provinsi_kabupaten_kecamatan,
        "Tanggal Lahir": tanggal_lahir_baru,
        "Jenis Kelamin": jenis_kelamin,
        "Nomor Urut": nomor_urut
    }

def main():
    print("===================================")
    print(" Simple Osint NIK By. Thonxyzz404 ")
    print("===================================")
    
    nik_input = input("Masukkan NIK: ")
    hasil = parse_nik(nik_input)
    
    if isinstance(hasil, dict):
        for key, value in hasil.items():
            print(f"{key}: {value}")
    else:
        print(hasil)

if __name__ == "__main__":
    main()