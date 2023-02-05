
"""
Module for currency exchange
This module provides several string parsing functions to
implement a simple currency exchange routine using an online currency
service.
The primary function in this module is exchange.
Author: Pankaj Yadav
Date:30-11-2022

"""

def before_space(s):
	"""Returns:a copy of s up to, but not including, the first space

	Parameter s:the string to slice
	Precondition:s is a string with at least one space

	test cases-
	>>> before_space("2.8 usd")
	'2.8'
	>>> before_space("4.567  inr")
	'4.567'
	>>> before_space(" 3.89 euros")
	''
	>>> before_space("4.68cup   ")
	'4.68cup'
	"""

	end_first=s.find(' ')
	first=s[0:end_first]
	return first



def after_space(s):
	"""Returns a copy of s after the first space
	Parameter s: the string to slice
	Precondition: s is a string with at least one space
	test cases-
	# i want to test the space pass

	>>> after_space("2.8 usd") 
	'usd'
	>>> after_space("4.56  inr")
	' inr'
	>>> after_space(" 3.9 euros")
	'3.9 euros'
	>>> after_space("4.67cup ")
	''
	>>> after_space('45.78inr  ')
	' '
	"""
	end_first=s.find(' ')
	last=s[end_first+1:]
	return last


def first_inside_quotes(s):
	"""Returns:the first substring of s between two (double) quotes

	A quote character is one that is inside a string, not one that
	delimits it. We typically use single quotes (') to delimit a
	string if we want to use a double quote character (") inside of
	it.
	Examples:
	first_inside_quotes('A "B C" D') returns 'B C'
	first_inside_quotes('A "B C" D "E F" G') returns 'B C',
	because it only picks the first such substring
	Parameter s: a string to search
	Precondition: s is a string containing at least two double
	quotes.

	test cases-
	#it takes first substring
	>>> first_inside_quotes('m"a d"g')
	'a d'
	>>> first_inside_quotes('mala "ya la y" f')
	'ya la y'

	"""
	end_first=s.find('"')+1
	start=s.find('"',end_first)
	last=s[end_first:start]
	return last



def get_lhs(json):
	"""Returns:Returns the lhs value in the response to a currency query
	Given a JSON response to a currency query, this returns the
	string inside double quotes (") immediately following the
	keyword
	"lhs". For example, if the JSON is
	'{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }'
	then this function returns '1 Bitcoin' (not '"1 Bitcoin"').
	This function returns the empty string if the JSON responsequit()
	contains an error message. 
	Parameter json: a json string to parse
	Precondition: json is the response to a currency query

	test cases-
	#testing for more than one space between string
	
	>>> get_lhs('{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }')
	'1 Bitcoin'
	>>> get_lhs('{ "lhs" : "1  Doller", "rhs" : "19995.85429186 Euros", "err" : "" }')
	'1  Doller'

	"""
	first_colon=json.find(':')+3
	first_comma=json.find('"',first_colon)
	get_lhs=json[first_colon:first_comma]
	return get_lhs


def get_rhs(json):
	"""Returns: the rhs value in the response to a currency query
	Given a JSON response to a currency query, this returns the
	string inside double quotes (") immediately following the
	keyword
	"rhs". For example, if the JSON is
	'{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }'
	then this function returns '19995.85429186 Euros' (not
	'"38781.518240835 Euros"').
	This function returns the empty string if the JSON response
	contains an error message.
	Parameter json: a json string to parse
	Precondition: json is the response to a currency query

	# check the rhs of jason
	test case-
	>>> get_rhs('{ "lhs" : "3 Bitcoin", "rhs" : "234555.34 Euros", "err" : "" }')
	'234555.34 Euros'
	>>> get_rhs ('{ "lhs" : "2 Doller", "rhs" : "162.345 INR", "err" : "" }')
	'162.345 INR'

	"""
	first_colon=json.find(':')
	second_colon=json.find(':',first_colon+1)+3
	second_comma=json.find('"',second_colon)
	get_rhs=json[second_colon:second_comma]
	return get_rhs


def has_error(json):
	"""Returns: True if the query has an error; False otherwise.
	Given a JSON response to a currency query, this returns True if
	there
	is an error message. For example, if the JSON is
	'{ "lhs" : "", "rhs" : "", "err" : "Currency amount is invalid." }'
	then the query is not valid, so this function returns True (It
	does NOT return the message 'Currency amount is invalid.').
	Parameter json: a json string to parse
	Precondition: json is the response to a currency query

	# test the error of json
	test cases-
	>>> has_error('{ "lhs" : "", "rhs" : "", "err" : "Currency amount is invalid." }') 
	True
	>>> has_error('{ "lhs" : "2.8 USD", "rhs" : "52.5 INR", "err" : "" }')
	False
	>>> has_error('{ "lhs" : "2.8 USD", "rhs" : "123.566 INR", "err" : "" }')
	False
	"""
	first_colon=json.find(':')+1
	second_colon=json.find(':',first_colon+1)+1
	third_colon=json.find(':',second_colon)+3
	is_qoute=json.find('"',third_colon)
	error_string=json[third_colon:is_qoute]
	
	return error_string!=''

def query_website(old, new, amt):
	"""
	Returns: a JSON string that is a response to a currency query.

	A currency query converts amt money in currency old to the currency new. The response should be a string of the form
	'{ "lhs":"<old-amt>", "rhs":"<new-amt>", "err":"" }' where the values old-amount and new-amount contain the value
	and name for the old and new currencies. If the query is invalid, both old-amount and new-amount will be empty, while
	"err" will have an error message.

	Parameter old: the currency on hand

	Precondition: old is a string with no spaces or non-letters

	Parameter new: the currency to convert to

	Precondition: new is a string with no spaces or non-letters

	Parameter amt: amount of currency to convert

	Precondition: amt is a float

	Parameter new: the currency to convert to

	Precondition: new is a string with no spaces or non-letters

	Parameter amt: amount of currency to convert

	Precondition: amt is a float





	test cases-

	>>> query_website('INR','CUP',2.34)
	'{ "lhs" : "2.34 Indian Rupees", "rhs" : "0.75518862714378 Cuban Pesos", "err" : "" }'



	"""
	import requests
	json = (requests.get('http://cs1110.cs.cornell.edu/2022fa/a1?old={0}&new={1}&amt={2}'.format(old,new,amt))).text
	return json


def is_currency(code):

	"""
	Returns: True if code is a valid (3 letter code for a) currency It returns False otherwise.

	Parameter code: the currency code to verify

	Precondition: code is a string with no spaces or non-letter.

	test cases-
	>>> is_currency('INR')
	True
	>>> is_currency('AAA')
	False

	"""
	return not(has_error(query_website(code,code,2.5))==True)

  	
	
def exchange(old, new, amt):

	"""
	Returns: the amount of currency received in the given exchange. In this exchange, the user is changing amt money in currency
	old to the currency new. The value returned represents the amount in currency new.
	The value returned has type float.


	Parameter old: the currency on hand

	Precondition: old is a string for a valid currency code

	Parameter new: the currency to convert to

	Precondition: new is a string for a valid currency code

	Parameter amt: amount of currency to convert

	Precondition: amt is a float

	#
	test cases-
	>>> exchange('INR','USD',82.7)
	'1.03649654742'



	"""

	json=query_website(old, new,  amt)
	exchange_amt=get_rhs(json)
	return before_space(exchange_amt)

# if __name__=='__main__':
#   	import doctest
#   	doctest.testmod()
  	

	

		






