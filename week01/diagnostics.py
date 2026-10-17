#1. Print the numbers 1-20, but "Fizz" for multiples of 3, "Buzz" for multiples of 5 and "FizzBuzz" for multiples of both.
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
#2. Write is_palindrome(s) that ignores case and spaces ("Anna" → True, "Never odd or even" → True).

#3. Given nums = [3, 4, 7, 10, 12], build a new list that contains only the even numbers, squared.

#4. Count how often each word appears in "the cat and the hat and the bat" and store the result in a dict.

#5. Ask the user for a number with input(). If they type something that isn't a number, print an error instead of crashing.

#6. Write a function that returns (smallest, largest, average) of a list without using min, max or sum.

#7. Predict the output, then run it: a = [1, 2, 3]; b = a; b.append(4); print(a)

#8. Write three lines to test.txt, then read the file and print how many lines it has.

#9. Write a class Rectangle with width, height and a method area().

#10. What does "192.168.1.10".split(".") return? Turn it into a list of integers.
