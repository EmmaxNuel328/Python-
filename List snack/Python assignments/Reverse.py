prompt = input("Enter a word: ")
def Reverse(prompt):
	reverse = " "
	for prompts in prompt:
		reverse =  prompts + reverse
	return reverse
print(Reverse(prompt))	
