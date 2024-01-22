user_input = input("Enter a string: ")
result_string = ''.join(sorted(user_input, key=lambda x: (x.isupper(), x.lower() if x.islower() else x == ' ')))
print("Modified String:", result_string)
