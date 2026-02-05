filename = "output.txt"


user_input_1 = input("Enter text to write to the file: ")

with open(filename, "w") as file:
    file.write(user_input_1 + "\n")

print(f"Data successfully written to {filename}.")
print()

user_input_2 = input("Enter additional text to append: ")

with open(filename, "a") as file:
    file.write(user_input_2 + "\n")

print("Data successfully appended.")
print() 


print(f"Final content of {filename}:")

with open(filename, "r") as file:
    content = file.read()
    print(content)