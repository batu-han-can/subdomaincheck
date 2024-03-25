import requests

def make_requests(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass

target_input = "google.com"

with open("subdomainlist.txt","r") as subdomainlist:
    for word in subdomainlist:
        word = word.strip()
        url = "http://" + word + "." + target_input
        response = make_requests(url)
        if response:
            print("Bulundu Subdomain ---->>>" + url)
