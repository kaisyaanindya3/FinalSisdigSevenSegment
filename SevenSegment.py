# ===============================================================
# Kaisya Anindya Callista Putri Kusyanto                        =
# D121231008-Tugas Final Sistem Digital-Seven Segment Display   =
# ===============================================================

import tkinter as tk
from tkinter import ttk

# Fungsi untuk mengonversi angka ke representasi seven segment display
def convert_to_segments(number):
    segments = {
        0: ['A', 'B', 'C', 'D', 'E', 'F'],
        1: ['B', 'C'],
        2: ['A', 'B', 'D', 'E', 'G'],
        3: ['A', 'B', 'C', 'D', 'G'],
        4: ['B', 'C', 'F', 'G'],
        5: ['A', 'C', 'D', 'F', 'G'],
        6: ['A', 'C', 'D', 'E', 'F', 'G'],
        7: ['A', 'B', 'C'],
        8: ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
        9: ['A', 'B', 'C', 'D', 'F', 'G'],
    }
    return segments.get(number, [])

# Fungsi untuk menampilkan seven segment display berdasarkan input pengguna
def show_segments(input_number):
    # Hapus segmen sebelumnya
    for segment in segments:
        canvas.itemconfig(segments[segment], fill='grey')
    
    # Menemtukan segment yang aktif
    active_segments = convert_to_segments(input_number)

    # Aktifkan segmen yang sesuai input
    for segment in active_segments:
        canvas.itemconfig(segments[segment], fill='red')
    
    # Tampilkan binary input
    binary_values = format(input_number, '04b')    #format biner panjang 4 
    binary_input.set(binary_values)

    #Tampilkan decodder output
    decoder_values = ['1' if segment in active_segments else '0' for segment in ['A', 'B', 'C', 'D', 'E', 'F', 'G']] 
    decoder_output.set(' '.join(decoder_values))

    # Treeview
    binary_values = [int(b) for b in binary_values]
    table.delete(*table.get_children())
    table.insert('', 'end', values= (binary_values[0], binary_values[1], binary_values[2], binary_values[3], *decoder_values))

# Fungsi panggilan saat tombol di klik
def on_button_click():
    try:
        input_number = int(entry.get())
        if 0 <= input_number <= 9:
            show_segments(input_number)
    except ValueError:
        binary_input.set("")
        decoder_output.set("")

# Buat jendela utama 
window = tk.Tk()
window.title("Kaisya Anindya-D121231008-Seven Segment Display")

# Buat canvas untuk menampilkan seven segment display
canvas = tk.Canvas(window, width=700, height=500, background='black')
canvas.pack()

# Segmen-segmen
segments = {
    'A': canvas.create_rectangle(250, 35, 450, 60, fill='grey'),
    'B': canvas.create_rectangle(460, 60, 485, 240, fill='grey'),
    'C': canvas.create_rectangle(460, 260, 485, 440, fill='grey'),
    'D': canvas.create_rectangle(250, 440, 450, 465, fill='grey'),
    'E': canvas.create_rectangle(215, 260, 240, 440, fill='grey'),
    'F': canvas.create_rectangle(215, 60, 240, 240, fill='grey'),
    'G': canvas.create_rectangle(250, 235, 450, 260, fill='grey'),
}

# Buat label dan entry untuk memasukkan input
label = tk.Label(window, text="Masukkan angka (0-9):")
label.pack()

entry = tk.Entry(window)  #kotak input
entry.pack()

# Buat tombol untuk menampilkan 
button = tk.Button(window, text="Tampilkan", command=on_button_click)
button.pack()

# Buat label untuk menampilkan input biner dan decoder output
binary_input = tk.StringVar()
decoder_output = tk.StringVar()

# Buat tabel dengan treeview
table = ttk.Treeview(window, columns= ('Biner(w)', 'Biner(x)', 'Biner(y)', 'Biner(z)', 'Segment A', 'Segment B', 'Segment C', 'Segment D', 'Segment E', 'Segment F', 'Segment G'), show='headings')
table.heading('Biner(w)', text='Biner(w)')
table.heading('Biner(x)', text='Biner(x)')
table.heading('Biner(y)', text='Biner(y)')
table.heading('Biner(z)', text='Biner(z)')
table.heading('Segment A', text='Segment A')
table.heading('Segment B', text='Segment B')
table.heading('Segment C', text='Segment C')
table.heading('Segment D', text='Segment D')
table.heading('Segment E', text='Segment E')
table.heading('Segment F', text='Segment F')
table.heading('Segment G', text='Segment G')

# Atur lebar kolom
table.column('Biner(w)', width=50)
table.column('Biner(x)', width=50)
table.column('Biner(y)', width=50)
table.column('Biner(z)', width=50)
table.column('Segment A', width=70)
table.column('Segment B', width=70)
table.column('Segment C', width=70)
table.column('Segment D', width=70)
table.column('Segment E', width=70)
table.column('Segment F', width=70)
table.column('Segment G', width=70)
table.pack()

# Jalankan window
window.mainloop()




