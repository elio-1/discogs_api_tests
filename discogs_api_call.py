import discogs_client
import random


def random_number_from_0_to(max_n):
    return random.randint(0, max_n)

# ----------------------------
def print_line():
    return print("-"*10)


token = input("token: ")
d = discogs_client.Client('my_user_agent/1.0', user_token=token)


print_line()
search_input = input("Search: ")
print_line()

# this use the search part of the api https://www.discogs.com/developers#page:database,header:database-search 
# and return this <discogs_client.models.MixedPaginatedList object at 0x00...>
results = d.search(search_input, type="release")

# result contain all the pages of every release and the different versions (albums, remaster, remix, etc.)

# full dict with results.data

# lists of info we can get on a song 

# all the credits of the song. to note : the produters and song writers are generally last.
artists = results[0].credits
# list of dict containing every artist with  more info (same order as result[0].credits)
credits_detailed = results[0].data["extraartists"]
#exemple credits_detailed[0]['role'] return Bass 

year = results[0].year
genre = results[0].genres
style = results[0].styles
# since there can sometime be more than one video and the first one isnt always the official one. since its discogs its usually vinyl v but hey
video_url_link = results[0].data["videos"][0]['uri']

print(artists + " //  " + year + " " + genre + " " + style +" // "+ video_url_link)
# genre = song["genre"]
# # extraatists is weird but we should get the arranger or somoething cool
# arrangedby = song["extraartists"][0]['name']


## curl "https://api.discogs.com/database/search?q=earth+wind+fire+september" -H "Authorization: Discogs token=TOKEN"
## /database/search?q={query}&{?type,title,release_title,credit,artist,anv,label,genre,style,country,year,format,catno,barcode,track,submitter,contributor}
## curl "https://api.discogs.com/database/search?q=earth+wind+fire+september&type=release" -H "Authorization: Discogs token=TOKEN"