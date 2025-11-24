# Codebreaker
User attempts to guess a 4 digit code made by the computer

We create a random list of 4 digit numbers. Then we ask the user to guess it and, using the for loop, we traverse their guess to determine what's right, what's misplaced and what's wrong. We first establish that if everything is right then we stop there but, if it isn't, we check each digit to see if they are in the right place using the while loop. We create two lists code_used and guess_used and set them to True for that specific index. Then we increment y. When the loop is done, we then focus on the parts which weren't exactly right. We check 4 times as there are 4 digits and say that if the value at the index of guess_used is False then we check if the value at index j is False AND that the digit at index i is the same as the digit at index j. If so it will say it is misplaced, and code_used[j] becomes to True to say that the digit exists within the code but at a different index so any other digits guessed can never be in the index of the already guessed value (as it is marked True so is skipped in the for loop) else it is not in the code at all. Then, after 5 tries, the code is revealed.

• Uses Python string manipulation, loops, and conditionals to analyse and process encoded text.
• Applies logical reasoning and algorithmic thinking to test and refine possible decryption paths.
• Demonstrates modular program structure through functions that handle different stages of the codebreaking process.
