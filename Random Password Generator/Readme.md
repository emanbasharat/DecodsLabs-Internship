# 🔐 Random Password Generator

A simple **Python Random Password Generator** that creates a random password based on the length entered by the user.

The generator uses uppercase letters, lowercase letters, numbers, and special characters to create a random password.

## ✨ Features

* Allows the user to choose the password length
* Generates a random password
* Includes uppercase and lowercase letters
* Includes numbers
* Includes special characters such as `@`, `#`, and `$`
* Simple beginner-friendly Python project

## 🛠️ Technologies Used

* **Python**
* `random` module
* `string` module

## 📌 How It Works

1. The program asks the user to enter the desired password length.
2. It creates a character set containing:

   * Uppercase letters
   * Lowercase letters
   * Numbers
   * Special characters (`@`, `#`, `$`)
3. A `for` loop runs according to the requested password length.
4. `random.choice()` selects a random character.
5. The selected characters are added to the password.
6. The final password is displayed.

## 💻 Code

```python
import random
import string

length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits + "@#$"

password = ""

for i in range(length):
    password += random.choice(characters)

print("Your password is:", password)
```

## ▶️ Example Output

```text
Enter password length: 12
Your password is: aB7@kP2$xQ9m
```

## 📚 What I Learned

Through this project, I practiced:

* Taking user input using `input()`
* Converting input into an integer using `int()`
* Using Python modules
* Working with strings
* Using `for` loops
* Using `random.choice()`
* Combining different character sets
* Building a simple Python project

## 🚀 Future Improvements

This project can be improved by adding:

* More special characters
* Password strength checking
* Option to generate multiple passwords
* Copy-to-clipboard functionality
* A graphical user interface (GUI)

## 👩‍💻 Author

**Emaan Basharat**

This project was created as part of my Python learning and internship practice.
