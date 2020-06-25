import tweepy as tw
import yaml
import uuid
import os

class twitapp:

    def connection():
        with open("/Users/davidjoy/Desktop/Astra/astra_demo/astra/twitApp/conf.yaml", "r") as conf:
            cfg = yaml.load(conf, Loader=yaml.FullLoader)
        auth = tw.OAuthHandler(consumer_key=cfg["config"]["consumer_key"],
                               consumer_secret=cfg["config"]["consumer_secret"])
        auth.set_access_token(key=cfg["config"]["access_token"], secret=cfg["config"]["access_token_secret"])
        api = tw.API(auth)

        try:
            api.verify_credentials()
            print("connected")
        except:
            print("connect issue")

        return api;

    def tweet(srch):
        sterm = "#"+srch
        api = twitapp.connection()
        tweets = tw.Cursor(api.search, q=sterm, lang="en").items(5)
        payload_data = [
            '{"columns":[{"name":"twittername","value":"'f"{tweet.user.screen_name.encode('ascii',errors='replace').decode()}"'"},\
            {"name":"username","value":"'f"{tweet.user.name.encode('ascii',errors='replace').decode()}"'"}, \
            {"name":"search","value":"'f"{sterm}"'"}, \
            {"name":"rowid","value":"'f"{uuid.uuid4()}"'"},{"name":"created_at","value":"'f"{tweet.created_at}"'"}, \
            {"name":"location","value":"'f"{tweet.user.location.encode('ascii',errors='replace').decode()}"'"}, \
            {"name":"hashtags","value":"'f"{tweet.entities.get('hashtags')}"'"}]}'
                for tweet in tweets]
        return payload_data;

# '{"columns":[{"name":"rowid","value":14}, {"name":"rowvalue", "value": "Steny Sebastian"}]}'

# 'f"{uuid.uuid4()}"'

# '{"columns":[{"name":"rowid","value":14}, {"name":"rowvalue", "value": "Steny Sebastian"}]}'
# "'f"{str(tweet.author.name.encode('UTF-8'))}"'"

# xyzaa27b-de8e-4afc-8431-8f06a326047d

#"'f"{tweet.text.encode('utf-8').decode()}"'"

# "'f"{tweet.text.encode('utf-8',errors='ignore').decode('latin-1').encode('utf-8').decode()}"'"
# "'f"{tweet.source}"'"

#{"id": tweet.id,"entities":tweet.entities,"text":tweet.text,"user":tweet.user.name,"img":tweet.user.profile_image_url,"retweet_count":tweet.retweet_count,
# "source":tweet.source,"source_url":tweet.source_url,"created_at":tweet.created_at,"media_image_url":tweet.entities.media.media_url }

# username "'f"{tweet.user.name}"'"
# screenname "'f"{tweet.user.screen_name}"'"
# location "'f"{tweet.user.location}"'"
# created_at "'f"{tweet.created_at}"'"
# hashtags "'f"{tweet.entities.get('hashtags')}"'"
# tweet.txt
# tweet.geo
#{"name":"hashtags","value":"'f"{tweet.entities.get('hashtags')}"'"}, \
#{"name":"tweettext","value":"'f"{tweet.text.encode('ascii',errors='replace').decode()}"'"]}'