# Project Name : Student Grade Management System

## Table of Contents
- [Overview](#overview)
- [Problem ](#problem)
- [Solution](#solution)
- [Features](#features)
- [Program ](#explained)
- [Github  ](#versioncontrol)

---

## Overview
Manually analyzing text for word counts, sentences, email extraction, or palindrome detection can be:
    * Time-consuming when working with longer text.
    * Error-prone when searching for patterns like emails or numbers.
    * Inconsistent if repeated multiple times.
    * A clear, automated solution reduces workload and ensures accuracy in text analysis.

---

## Problem
Teachers often handle multiple students and subjects at once. Doing calculations manually can be:
    * Time-consuming when computing averages.
    * Error-prone when assigning letter grades and GPAs.
    * Inconsistent in determining pass/fail results.
    * A clear, automated solution reduces workload and increases accuracy.

---

## Solution
Solution
    * The solution is a Python-based Text Analyzer that:
    * Accepts user input from the terminal.
    * Applies regex-based text processing for accurate pattern detection.
    * Performs common text-processing tasks quickly.
    * Keeps track of results in a structured summary report.
    * Provides an easy-to-use interactive menu for navigation.

---

## Features
    * Word Counter: Counts and displays words in the text.
    * Sentence Counter: Detects and counts sentences.
    * Email Extractor: Finds and lists all email addresses in the text.
    * Number Extractor: Detects and lists all numbers in the text.
    * Word Replacement: Replaces a given word with another.
    * Palindrome Check: Verifies whether a given word is a palindrome.
    * Summary Report: Logs and displays a report of all actions performed in one session.
    * User-Friendly Menu: Options are presented clearly with error handling for invalid input.

---

## Program
    * count_words(text)
        - Cleans and counts words in the input.
        - Stores the result in the summary report.
    * count_sentences(text)
        - Splits text into sentences and counts them.
    * findall_email_address(line)
        - Uses regex to extract all email addresses.
    * findall_numbers(line)
        - Extracts numbers from the text.
    * replace_word(original, replacement)
        - Replaces a given word with a replacement string.
    * palindrome(text)
        - Checks if a given word is a palindrome.
    * Menu System (loop)
        - Presents options 1–7 (Word count, Sentence count, Email search, Number search, Replace word, Palindrome check, Quit).
        - enerates a final summary report when quitting.

## Github
The progress of this project is documented in my Python coursework:
    * Final Verion:  
        https://github.com/sudo-stanly/Python-coursework/blob/main/Advanced%20studies/projects/project%201.py
    
    * Fixes:  
        https://github.com/sudo-stanly/Python-coursework/commit/2368098c2bf6b92dbac208e714766545e8c11345
        https://github.com/sudo-stanly/Python-coursework/commit/feb82fdedbb0f2500ce5d9f17ae506ddbb673b46
    
    * Earlier Progress:  
        https://github.com/sudo-stanly/Python-coursework/commit/b97d13022afa16622bf859e8fe75b5abbaceef68
        https://github.com/sudo-stanly/Python-coursework/commit/3aaa4d2f3c01d2925f299620c0dc37bfabbd4b34