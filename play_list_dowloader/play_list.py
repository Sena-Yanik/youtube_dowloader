import yt_dlp

def download_playlist(url, save_path="."):
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{save_path}/%(playlist)s/%(title)s.%(ext)s'
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Playlist download complete!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    playlist_url = input("Enter YouTube playlist URL: ")
    download_playlist(playlist_url)