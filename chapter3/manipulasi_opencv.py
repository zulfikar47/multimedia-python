import tkinter as tk
from PIL import Image, ImageTk

# Inisialisasi jendela aplikasi
root = tk.Tk()
root.title("Multimedia Application")

# Baca dan proses gambar sebelum memulai mainloop
image = Image.open('motor.png')
photo = ImageTk.PhotoImage(image)

# Buat label untuk menampilkan gambar
label = tk.Label(root, image=photo)
label.pack()

# Jalankan loop utama Tkinter
root.mainloop()
