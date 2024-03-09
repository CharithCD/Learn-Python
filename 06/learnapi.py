import requests
import sys
import json

if len(sys.argv) < 2:
    sys.exit("Not enough arguments")

# response = requests.get("https://api.github.com/users/" + sys.argv[1])
# response =  requests.get("https://itunes.apple.com/search?term="+sys.argv[1]+"&limit=1")
ARTIST_NAME = sys.argv[1]
responses =  requests.get("https://itunes.apple.com/search?term="+ ARTIST_NAME + "&entity=song&limit=5")
# responses =  requests.get("https://itunes.apple.com/search?term="+ ARTIST_NAME + "&entity=album&limit=5")

# print(json.dumps(responses.json(), indent=4, sort_keys=True))

for result in responses.json()["results"]:
    print(result["trackName"])