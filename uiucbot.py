import praw
import time
import webbrowser

print ("Username: ")

username = raw_input()

r = praw.Reddit(user_agent = "Suraj /u/"+username)
print("Logging in...")
r.login(username, disable_warning=True) #put username and password inside if you want to auto-login
print("Which subreddit would you like to search")
a = raw_input()
#print("What words would you like to search for: ")
#words_to_match = raw_input = ()

#words_to_match = words_to_match.split(',')


#print("Searching r/"+a+" for "+words_to_match)

words_to_match = ['free', 'food', 'swag']
cache  = []

def run_bot():
	#a = "uiuc"
	#print("Grabbing subreddit ...")
	subreddit = r.get_subreddit(a) #subreddit test
	#print("Grabbing subreddit ...")
	comments = subreddit.get_comments(limit = 25) #25 calls per time


	for comment in comments:
		comment_text = comment.body
		isMatch = any(string in comment_text for string in words_to_match)
		if comment.id not in cache and isMatch:
			print("Match found! Comment ID: " + comment.id)
			#print("Match found! Comment URL: "+"https://www.reddit.com/r/"+a+"/comments/"+comment.id)
			#site = "https://www.reddit.com/r/"+a+"/comments/"+comment.id
			#print("Match found! Comment URL: "+site)
			#webbrowser.open(site)

			print(comment_text)
			print("------------------------------------------------------------------")
			
			cache.append(comment.id)
	#print("Done")


while True:
	run_bot()
	time.sleep(3)






