**Q1. What is a data type? Why is it important in Python?**

Definition: A data type is a classification that tells the computer how to interpret and manipulate a specific piece of data.
Importance: It is crucial because it determines what operations can be performed on that data (e.g., you can add two integers, but you can’t subtract a string from an integer). In Python, everything is an object, and data types help manage memory and ensure code runs efficiently.

**Q2. Explain the difference between int and float with examples.**

int (Integer): Represents whole numbers without decimals.
Example: x = 10, y = -5
float (Floating-point): Represents real numbers that contain a decimal point.
Example: pi = 3.14, price = 99.99

**Q3. What is a string? Is it mutable or immutable? Explain.**

String: A sequence of characters enclosed in single (' '), double (" "), or triple quotes.
Mutability: Strings are immutable.
Explanation: Once a string is created, its individual characters cannot be changed. If you try to change one letter (e.g., s[0] = 'A'), Python will throw an error. You must create a new string if you want a modified version.

**Q4. What is Boolean data type? Give real-life examples.**

Boolean: A data type that has one of two possible values: True or False.
Real-life Examples:
Light Switch: Is the light on? (True/False)
Login Status: Is the user logged in? (True/False)
Attendance: Is the student present? (True/False)

**Q5. Define mutable and immutable data types with examples.**

Mutable: Data types whose values can be changed after they are created.
Examples: List, Dictionary, Set.
Immutable: Data types whose values cannot be changed after they are created.
Examples: Int, Float, String, Tuple.

**Q6. What is a list? Write any 4 properties of list.**

Definition: A list is an ordered collection of items that can be of different data types.
Properties:
Ordered: Elements maintain their specific order of insertion.
Mutable: You can add, remove, or change items.
Heterogeneous: Can store different types (int, string, etc.) together.
Duplicates allowed: You can have the same value multiple times.

**Q7. Explain indexing and slicing in list with example.**

Indexing: Accessing a single element using its position (starts at 0).
Example: If L = [10, 20, 30], L[0] is 10.
Slicing: Accessing a range of elements using the syntax [start:stop].
Example: If L = [1, 2, 3, 4, 5], L[1:4] returns [2, 3, 4].

**Q8. Difference between append() and insert() method.**

append(item): Adds the item to the very end of the list.
insert(index, item): Adds the item at a specific position (index) and shifts the following items to the right.

**Q9. What is a set? Why duplicates are not allowed in set?**

Set: An unordered collection of unique elements.
Why no duplicates? Sets are based on a mathematical concept where an item is either in the collection or it isn't. Python uses "hashing" to store set elements; since each hash must be unique to find the item quickly, duplicates are automatically removed.

**Q10. Explain union and intersection of sets with example.**

Union (|): Combines all unique elements from both sets.
Example: {1, 2} | {2, 3} → {1, 2, 3}
Intersection (&): Keeps only the elements that are present in both sets.
Example: {1, 2} & {2, 3} → {2}

**Q11. What is a dictionary? Explain key-value pair concept.**

Dictionary: An unordered, mutable collection of data stored as pairs.
Key-Value Concept: Every "Value" (the data) is associated with a unique "Key" (the label). You use the key to look up the value, similar to how you use a word to look up a definition in a real dictionary.
Example: {"name": "Alice"} — "name" is the key, "Alice" is the value.

**Q12. Difference between list and set.**

Feature	List	Set
Order	Ordered	Unordered
Duplicates	Allowed	Not Allowed
Indexing	Supported (L[0])	Not Supported

**Q13. Difference between set and dictionary.**

Feature	Set	Dictionary
Structure	Collection of unique values	Collection of key-value pairs
Syntax	{1, 2, 3}	{"a": 1, "b": 2}
Access	By value	By key

**Q14. What is the difference between remove() and pop() in list?**

remove(value): Deletes the first occurrence of a specific value. (e.g., L.remove(10))
pop(index): Deletes and returns the element at a specific index. If no index is given, it removes the last item.

**Q15. Can dictionary keys be duplicated? Explain.**

Answer: No, dictionary keys cannot be duplicated.
Explanation: Keys must be unique because they act as the identifier for the value. If you try to assign a value to an existing key, Python will simply overwrite the old value with the new one. However, values within a dictionary can be duplicated.