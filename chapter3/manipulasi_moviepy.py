from moviepy.editor import VideoFileClip, concatenate_videoclips

def process_videos(input_path, output_path, short_output_path, combined_output_path):
    try:
        # Muat video
        video = VideoFileClip(input_path)
        print("✅ Video berhasil dimuat")

        # Simpan video awal
        video.write_videofile(output_path)
        print("✅ Video berhasil disimpan sebagai result.mp4")

        # Buat subclip dari video
        short_video = video.subclip(0, 10)
        short_video.write_videofile(short_output_path)
        print("✅ Subclip berhasil disimpan sebagai short_result.mp4")

        # Gabungkan video dengan subclip
        combined_video = concatenate_videoclips([video, short_video])
        combined_video.write_videofile(combined_output_path)
        print("✅ Video gabungan berhasil disimpan sebagai combined_result.mp4")

    except Exception as e:
        print(f"❌ Terjadi kesalahan: {e}")

if __name__ == "__main__":
    input_path = 'help.mp4'
    output_path = 'result.mp4'
    short_output_path = 'short_result.mp4'
    combined_output_path = 'combined_result.mp4'
    
    process_videos(input_path, output_path, short_output_path, combined_output_path)
