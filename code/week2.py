# Task 1: Sum of Integers in a List
user_input = input("Enter a list of integers separated by spaces: ")
numbers = list(map(int, user_input.split()))
sum_of_integers = sum(numbers)
print("Sum of integers in the list:", sum_of_integers)


# Task 2: Printing Favorite Books
favorite_books = ("Book1", "Book2", "Book3", "Book4", "Book5")
for book in favorite_books:
    print(book)


# Task 3: Storing Person Information in a Dictionary
person = {}
person["name"] = input("Enter your name: ")
person["age"] = input("Enter your age: ")
person["favorite_color"] = input("Enter your favorite color: ")
print("Person Information:", person)


# Task 4: Finding Common Elements in Sets
set1 = set(map(int, input("Enter elements for Set 1: ").split()))
set2 = set(map(int, input("Enter elements for Set 2: ").split()))
common_elements = set1.intersection(set2)
print("Common elements in the sets:", common_elements)

# Task 5: Filtering Words with Odd Number of Characters
words = ["apple", "banana", "cherry", "date", "elderberry"]
odd_length_words = [word for word in words if len(word) % 2 != 0]
print("Words with odd number of characters:", odd_length_words)
