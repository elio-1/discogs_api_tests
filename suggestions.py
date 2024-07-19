import os
from dotenv import load_dotenv
import discogs_client
import re

def load_api_key():
    load_dotenv()
    return os.getenv("DISCOGS_SECRET_KEY")

def get_suggestions(search_input, how_many=3):
    search_input = search_input.lower()
    d = discogs_client.Client('my_user_agent/1.0', user_token=load_api_key())
    results = d.search(search_input, type="release")
    artists = results[0].credits
    if artists:
        i = 1
        while True:
            tmp_artist = artists[-i].name.lower().split()
            if len(tmp_artist) > 1:
                pattern = fr"\b(?:{tmp_artist[0]})|(?:{tmp_artist[1]})\b"
            else:
                pattern = fr"\b(?:{tmp_artist[0]})\b"
            if not re.search(pattern, search_input):
                break
            if i > len(artists):
                break
            i += 1
            print(i)
        print("searching for: " + artists[-i].name)
        results2 = d.search(artists[-i].name, type="release")
        suggestions = [results2[i].title for i in list(range(how_many))]
        print(suggestions)
        return suggestions
    else:
        raise Exception('no credit found, try to be more specific with the search input.')
    
def main():
    get_suggestions(input('search: '), 4)

if __name__ == "__main__":
    main()
