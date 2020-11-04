# write data in a file.

with open("Create a file.txt","a") as file1:

    L = ["This is Delhi345345 \n","This is Paris345345 \n","This is London \n"]
    # \n is placed to indicate EOL (End of Line)
    file1.write("Write data in it I have completed 10 days successfully. \n")
    file1.writelines(L)
    file1.write("soundrapandian \n")
# with open("Create a file 30 days 30 hour operations.txt", "r") as file2:
#         print("Output of Readline(9) function is :")
#         print(file2.read())
#         print





# print("Output of Read function is :")
# print(file1.read())
#
# # seek(n) takes the file handle to the nth
# # bite from the beginning.
# file1.seek(0)
#
# print("Output of Readline function is :")
# print(file1.readline())

