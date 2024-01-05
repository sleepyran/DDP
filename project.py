import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = tk.Tk()

def hitung_estimasi():
    berat = float(entry_berat.get())
    tarifkg = float(entry_tarif.get())
    tujuan = combo_tujuan.get()

    tarifkota = {
        'Jakarta': 1.9,
        'Bogor': 2.7,
        'Tangerang': 4.2,
        'Bekasi': 3.8,
       
    }
    if tujuan in tarifkota:
        tarifkg *= tarifkota[tujuan]
        estimasi_harga = berat * tarifkg
        hasil.config(text=f'Estimasi Harga ke {tujuan}: Rp.{estimasi_harga:.2f}')
    else:
        hasil.config(text='Kota tujuan tidak valid.')

root.title("Estimasi Harga Ekspedisi")

berat = tk.Label(root, text="Berat Paket (kg):")
berat.pack()

entry_berat = tk.Entry(root)
entry_berat.pack()

tarif = tk.Label(root, text="Tarif per Kg (Rp.):")
tarif.pack()

entry_tarif = tk.Entry(root)
entry_tarif.pack()

tujuan = tk.Label(root, text="Kota Tujuan:")
tujuan.pack()

tujuan_options = ['Jakarta', 'Bogor', 'Tangerang', 'Bekasi']
combo_tujuan = tk.StringVar()
combo_tujuan.set(tujuan_options[0])
dropdown_tujuan = ttk.OptionMenu(root, combo_tujuan, *tujuan_options, bootstyle="light")
dropdown_tujuan.pack()

button_hitung = ttk.Button(root, text="Hitung Estimasi", command=hitung_estimasi, bootstyle="success")
button_hitung.pack()

hasil = tk.Label(root, text="Estimasi Harga:")
hasil.pack()

root.mainloop()