from suggestions import get_suggestions
from youtube_get_info import get_url, get_video_title

def main():
    print(get_url(get_suggestions(get_video_title(input('video url: ')), 4)))

if __name__ == "__main__":
    main()