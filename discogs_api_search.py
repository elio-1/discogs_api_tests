import discogs_client
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("DISCOGS_SECRET_KEY")
d = discogs_client.Client('my_user_agent/1.0', user_token=token)
search_input = input("Search: ")
results = d.search(search_input, type="release")
artists = results[0].credits
print(artists)
results2 = d.search(artists[-1].name, type="release")
print(results2[0].title)
print(results2[1].title)
print(results2[2].title)