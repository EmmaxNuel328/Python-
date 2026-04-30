def Length(prompt):
	sum = 0
	for prompt in prompt:
		sum = sum + 1
	return sum
def second(prompt):
	return prompt * 60
	seconds = prompt * 60
print(prompt, " min in seconds is ",second(prompt),"second")
