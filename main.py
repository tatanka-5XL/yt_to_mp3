import yt_dlp

# Ask for YouTube URL
url = input("Enter YouTube video URL: ")

# Options to download best audio only
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',  # Output filename = video title
    'ffmpeg_location': '/Users/petrp/.local/bin/ffmpeg', 
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'quiet': False,
    'noplaylist': True,
}

# Run the downloader
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

