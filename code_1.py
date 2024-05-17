""" 
https://www.linkedin.com/in/prasad-sankalpa-0267b4218/
 """

import pyshorteners as psh

link = input("\nEnter your link here : ")

short_link = psh.Shortener()
x = short_link.tinyurl.short(link)

print("\nHere is your shorted link : "+x)