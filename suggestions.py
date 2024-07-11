import discog_api
import pytube 

def request_licked_video(url):
    return [discog_api.request_credits(pytube.title(url))]

def random_suggestion(list, how_many_you_want):
    suggestions = []
    while true:
        suggestions.Add(Random(list))
        if suggestions.count > how_many_you_want:
            break
    return [suggestions]

def get_suggestion(url):
    return random_suggestion(request_licked_video(url))

def visual_page(new_video):
    history = []
    render(history.add(new_video))
    
    