# bs4 is a web scrapping and html parsing module
# allows you to extract information from html documents and then modify html documents
from bs4 import BeautifulSoup
import requests

# READING HTML FILES:
# ----------------------


# to read an html file you need one first
# first open the file using with open() as f(f standing for file)
# first parameter is the html file name, second is how to open it, r means read mode
# with open("dummy.html", 'r') as f:

	# create a variable for the file as doc, set it equal to beautiful soup
	# first parameter is the document you want to read into bs4 then html.parser to parse ity as an html file
	# if you then print out doc or whatever you called the file you will get the full html file
	# doc = BeautifulSoup(f, "html.parser")

# use doc.prettify to get all the indentation
# print(doc.prettify)

# ---------------
# FINDING THINGS BY TAGS
# ----------------

# say doc(or whatever the file is named).title if its a the title tag or p if its a p
# not if theres multiple html tags with the same tag name it will only return the first one

# title_tag = doc.title
# print(title_tag)

# accessing just the string inside the tag:
# use .string
# print(title_tag.string)
# 

# you can also change the inner string/conten

# title_tag.string = "Ame's Hello"
# print(title_tag)

# -------
# finding more than just the first element
# -------

# use .find("tag name")
# to find more than just one use find_all('tag name')
# p_tag = doc.find_all('p')
# print(p_tag)

# ------------
# how to access tags within another tag
# ------------

# so you can index the tags once youve assinged them to a variable
# print(p_tag[0])

# then you can use find_all on it again
# you can even index it and store it in a variable
# print(p_tag[1].find_all('b')

# ------------------------------------------------------
# parsing a website html:
# ------------------------------------------------------

# from the comand line make sure to pip install requests
# this allows you to access websites 

# wyou go the the specific page and copy the link
# import requests


# create a url variable and set it to the link of the webpage of interest
# url = "https://www.newegg.com/gigabyte-geforce-rtx-3080-ti-gv-n308tvision-oc-12gd/p/N82E16814932437"


# then create a result variable and send the a request to get the url
# this will return the content of the page and will be stored in result
# result = requests.get(url)
# print(result)

# create the doc variabe again and set it to BeautifulSoup(result.text, html.parser)
# doc = BeautifulSoup(result.text, "html.parser")
# print(doc.prettify())


# this website is a  pc part buying site, if we want to find the price on the page we can just look for the dollar sign
# we can create a variable called prices, use the find all on the doc variable and search for specific text instead of a dollar sign
# prices = doc.find_all(text = '$') 
# print(prices)

# this will just give us every instand of the dollar sign alone, but to find the actual amount we would need the parent element
# for price in prices:
	# print(price.parent)

# we know that the first instance is the price of interest so we can index it
# parent = prices[0].parent

# we also know the the actual price is in a strong tag
# price_strong = parent.find('strong')
# print(price_strong.string)


# ------------------------------------------------------
# Part 2: Advanced Searching, Filtering, Modifying
# ------------------------------------------------------

# using a new file:

# with open('index.html', 'r') as f:
# 	doc = BeautifulSoup(f, "html.parser")

# Modifying attributes of tags
# option_tag1 = doc.find('option')
# print(option_tag1)
# to modify the attributes of the tag such as selected, value place the attribute you want tp change into square brackets
# option_tag1['value'] = 'new value'
# print(option_tag1)

# changing its class or id works the same way
# option_tag1['class'] = 'heavy'
# print(option_tag1)

# if you want to see what the attributes are
# print(option_tag1.attrs)

# ---------------------
# advanced find()
# ---------------------


# when you just pass a word inthe find/find_all() brackest youre looking for a tag
# you can search multiple tags at the same time by inputing a list

# multi_tags = doc.find_all(['p', 'div'])
# print(multi_tags)

# you can search for specific things as well such as a tag with specific text
# undergrad_op = doc.find('option', string = 'Undergraduate')

# print(undergrad_op)

# looking for specific attr as well to make the search more specific
# undergrad_op_val = doc.find('option', string = 'Undergraduate', value = 'undergraduate')

# look for class names/ids
# you use class_= if youre searching for a class
# undergrad_op['class'] = 'hello'
# hello_class = doc.find(class_='hello')
# print(hello_class)

# --------------
# using regular expressions:
# --------------

# import the re module
# import re

# the re module allows you to use regular expressions
# trying to find somethin that has a dollar sign and the text beside the dollar sign
# you say string/text = re.compile then a backslash, the special character you want to search
# a full stop then star, this will look for any character next to the dollar sign
# price = doc.find(string=re.compile('\$.*'))

# . strip to remove white spaces
# print(price.strip())

# limiting results when you search when using find all
# use the limit key word and the amount you want to limit it to
# first_3_op = doc.find_all('option', limit=3)
# print(first_3_op)

# --------------------------------------------
# saving the modifications to the document
# --------------------------------------------

