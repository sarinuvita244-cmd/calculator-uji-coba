# TAHAP I
# ========================================================================================
# INISIALISASI & KONFIGURASI JENDELA UTAMA (GUI)
# ======= 1. Memanggil Pustaka Tkinter
import tkinter as tk

# ======= 2. Membuat Custom Variable Jendela Utama Aplikasi
layar_utama = tk.Tk()

# ======= 3. Mengatur Atribut Jendela Utama Aplikasi (Judul, Ukuran, dan Warna Background)
layar_utama.title("Kalkulator")
layar_utama.geometry("350x500")
layar_utama.configure(bg="#24244a") 
# ========================================================================================

# TAHAP 2
# ========================================================================================
# DEKLARASI VARIABEL PEMPROSES DATA
# Membuat Variable Papan Hitung sebagai memori penyimpan input string angka/operator
papan_hitung = "" 
# ========================================================================================

# TAHAP 3
# ========================================================================================
# PEMBUATAN FUNGSI LOGIKA (DUMMY / SEMENTARA)
# Fungsi dikosongkan dengan 'pass' agar tombol yang akan dibuat bisa merujuk ke fungsi ini 
# ======= 1. Fungsi dummy untuk tombol angka & operator
def tekan_tombol(num):
  global papan_hitung
  papan_hitung = papan_hitung + str(num)
  string_tampilan.set(papan_hitung)

# ======= 2. Fungsi dummy untuk tombol sama dengan (=)
def hitung():
  global papan_hitung
  try:
    # Mengganti karakter visual menjadi operator Python sebelum dihitung
    total = str(eval(papan_hitung.replace('x', '*').replace('÷', '/').replace(',', '.')))
    string_tampilan.set(total)
    papan_hitung = total
  except:
    string_tampilan.set("Error")
    papan_hitung = ""

# ======= 3. Fungsi dummy untuk tombol reset (C)
def hapus_semua():
  global papan_hitung
  papan_hitung = ""
  string_tampilan.set("")
# ========================================================================================

# TAHAP 4
# ========================================================================================
# PEMBUATAN LAYAR TAMPILAN PAPAN ANGKA DAN OPERATOR
# ======= 1. Membuat variabel Tkinter untuk sinkronisasi teks pada komponen Entry
string_tampilan = tk.StringVar()

# ======= 2. Membuat komponen widget Entry untuk layar kalkulator
layar = tk.Entry(
  layar_utama, 
  textvariable=string_tampilan, 
  font=("Helvetica", 36), 
  bd=0, 
  bg="#fafefa", 
  fg="black", 
  justify="right"
)
layar.pack(fill="both", ipadx=10, ipady=30, padx=10, pady=10)
# ========================================================================================

# TAHAP 5
# ========================================================================================
# PEMBUATAN DAN KONFIGURASI WIDGET FRAME TOMBOL
# ======= 1. Membuat Frame khusus sebagai tempat meletakkan susunan tombol
frame_tombol = tk.Frame(layar_utama, bg="#FFFFFF") 
frame_tombol.pack(fill="both", expand=True, padx=10, pady=10)

# ======= 2. Konfigurasi grid layout agar ukuran tombol bisa membesar/mengecil secara proporsional
for i in range(5):
  frame_tombol.rowconfigure(i, weight=1)
for i in range(4):
  frame_tombol.columnconfigure(i, weight=1)
# ========================================================================================

# TAHAP 6
# ========================================================================================
# DESAIN DATA & RENDERING TOMBOL (GRID SYSTEM)
# ======= 1. Pemetaan data konfigurasi tombol
# Sususnan data (Teks, Baris (row), Kolom (Column), Warna Bg, Warna Fg, Fungsi/Aksi)
tombol_config = [
  ('C', 0, 0, "#93cdd0", 'black', hapus_semua),
  ('+/-', 0, 1, '#93cdd0', 'black', lambda: tekan_tombol('-')),
  ('%', 0, 2, '#93cdd0', 'black', lambda: tekan_tombol('/100')),
  ('÷', 0, 3, "#39a7b6", 'white', lambda: tekan_tombol('÷')),
    
  ('1', 1, 0, "#4C8C9F", 'white', lambda: tekan_tombol('1')),
  ('2', 1, 1, "#4C8C9F", 'white', lambda: tekan_tombol('2')),
  ('3', 1, 2, '#4C8C9F', 'white', lambda: tekan_tombol('3')),
  ('x', 1, 3, '#39a7b6', 'white', lambda: tekan_tombol('x')),
    
  ('4', 2, 0, '#4C8C9F', 'white', lambda: tekan_tombol('4')),
  ('5', 2, 1, '#4C8C9F', 'white', lambda: tekan_tombol('5')),
  ('6', 2, 2, '#4C8C9F', 'white', lambda: tekan_tombol('6')),
  ('-', 2, 3, '#39a7b6', 'white', lambda: tekan_tombol('-')),
    
  ('7', 3, 0, '#4C8C9F', 'white', lambda: tekan_tombol('7')),
  ('8', 3, 1, '#4C8C9F', 'white', lambda: tekan_tombol('8')),
  ('9', 3, 2, '#4C8C9F', 'white', lambda: tekan_tombol('9')),
  ('+', 3, 3, '#39a7b6', 'white', lambda: tekan_tombol('+')),
    
  (',', 4, 2, '#4C8C9F', 'white', lambda: tekan_tombol(',')),
  ('=', 4, 3, '#39a7b6', 'white', hitung)
]

# ======= 2. Membuat dan menampilkan tombol berdasarkan data di atas
for teks, r, c, bg_color, fg_color, aksi in tombol_config:
  btn = tk.Button(
    frame_tombol, text=teks, font=("Helvetica", 18, "bold"),
    bg=bg_color, fg=fg_color, bd=0, relief="flat", command=aksi
  )
  btn.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)

  # Penanganan Khusus untuk tombol '0' agar berukuran lebih lebar (memakan 2 kolom grid)
  btn_nol = tk.Button(
  frame_tombol, text="0", font=("Helvetica", 18, "bold"),
  bg="#4C8C9F", fg="white", bd=0, relief="flat", command=lambda: tekan_tombol('0')
)
btn_nol.grid(row=4, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
# ========================================================================================

# LOOPING 
# Didahulukan setelah INISIALISASI & KONFIGURASI JENDELA UTAMA (GUI)
# Agar aplikasi GUI berjalan dan merespon interaksi pengguna
layar_utama.mainloop()