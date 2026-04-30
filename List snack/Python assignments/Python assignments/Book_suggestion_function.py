import random
def suggest_book(book_list = []):
	suggested_book = random.choice(book_list)
	pages = random.randint(1,2000)
	return suggested_book,pages
def add_books(prompt,book_list = []):
	prompt = input("Enter name of book you want to add and page(seperate the name of the book from the page with |): ")
	book_list.append(prompt)
	return book_list
def remove_books(prompt,book_list):
	for index in book_list:
		if book_list == index:
			book_list.remove(prompt)
	return book_list