# first we modify
# we find all input tags with type = text
# inputs = doc.find_all('input', type='text')
# for i in inputs:
	# i['placeholder'] = 'I changed the placeholder'


# to save these changes
# use withbopen again, name the new html file then use 'w' instead of 'r' as we are writing a new file nott reading 
# then file.write()  and input the string of your doc variable you modified
# this takes the text of the doc and writes it in the new file named changed.html
# with open('changed.html', 'w') as file:
	# file.write(str(doc))

# the new file will be saved in the same folder



# --------------------------------------
# PART 3: Traversing the DOM
# --------------------------------------

# DOM/TREE TRAVERSAL:

# We qill be looking to find crypto prices and names from a website
# the data is on the tbody tag

# url = 'https://coinmarketcap.com/'
# result = requests.get(url).text
# doc = BeautifulSoup(result, 'html.parser')

# getting the tbody
# tbody = doc.tbody

# navigating siblings
# inside tbody there are tr
# this gives all the tags inside tbody wich is the table rows
# trs = tbody.contents

# looking at the first table row
# print(trs[0])

# getting its next 
# you can also use previous sibling
# print(trs[0].next_sibling)

# you can look at the next siblings to look at all the ones that come after the current one, you must convert it into a list
# print(list(trs[1].next_siblings))

# you can use .parent
# for example if you want to know what the parent tag is
# print(trs[0].parent.name)

# you can also look at the descendants to seobject as a response just convert into a liste anything within the tag
# if you get generator 
# print(list(trs[0].descendants))

# you can also do .contents or .children to get the same result
# however childrren will only give the direct tags inside of it and not the other tags within the descendants


# ---------------------------
# getting the crypto prices and names
# ---------------------------

# we have all the table rows so we can loop through them
# we will create an empty dictionary to hold the data
# prices = {}

# we will limit it to the first 10 rows to avoid getting an errow
# for tr in trs[:10]:

	# we want to look through the table data in eacch row for the name and the price
	# if we print this we will notice that the third td is the name and the rest give the prices and changes
	# for td in tr.contents:

	# 	print(td)
	# 	print()


	# now we can index it to only print what we need name and price
	# for td in tr.contents[2:4]:
	# 	print(td)
	# 	print()

	# now we can store these in a variable called name and price as follows
	# name, price = tr.contents[2:4]

	# less complex way:
	# then we loop through the name and price accordingly

	# name = tr.contents[2]
	# price = tr.contents[3]
	# print(name)

	# now we want the name text
	# we know that the name text is inside a p tag by printing name.p
	# print(name.p)

	# now to seperate the text from the tag we use .string
	# print(name.p.string)

	# we can then say that the fixed name is = to that
	# fixed_name = name.p.string

	# now looking for the price
	# the price seems to be inside the a tag so we can iscolate that
	# print(price.a.string)

	# we can then have the save that in the current price variable
	# current_price = price.a.string

	# and now we can append these to the dictionary
	# prices[fixed_name] = current_price

# now we can print the prices
# print(prices)

# -------------------------------------------------------
# PART 4: finding cheapest in stock product
# -------------------------------------------------------

# a script to find the cheapest instock  gpu

# import re for regular expressions
import re

# the first thing is to ask the user what gpu/product they want
prod = input('What product do you want to search for?: ')


# now print in the link taking not of what we have in the link cause that determines what showes up
# we use a formated string because we insert the product in the url to make it search it on the website as well as adding in the filter code
url = f'https://www.newegg.com/p/pl?d={prod}&N=4131'



# get the page with requests
page = requests.get(url).text

# parse the page
doc = BeautifulSoup(page, 'html.parser')

# now we want to check how many pages of results we get cause we dont only want to get the first page
# so we have to try to find th pages div on the actual website that has the page numbers
# when we inspect the page we fin that the numbers are in a span with the following class: list-tool-pagination
# now look for that span in the doc
page_no_span = doc.find(class_ = 'list-tool-pagination').strong

# print(page_no_span)

# after printing the page number span we realise what we want is inside the strong tag
# we see that we dont get the actual numbers because of the comas, so convert the result into a string and split accordingly
res_pages = str(page_no_span)[26:].split('<')[0]
print(res_pages)
# now that we have the pages we want to loop through all the pages and grab all of the elements on those pages

# so we will loop fthrough the number of pages and send a page request for all of the pages
# and in the url add the following at the '&page={pages}' to search for the specific page
# for pages in range(1, int(res_pages) + 1):
# 	url = f'https://www.newegg.com/p/pl?d={prod}&N=4131&page={pages}'
# 	page = requests.get(url).text
# 	doc = BeautifulSoup(page, 'html.parser')

	# now we are grabbing every page
	# we need to grab all the right products
	# we want to have our own filter
	# it will match any text that contains this
	# items = doc.find_all(text=re.compile(prod))
	# print(items)
	




