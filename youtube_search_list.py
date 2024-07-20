from pytube import Search

def get_url(videos):
    return [f"https://www.youtube.com/watch?v={Search(video_name).results[0].video_id}" for video_name in videos]
