#SISTEM PENGGAJIAN PT KITA JAYA
class Karyawan:
    # Class Attribute (milik bersama seluruh object)
    perusahaan = "PT KITA JAYA"
    jumlah_karyawan = 0

    def __init__(self, nama: str, id_karyawan: str, gaji_pokok: float):
        # Encapsulation: menggunakan atribut private (__)
        self.__nama = nama
        self.__id_karyawan = id_karyawan
        self.__gaji_pokok = 0
        self.gaji_pokok = gaji_pokok  # Memanggil setter untuk validasi awal
        Karyawan.jumlah_karyawan += 1

    # --- Property & Setter (Encapsulation) ---
    @property
    def nama(self):
        return self.__nama

    @property
    def id_karyawan(self):
        return self.__id_karyawan

    @property
    def gaji_pokok(self):
        return self.__gaji_pokok

    @gaji_pokok.setter
    def gaji_pokok(self, nilai: float):
        if nilai < 0:
            raise ValueError("Gaji pokok tidak boleh bernilai negatif!")
        self.__gaji_pokok = nilai

    # --- Instance Method ---
    def hitung_gaji_total(self) -> float:
        return self.__gaji_pokok

    def tampilkan_slip(self):
        print(f"Perusahaan   : {Karyawan.perusahaan}")
        print(f"ID / Nama    : {self.__id_karyawan} - {self.__nama}")
        print(f"Gaji Pokok   : {self.format_rupiah(self.__gaji_pokok)}")
        print(f"Total Gaji   : {self.format_rupiah(self.hitung_gaji_total())}")
        print("-" * 40)

    # --- Class Method ---
    @classmethod
    def ubah_nama_perusahaan(cls, nama_baru: str):
        cls.perusahaan = nama_baru

    @classmethod
    def total_karyawan(cls) -> int:
        return cls.jumlah_karyawan

    # --- Static Method ---
    @staticmethod
    def format_rupiah(nominal: float) -> str:
        return f"Rp {nominal:,.0f}".replace(",", ".")


# Class ke-2: Inheritance (Turunan dari class Karyawan)
class KaryawanTetap(Karyawan):
    def __init__(self, nama: str, id_karyawan: str, gaji_pokok: float, tunjangan: float):
        super().__init__(nama, id_karyawan, gaji_pokok)
        self.__tunjangan = tunjangan

    @property
    def tunjangan(self):
        return self.__tunjangan

    @tunjangan.setter
    def tunjangan(self, nilai: float):
        if nilai < 0:
            raise ValueError("Tunjangan tidak boleh negatif!")
        self.__tunjangan = nilai

    # Overriding method hitung_gaji_total
    def hitung_gaji_total(self) -> float:
        return self.gaji_pokok + self.__tunjangan


# Class ke-3: Inheritance (Turunan dari class Karyawan)
class KaryawanKontrak(Karyawan):
    def __init__(self, nama: str, id_karyawan: str, gaji_pokok: float, jam_lembur: int, upah_lembur: float):
        super().__init__(nama, id_karyawan, gaji_pokok)
        self.__jam_lembur = jam_lembur
        self.__upah_lembur = upah_lembur

    # Overriding method hitung_gaji_total
    def hitung_gaji_total(self) -> float:
        bonus_lembur = self.__jam_lembur * self.__upah_lembur
        return self.gaji_pokok + bonus_lembur


# ==========================================
# Pembuatan Object & Pengujian Program
# ==========================================
if __name__ == "__main__":
    # Menggunakan Class Method
    Karyawan.ubah_nama_perusahaan("PT KITA JAYA")

    # Membuat Object dari masing-masing class
    karyawan_1 = KaryawanTetap("MUHAMMAD ANRI", "EMP-001", 6000000, 1500000)
    karyawan_2 = KaryawanKontrak("RABIA CANTIK", "EMP-002", 4500000, 10, 50000)

    # Menggunakan Setter untuk mengubah gaji pokok
    karyawan_1.gaji_pokok = 6500000

    # Menampilkan hasil slip gaji
    print("=== SLIP GAJI KARYAWAN ===")
    karyawan_1.tampilkan_slip()
    karyawan_2.tampilkan_slip()

    # Menggunakan Class Method & Static Method secara langsung
    print(f"Total Karyawan Terdaftar : {Karyawan.total_karyawan()} orang")
    print(f"Contoh Format Rupiah     : {Karyawan.format_rupiah(12500000)}")
