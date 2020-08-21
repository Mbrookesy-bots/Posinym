import tweepy

#Gather data from config file for authentication
with open("../config.txt", "r") as config:

    file = config.readlines()

    consumerApiKey = file[0][18:44]
    consumerApiSecretKey = file[2][25:76]
    bearerToken = file[4][14:133]
    authApiKey = file[6][19:69]
    authApiSecret = file[8][26:72]

auth = tweepy.OAuthHandler(consumerApiKey, consumerApiSecretKey)
auth.set_access_token(authApiKey, authApiSecret)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error")