import os
from dotenv import load_dotenv
import discogs_client

load_dotenv()

token = os.getenv("DISCOGS_SECRET_KEY")
d = discogs_client.Client('my_user_agent/1.0', user_token=token)
search_input = input("Search: ")
results = d.search(search_input, type="release")
artists = results[0].credits
if artists:
    print(artists)
    i = 1
    while True:
        if bool(word not in artists[-1].name for word in search_input.split()):
            break
        i = 2
    print("searching for: " + artists[-i].name)
    results2 = d.search(artists[-i].name, type="release")
    print(results2[0].title)
    print(results2[1].title)
    print(results2[2].title)
else:
    print('no credit found')