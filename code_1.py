""" 
example web link : https://www.linkedin.com/in/prasad-sankalpa-0267b4218/
 """

import pyshorteners as psh

def is_valid_url(link):
    """ This function checks if the entered URL is in the correct format."""
    if url == "":
        return False
    parsed_url = url.split("://")
    if len(parsed_url) != 2:
        return False
    if parsed_url[0] not in ("http","https"):
        return False
    return True

def generate_short_url(url):
    """ This function generates tiny code for the URL, but first checks if the URL format is correct. """
    if not is_valid_url(url):
        return "Invalid URL format. Please enter a valid URL starting with 'http' or 'https'."
    short_url = psh.Shortener()
    x = short_url.tinyurl.short(url)
    return "Here is your shorted link : "+ x

if __name__ == "__main__":
    url = input("\nEnter your link here : ")
    short = generate_short_url(url) 
    print("\n"+short+"\n")