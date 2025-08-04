# -*- coding: utf-8 -*-
"""
Created on Mon Aug  4 23:32:34 2025

@author: HP
"""

def analyze_name(full_name):
    name = full_name.replace(" ", "").lower()
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"

    vowel_count = sum(1 for char in name if char in vowels)
    consonant_count = sum(1 for char in name if char in consonants)
    print(f"Vowels: {vowel_count}, Consonants: {consonant_count}")

    print("ASCII values:")
    for char in full_name:
        print(f"{char} : {ord(char)}")

    reversed_name = full_name[::-1]
    print(f"Reversed name: {reversed_name}")

    if name == name[::-1]:
        print("Your name is a palindrome.")
    else:
        print("Your name is not a palindrome.")

    unique_letters = sorted(set(name))
    print(f"Unique letters sorted: {unique_letters}")

    for char in name:
        if name.count(char) == 1:
            print(f"First non-repeating character: {char}")
            break
    else:
        print("No non-repeating character found.")

if __name__ == "__main__":
    analyze_name("Sheikh Saadi")  
