# Write your solution for algorithm 4 below
test_string = "I love software engineering"

sorted_strings = sorted(test_string.split(), key = str.lower)
print(sorted_strings)