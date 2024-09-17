# %% [markdown]
# # DATASCI 101: Homework 02
# 
# 
# This is an iPython Notebook. You can edit the cells to answer the prompts. Feel free to add more cells as needed. Use "Markdown" cells writing text. When you are finished, use the Explorer pane to find this file. Right click and select download. Upload your submission on Gradescope!
# 
# 
# ## Question 1
# 
# ### Q1.a
# 
# Demonstrate using a Jupyter notebook.
# 
# Create a new code cell after this cell and create a variable called `password` that contains the string "chinchilla" as its only item. Then run the cell. 
# 
# ---
# 

# %%
password = 'chinchilla'

# %% [markdown]
# 
# Now create another code cell. In this one enter only the word `password` and run the cell. 
# 
# ----
# 

# %%
password

# %% [markdown]
# 
# Now edit this text cell to add an explanation of why the two cells behave differently.
# 
# 
# The first cell, password = 'chinchilla', is an assignment operator. This means that when we run this code, we are assigning a string value of 'chinchilla' to the variable named password. In the second cell, we just typed in the variable name password after assigning it to the string value of 'chinchilla' in the previous cell. When we run the second cell, we are asking for the value of the variable, which is why we got an output of the string 'chinchilla'. The two cells behave differently since the first cell handles variable assignment and the second cell is accessing the value of the string variable password. 
# 
# ---
# 

# %% [markdown]
# Now create a cell that creates the `password` variable on one line and then has only the word `password` on the next line. Run the cell. Create another text cell after that one and explain how you can use the behavior you are seeing here to show your results on homework assignments.

# %%
password = ' '
password

# %% [markdown]
# We can use the behavior of the cell above for homework assignments by noticing how Python keeps track of variable values and displays their output. Since the second line makes it possible for the variable value to be outputted, this is how we can show results. 

# %% [markdown]
# 
# 
# ### Q1.b
# 
# In the rest of this homework, we are going to write some code related to password security. 
# 
# Suppose a website stores passwords in plain text. The user will supply a password, and the website will store it in a variable called `attempt`.
# 
# Write a function that takes in the `attempt` and the `password` and returns `True` if they are the same and `False` otherwise.
# 
# * Verify (show in code) that your function works by calling it with the password "chinchilla" and the attempt "chinchilla".
# * Verify that your function works by calling it with the password "chinchilla" and the attempt "Chinchilla".
# 
# Use comments to explain what you expect to see in the output of your function from previous two applications of your function.

# %%
attempt = 'chinchilla'
password = 'chinchilla'

def password_security(attempt, password):
    if attempt == password:
        return True
    else: 
        return False
    
password_security(attempt, password)
    
# from the output of this code, we would expect to get a return value of 'True' 
# since the attempt variable and the password variable are both set to 'chinchilla', 
# which are identical variable names. 

# %%
attempt = 'Chinchilla'
password = 'chinchilla'

def password_security(attempt, password):
    if attempt == password:
        return True
    else: 
        return False
    
password_security(attempt, password)
    
# from the output of this code, we would expect to get a return value of 'False' 
# since the attempt variable and the password variable are not equivalent
# due to the C in 'chinchilla' being uppercase on the attempt

# %% [markdown]
# ### Q1.c
# 
# Suppose we have a **dictionary** of users and their passwords. The keys are the usernames and the values are the passwords. 
# 
# Here are several users and their passwords:
# 
# | Username | Password |
# |----------|----------|
# | alice    | chinchilla |
# | bob      | 123456 |
# | charlie  | password |
# 
# Create a dictionary called `users` that contains the above information.
# 
# Now write a function that takes in a `username` and a `password` and returns `True` if the `username` is in the `users` dictionary and the `password` matches the password in the dictionary. Otherwise, it should return `False`.
# 
# * Verify that your function works by calling it with the username "alice" and the password "chinchilla".
# * Verify that your function works by calling it with the username "alice" and the password "Chinchilla".
# * Verify that your function works by calling it with the username "bobby" and the password "123456".
# 
# Again, use comments to explain what you expect to see in the output of your function from previous three applications of your function.
# 
# To get you started, here is a little helper function that will return `True` if a key is in a dictionary and `False` otherwise.

# %%
users = {
    "alice": "chinchilla", 
    "bob": "123456", 
    "charlie": "password"
}
    
def key_in_dict(key, d):
    if key in users and users[key] == d:
        return True
    else:
        return False
    return key in d

print(key_in_dict("alice", "chinchilla"))
print(key_in_dict("alice", "Chinchilla"))
print(key_in_dict("bobby", "123456"))

# %% [markdown]
# Note: think about how you can use `if` statements to help you (or ask the AI assistant for help).
# 
# 
# ### Q1.d
# 
# Generally, we wouldn't want to keep strings as plain text. A frequent strategy is to use a [crypographic hash function](https://en.wikipedia.org/wiki/Cryptographic_hash_function) to make the plain text password unreadable. A hashing function will replace the input with a different string or number. It is very difficult to go backwards from the hashed value to the original string, but every time we hash, we get the same value.
# 
# Use the `hash2` function on the password. Demonstrate that each time we use it we get the same value by calling it twice (remember that only the last line of a cell will print out). You answer should have an explicit `True` value as the output.

