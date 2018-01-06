import tweepy
import json
# from pprint import pprint
import time


outputFile = open('graph.csv', 'w')



key = json.load(open('keys.json'))
auth = tweepy.OAuthHandler(key['api_key'], key['api_secret'])
auth.set_access_token(key['token'], key['token_secret'])

api = tweepy.API(auth)

initialUsername = 'techieVignesh'
user = api.get_user(initialUsername)

# public_tweets = api.home_timeline()
# pprint(public_tweets)

# for tweet in public_tweets:
#     print(tweet.text)

# print(user.screen_name)
# print (user.followers())



index = 0
for friend in user.friends():
	# print(initialUsername + ',' + friend.screen_name)
	print('Parsing friend :' + str(index));
	outputFile.write(initialUsername + ',' + friend.screen_name + '\n')
	for primary_user_s_friend in friend.friends():
		# print(friend.screen_name + ',' + primary_user_s_friend.screen_name)
		outputFile.write(friend.screen_name + ',' + primary_user_s_friend.screen_name + '\n')
	for primary_user_s_follower in friend.followers():
		# print(primary_user_s_follower.screen_name + ',' + friend.screen_name )
		outputFile.write(primary_user_s_follower.screen_name + ',' + friend.screen_name  + '\n')
	index+=1
	if(index == 14):
		print('Code sent to sleep for 15 mins and 30 sec. Comeback Later')
		time.sleep(930)

# output = initialUsername + "," + primaryFriend.strip()
# 		outputFile.write(output + '\n')
# 	for primaryFollower 
