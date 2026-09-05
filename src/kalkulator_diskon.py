"""
Kalkulator diskon sederhana untuk toko online.
SENGAJA mengandung BUG NYATA untuk menguji
apakah Copilot Code Review benar-benar
menganalisis LOGIKA, bukan cuma gaya penulisan.
"""


def hitung_harga_akhir(harga, persen_diskon):
    # BUG 1: tidak ada validasi jika persen_diskon
    # negatif atau lebih dari 100 -- bisa
    # menghasilkan harga akhir negatif atau
    # lebih mahal dari harga asli
    diskon = harga * (persen_diskon / 100)
    harga_akhir = harga - diskon
    return harga_akhir


def hitung_total_keranjang(daftar_harga):
    # BUG 2: pembagian dengan panjang list yang
    # BISA SAJA nol (keranjang kosong), akan
    # menyebabkan ZeroDivisionError saat runtime
    total = sum(daftar_harga)
    rata_rata = total / len(daftar_harga)
    return total, rata_rata


def terapkan_kupon(harga, kode_kupon):
    # BUG 3: password/kode rahasia DITULIS
    # LANGSUNG di kode (hardcoded secret) --
    # praktik keamanan yang buruk
    KODE_RAHASIA_ADMIN = "ADMIN12345"
    if kode_kupon == KODE_RAHASIA_ADMIN:
        return 0
    return harga


if __name__ == "__main__":
    print(hitung_harga_akhir(100000, 20))
