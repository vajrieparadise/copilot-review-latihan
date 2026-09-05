"""
Kalkulator diskon sederhana untuk toko online.
Mengimplementasikan fungsi-fungsi untuk menghitung
diskon, total keranjang, dan penerapan kupon dengan
validasi dan error handling yang proper.
"""

from typing import List, Tuple
import os


def hitung_harga_akhir(harga: float, persen_diskon: float) -> float:
    """
    Menghitung harga akhir setelah diskon.
    
    Args:
        harga: Harga awal (harus positif)
        persen_diskon: Persentase diskon (0-100)
        
    Returns:
        Harga setelah diskon diterapkan
        
    Raises:
        ValueError: Jika harga negatif atau persen_diskon di luar range 0-100
    """
    # PERBAIKAN BUG 1: Validasi input
    if harga < 0:
        raise ValueError("Harga tidak boleh negatif")
    if not (0 <= persen_diskon <= 100):
        raise ValueError("Persen diskon harus antara 0 dan 100")
    
    diskon = harga * (persen_diskon / 100)
    harga_akhir = harga - diskon
    return harga_akhir


def hitung_total_keranjang(daftar_harga: List[float]) -> Tuple[float, float]:
    """
    Menghitung total dan rata-rata harga dari daftar harga.
    
    Args:
        daftar_harga: List berisi harga-harga item
        
    Returns:
        Tuple (total, rata_rata)
        
    Raises:
        ValueError: Jika daftar kosong
    """
    # PERBAIKAN BUG 2: Validasi daftar kosong
    if not daftar_harga or len(daftar_harga) == 0:
        raise ValueError("Daftar harga tidak boleh kosong")
    
    total = sum(daftar_harga)
    rata_rata = total / len(daftar_harga)
    return total, rata_rata


def terapkan_kupon(harga: float, kode_kupon: str, admin_password: str = None) -> float:
    """
    Menerapkan kupon admin jika kode kupon benar.
    
    Args:
        harga: Harga item
        kode_kupon: Kode kupon yang diberikan customer
        admin_password: Password admin (default dari environment variable)
        
    Returns:
        Harga setelah kupon diterapkan (0 jika admin, atau harga asli)
    """
    # PERBAIKAN BUG 3: Load secret dari environment variable, bukan hardcoded
    if admin_password is None:
        admin_password = os.getenv("ADMIN_PASSWORD", "")
    
    if kode_kupon == admin_password and admin_password:
        return 0
    return harga


if __name__ == "__main__":
    # Test kode
    print("Test hitung_harga_akhir:")
    print(f"Harga 100000 dengan diskon 20%: {hitung_harga_akhir(100000, 20)}")
    
    print("\nTest hitung_total_keranjang:")
    harga_list = [10000, 20000, 15000]
    total, rata_rata = hitung_total_keranjang(harga_list)
    print(f"Total: {total}, Rata-rata: {rata_rata}")
    
    print("\nTest terapkan_kupon:")
    print(f"Kupon tidak valid: {terapkan_kupon(100000, 'INVALID')}")
