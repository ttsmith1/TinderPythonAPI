with open("tinder_api/utils/token.txt", "r") as f:
    tinder_token = f.read()

# it is best for you to write in the token to save yourself the file I/O
# especially if you have python byte code off
#tinder_token = ""

headers = {
    'app_version': '6.9.4',
    'platform': 'ios',
    'content-type': 'application/json',
    'User-agent': 'Tinder/7.5.3 (iPohone; iOS 10.3.2; Scale/2.00)',
    'X-Auth-Token': 'b20844b0-6ead-41cb-976b-0aee5ff0e5ed',
}

host = 'https://api.gotinder.com'

if __name__ == '__main__':
    pass