# %%
import hashlib

# define the hash2 function
def hash2(x):
  return hashlib.sha256(x.encode('utf-8')).hexdigest()

# hash the password twice
password = 'my_secure_password'
hash1 = hash2(password)
hash2_value = hash2(password)

# check if the two hash values are identical
hash1 == hash2_value
  

# %% [markdown]
# ### Q1.e
# 
# If a list of passwords were stolen, the malicious actors might be able to undo the hashing by guessing common words. This called a dictionary attack, as each word (and often combinations of common words and other characters) is hashed and then compared to the stolen list of passwords to see if it is present.
# 

# %%
hash("wolverine")

# %%
stolen_password = 'b00ef262afae566b51f740124a6b12d982a2cff1bbf2ab5632cb548e98da6feb'
hash(stolen_password)

# %% [markdown]
# Hash the following three words to see if one of them is the stolen password. Use `==` to evaluate if the hashed version is the same as the stolen password hash. Use a for loop or list comprehension to avoid repeating yourself. Can we guess the password?
# 
# * badger
# * wolverine
# * jaguar

# %%
passwords = {"badger", "wolverine", "jaguar"}

for animal in passwords: 
    hashed_password = hash(animal)
    print(hashed_password)
    hash_stolen_password = hash(stolen_password)
    print(hash_stolen_password)
    if hashed_password == stolen_password:
        print(hashed_password)

# none of the hashed passwords match the stolen password hash
    

# %% [markdown]
# ### Q1.f
# 
# A better way to protect passwords is to add a "salt" to all user's passwords on a given site. The salt is a secret string that is prepended to each password *before* hashing.
# 
# Complete the function below that combines the `salt` with the supplied `password` to strengthen it. Demonstrate that just hashing the correct password is insufficient to guess the password if you do not know the salt as well (again use `==`).

# %%
def salted_hash(password):
  salt = "zoology"
  salted_password = salt + password
  hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()
  return hashed_password # replace 0 with the salted hash

# compute the salted and hashed version of the password "cardinal"
hashed_with_salt = salted_hash("cardinal")
print(f"Salted hash of 'cardinal': {hashed_with_salt}")

# demonstrate that we cannot guess without the salt.
hashed_without_salt = hashlib.sha256("cardinal".encode()).hexdigest()
print(f"Hash of 'cardinal' without salt: {hashed_without_salt}")

print(f"Hashes match: {hashed_with_salt == hashed_without_salt}")

# %% [markdown]
# ## Question 2
# 
# ### Q2.a
# 
# Run the code in the following cell. What does the `%` operator do?

# %%
[3 % 2, 4 % 2, 5 % 2]

# %% [markdown]
# The code in the cell outputs the remainder of each arithmetic operation in the list. The % operator is called modulo, and it returns the remainder of each division problem. 

# %% [markdown]
# ### Q2.b
# 
# Complete the following function that will compute if an input is even or odd:

# %%
def is_odd(num):
    if num % 2 == 0:
        return False
    else: 
        return True

# %%
is_odd(16) # Should return False

# %%
is_odd(17) # Should return True

# %% [markdown]
# ### Q2.c
# 
# Here is some input data:

# %%
some_numbers = [91, 88, 38, 103, 199372, 3, 4945, 20098]

# %% [markdown]
# Write a **for loop** to select just the odd numbers of `some_numbers`. Make sure to use your function from part (b). Print out your result.

# %%
# create an empty list to store odd numbers
odd_numbers = []

# write a for loop to and use the function from part b
for number in some_numbers: 
    if is_odd(number):
        odd_numbers.append(number)

# print result
print(odd_numbers)

# %% [markdown]
# ### Q2d
# 
# Using a **list comprehension** select just the odd elements of `some_numbers`, convert them to strings (using the `str` function), and then `hash2` them. **Do not** use any results from part (c) in your solution.

# %%
hashed_odds = [hash2(str(num)) for num in some_numbers if num % 2 != 0]
print(hashed_odds)

# %% [markdown]
# ### Q2e
# 
# For a particular website, suppose users could only choose positive, whole numbers as passwords, and the site neglected use salting to make the numbers harder to guess.
# 
# Here is an example stolen value.

# %%
hash(str(206))

# %%
hashed_number = '5cf4e26bd3d87da5e03f80a43a64f1220a1f4ba9e1d6348caea83c06353c3f39'

# %% [markdown]
# Carry out a dictionary attach by implementing the following:
# 
# * Write a function that takes a number as an input, and returns True if that number (after being coverted to a string) hashes to the `hashed_number` value.
# * Use this function to find out if value in 0 to 100000 was the password. (Hint: use the `range(a, b)` function which gives back a sequence of values from a to (b - 1)).
# 

# %%
# placeholder comment
def is_password(number, hashed_number):
    number_string = str(number) 
    hashed_value = hash2(number_string)
    return hashed_value == hashed_number

for num in range(0, 100001):
    if is_password(num, hashed_number):
        print(f"Password found: {num}")
        break
    else: 
        print("Password not found in the given range.")


