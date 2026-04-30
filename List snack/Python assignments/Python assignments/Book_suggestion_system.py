from Book_suggestion_function import *
book_suggestion_system = """
1. Get Book
2. Add Book
3. Remove Book
4. Update Book
5. Show all books
0. BACK
"""
book_list = ["living in Eko" ,"Without a silver spoon" ,"Naruto ","Supa strika  ","DC comics  "]
index = 0
prompt = 1
stored_books = []
while prompt != 0:
	print(book_suggestion_system)
	prompt = input("Enter a choice from the above: ")
	match(prompt):
		case "1":
			print(suggest_book(book_list))
			prompt_suggest = "yes"
			while prompt_suggest != "no":
				prompt_suggest = input("Do you another suggestion(yes/no): ")
			
				if prompt_suggest == "yes":
					print(suggest_book(book_list))
		case "2":
			print(add_books(prompt,book_list))			
		case "3": 
			prompt = input("Enter name of book you want to  remove: ")
			print(remove_books(prompt,book_list))