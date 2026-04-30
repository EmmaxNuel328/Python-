prompt = int(input("Enter a number in minute(s): "))
def second(prompt):
	return prompt * 60
print(prompt, " min in seconds is ",second(prompt),"second")
def hour(prompt):
	return prompt/ 60
print(prompt,"min in hours is ", hour(prompt),"hour")