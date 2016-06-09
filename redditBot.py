import praw
import time
print ("Username: ")
username = raw_input()
r = praw.Reddit(user_agent = "Suraj /u/"+username)
print("Logging in...")
r.login(username, disable_warning=True) #put username and password inside if you want to auto-login


words_to_match = ['definately', 'defiantly', 'definantly', 'definatly']
cache  = []

def run_bot():
	print("Grabbing subreddit ...")
	subreddit = r.get_subreddit("test") #subreddit test
	print("Grabbing subreddit ...")
	comments = subreddit.get_comments(limit = 25) #25 calls per time
	for comment in comments:
		comment_text = comment.body
		isMatch = any(string in comment_text for string in words_to_match)
		if comment.id not in cache and isMatch:
			print("Match found! Comment ID: " + comment.id)
			comment.reply('I think you meant to say "definitely"')
			print("Reply successful!")
			cache.append(comment.id)
	print("Comments loop finished, time to sleep")


while True:
	run_bot()
	time.sleep(3)






