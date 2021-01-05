# Tinder Python API

THE ENDPOINTS HAVE CHANGED. THIS REPO IS OUT OF DATE. UPDATE TO COME.
This project contains python bindings for the unoffical tinder api. The tinder api is constantly changing and current libraries are not always up to date. This project is a mix of Pynder's style and Fbessez's endpoints/auth. Current a work in progress but is suitable for non-production projects.

## AUTHENTICATION

Tinder switched away from account-kit. Please use the SMS auth file to get your tinder token. I suggest hard coding it into the config.py file after you have obtained it.
If sms_auth is not working for you, you can find your tinder token using chrome inspector tool. Login to tinder.com, and search it the network tab for a request from the api. Check the request Headers for x-auth-token. Once you copy it, paste it into config.py.

## Getting Started

You will need to insert your tinder_token in the utils/config.py file. This currently uses SMS auth method for verification as FaceBook auth has changed.
Clone this repo, in your project import tinder_api and get to work. The example.py shows how to get rolling.

## Usage

```
import tinder_api.session

sess = tinder_api.session.Session() # creates a session

print(sess.meta) # prints your meta data
sess.update_profile(bio="I love VIM") # updates your bio - see kwargs

for user in sess.yield_users():
    user.name
    user.id
    user.age
    user.bio
    user.gender # male or female
    user.photos # url of the photos
    user.like() # swipe right
    user.pass() # swipe left
    user.super_like() # swipe up

    user.report(1) # report for spam

for match in sess.yield_matches():
    match.name # all the same endpoints as a normal user
    match.match_data # contains match data like messages/profile
    match.message('Hello, I use VIM so I am superior to all those other programmers you've dated')
    match.get_messages()
```
