filename = "importing_text_file/source.txt"
file = open(filename, mode = "r")
file_content = file.read()
# print(file_content)

# using the with function to obtain the same result 

# write the contents to file
with open(filename, mode= "w") as new_text:
    edit_text = new_text.write("I just edited my initial text")

    # Read the contents of the file
with open(filename, mode="r") as read_file:
    written_text = read_file.read()

# Print the written text
print(written_text)

print(edit_text)