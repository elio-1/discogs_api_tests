from pytube import Search, YouTube

def get_url(videos):
    return [f"https://www.youtube.com/watch?v={Search(video_name).results[0].video_id}" for video_name in videos]

def get_video_title(video_url):
    return YouTube(video_url).vid_info["videoDetails"]["title"]

# def main():
#     print(get_video_title('https://www.youtube.com/watch?v=bTDJyQqbYCA'))

# if __name__ == "__main__":
#     main()