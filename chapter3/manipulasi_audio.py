import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
from pydub.playback import play
import tempfile
import os

# Definisikan fungsi untuk memutar musik
def play_music():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav *.flac")])
    if file_path:
        try:
            audio = AudioSegment.from_file(file_path)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
                temp_path = temp_file.name
                audio.export(temp_path, format="wav")
            play(AudioSegment.from_file(temp_path))
            os.remove(temp_path)  # Menghapus file sementara setelah pemutaran selesai
        except Exception as e:
            print(f"❌ Terjadi kesalahan saat memuat file: {e}")

# Inisialisasi jendela aplikasi
root = tk.Tk()
root.title("Multimedia Application")

# Membuat tombol untuk memutar musik
play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack()

# Jalankan loop utama Tkinter
root.mainloop()
