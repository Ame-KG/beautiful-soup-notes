# bs4 is a web scrapping and html parsing module
# allows you to extract information from html documents and then modify html documents
from bs4 import Beautifulsoup


# READING HTML FILES:
# ----------------------


# to read an html file you need one first
# first open the file using with open() as f(f standing for file)
# first parameter is the html file name, second is how to open it, r means read mode
with open("dummy.html", 'r') as f:

	# create a variable for the file as doc, set it equal to beautiful soup
	# first parameter is the document you want to read into bs4 then html.parser to parse ity as an html file
	# if you then print out doc or whatever you called the file you will get the full html file
	doc = Beautifulsoup(f, "html.parser")
print(doc)






