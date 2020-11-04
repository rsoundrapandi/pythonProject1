# Python3 code to demonstrate working of
# Convert List of String List to String List
# using map() + generator expression + join() + isdigit()

# helper function
def convert(sub):
	return "".join(ele if ele.isdigit() else "" for ele in sub)

# initialize list
test_list = ["[1, 4]", "[5, 6]", "[7, 10]"]

# printing original list
print("The original list : " + str(test_list))

# Convert List of String List to String List
# using map() + generator expression + join() + isdigit()
res = list(map(convert, test_list))

# printing result
print(res)
