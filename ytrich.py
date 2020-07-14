from pypresence import Presence
import time, requests

client_id = ""
ytchannel = ""
apikey = ""

while True:
    jsonshit = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=" + ytchannel + "&type=video&eventType=live&key=" + apikey)
    if "live" in jsonshit.text:
        try:
        	RPC.close()
        except:
        	pass
        RPC = Presence(client_id)
        RPC.connect()                                                                 #Gets Video ID
        RPC.update(details="Hey im Live:", state="https://youtu.be/" + jsonshit.json()["items"][0]["id"]["videoId"] ) # large_image="unnamed" (optional) Go in Application and upload a Picture in the Rich Presence Category. Put name in here. Ex. unnamed )
    time.sleep(60) #Timer in Seconds to check if Live
