prompt = input("Enter a word: ")
def Vowels(prompt):
	reverse = " "
	for prompts in prompt:
		reverse =  prompts + reverse
	return reverse
print(Reverse(prompt))	
