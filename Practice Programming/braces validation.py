def braces_validation(braces_str):
	braces_dict = { '(': ')', '[': ']', '{': '}' }
	stack =[]
	for i in braces_str:
		if i in braces_dict.keys():
			stack.append(i)
		else:
			if i == braces_dict[stack[-1]] and stack:
				stack.pop()
	if len(stack)>0:
		return False
	else:
		return True
