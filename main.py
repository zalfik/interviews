# Caesar Cipher

import string

your_text = 'lets write some text'
shift = 5


def ceasar_cipher(text, shift):
    alphabet = string.ascii_lowercase
    mask = alphabet[shift:] + alphabet[:shift]
    shifter = str.maketrans(alphabet, mask)
    text = text.translate(shifter)
    return text

print(ceasar_cipher(your_text, shift))


# Palindrome

def palindrome(text):
    text = text[::-1]
    return text


print(palindrome(your_text))


# Fibonacci

your_number = 10

def Fibonacci(number):
    if number == 0:
        return number
    if number == 1:
        return number
    prev = 0
    next = 1
    print(prev, next, end=' ')
    for _ in range(2, number):
        tmp = prev + next
        print(tmp, end=' ')
        prev = next
        next = tmp

Fibonacci(your_number)
print('')

# Binary string to decimal

your_bin = '11001101'


def Bintodec(text):
    text_int = int(text)
    exp, decimal = 0, 0
    while text_int != 0:
        decimal = decimal + (text_int%10)*(2**exp)
        text_int = text_int//10
        exp += 1
    return decimal

print(Bintodec(your_bin))

# How to check that tuple A contains all elements of tuple B. Do both tuples contain unique values? 


tup_a = (1, 1, 5, 7, 9, 9, 11)
tup_b = (1, 5, 7, 11)

def tuple_containment(first, second):
    if all(element in second for element in first):
        print('{} contains all elements of {}'.format(second, first))
    if all(element in first for element in second):
        print('{} contains all elements of {}'.format(first, second))


tuple_containment(tup_a, tup_b)


def tuple_distinc(tup):
    return len(set(tup)) == len(tup)


print(tuple_distinc(tup_b))


# Write a function that returns a string of numbers from 0 to 100, "0123456789101112...".


def string_numbers(number):
    text = ''
    for num in range(number+1):
        text = text+str(num)
    return(text)

print(string_numbers(100))


# FizzBuzz

def fizzbuzz(number):
    for num in range(1,number+1):
        if num % 15 == 0:
            print('FizzBuzz', end=' ')
            continue
        if num % 3 == 0:
            print('Fizz', end=' ')
            continue
        if num % 5 == 0:
            print('Buzz', end=' ')
            continue
        print(num, end=' ')

print(fizzbuzz(20))