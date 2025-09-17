import re
import os

def clear(): #! this is just to clear the terminal output for cleaner visual like in c++.
    # Windows
    if os.name == 'nt':
        os.system('cls')
    # macOS/Linux
    else:
        os.system('clear')

summary_report = {
    "count_words": [],   
    "count_sentences": [],   
    "emails_found": [],      
    "numbers_found": [],     
    "replacements": [],     
    "palindrome_checks": [] 
}

def count_words(text):
    format_text = str(text).lower().title()
    cleaned_text = re.sub(r"[,.!#$%^&*90@\d/?';:{}\-+=_]", "", format_text)
    split_text = str(cleaned_text).split()
    count_text = len(split_text)
    print(f"[!] Words: {cleaned_text}\n[!] Count: {count_text}")
    
    return count_text

def count_sentences(text):
    sentences = re.split(r'[.!?]', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    print(f"Number of sentence(s): {len(sentences)}")

    return len(sentences)

def findall_email_address(line):
    match = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', line)
    if match:
        print(f"[!] Email/s found: {match}")
    else:
        print(f"[!] Email/s found: NONE")
        
    return match

def findall_numbers(line):
    match = re.findall(r"\d", line)
    
    if match:
        print(f"[!] Number/s found: {match}")
    else:
        print(f"[!] Number/s found: NONE")
        
    return match

def replace_word(original, replacement):
    rep = original.replace(original, replacement)
    
    print(f"[!] Word replaced\t\t: {rep}")
    
    return rep

def palindrome(text):
        isPalindrome = text == text[::-1]
        if isPalindrome:
            print(f"\"{text}\" is a Palindrome!")
        else:
            print(f"\"{text}\" is not a Palindrome!")
            
        return isPalindrome

option_list = []
while True:
    try:
        print("--------------------------------------------------")
        opt = str("[TEXT ANALYZER]").center(50)
        print(opt)
        print("[1] Count words\n[2] Count sentences\n[3] Find emails\n[4] Find numbers")
        print("[5] Replace a word\n[6] Check Palindrome\n[7] Quit")
        print("--------------------------------------------------")
        option = int(input("[?] Choice: "))
        option_list.append(option)
        
        if option == 1: #! Count words condition
            clear()
            print()
            option = None
            
            print("--------------------------------------------------")
            opt = str("OPTION 1").center(50)
            print(opt)
            print("--------------------------------------------------")
            
            user_text = input("Enter a text: ")

            result = count_words(user_text)
            summary_report["count_words"].append(result)
            
            while True:
                x = input("\n[!] Press Q to quit: ")
                if x.lower() == 'q':
                    clear()
                    break
                else:
                    print("[!] Invalid input. Please try again!")
            
            print()
                
        elif option == 2: #! Count sentences condition
            clear()
            print()
            option = None
            
            print("--------------------------------------------------")
            opt = str("OPTION 2").center(50)
            print(opt)
            print("--------------------------------------------------")
        
            user_text = input("Enter a text: ")
            if user_text.endswith("."):
                result = count_sentences(user_text)
                summary_report["count_sentences"].append(result)
            else:
                print("[!] Please end your sentence with a period.")

            while True:
                x = input("\n[!] Press Q to quit: ")
                if x.lower() == 'q':
                    clear()
                    break
                else:
                    print("[!] Invalid input. Please try again!")

            print()
            
        elif option == 3: #! Find emails condition
            clear()
            print()
            option = None
            
            print("--------------------------------------------------")
            opt = str("OPTION 3").center(50)
            print(opt)
            print("--------------------------------------------------")
        
            user_text = input("Enter a text including an email: ")
            result = findall_email_address(user_text)
            summary_report["emails_found"].append(result)

            while True:
                x = input("\n[!] Press Q to quit: ")
                if x.lower() == 'q':
                    clear()
                    break
                else:
                    print("[!] Invalid input. Please try again!")

            print()
            
        elif option == 4: #! Find numbers condition
            clear()
            print()
            option = None
            
            print("--------------------------------------------------")
            opt = str("OPTION 4").center(50)
            print(opt)
            print("--------------------------------------------------")
        
            user_text = input("Enter a text including a number: ")
            result = findall_numbers(user_text)
            summary_report["numbers_found"].append(result)
            
            while True:
                x = input("\n[!] Press Q to quit: ")
                if x.lower() == 'q':
                    clear()
                    break
                else:
                    print("[!] Invalid input. Please try again!")

            print()
                
        elif option == 5: #! Replace a word condition
            clear()
            print()
            option = None
            
            print("--------------------------------------------------")
            opt = str("OPTION 5").center(50)
            print(opt)
            print("--------------------------------------------------")
                    
            while True:
                original_text = input("[!] Enter your text\t\t: ")
                text_replacement = input("[!] Replace your text with\t: ")
                if original_text != "" and text_replacement != "":
                    result = replace_word(original_text, text_replacement)
                    summary_report["replacements"].append(result)
                    break
                else:
                    print("[!] Invalid input. Don't leave empty spaces!")
            
            while True:
                x = input("\n[!] Press Q to quit: ")
                if x.lower() == 'q':
                    clear()
                    break
                else:
                    print("[!] Invalid input. Please try again!")

            print()
        
        elif option == 6:
            clear()
            print()
            option = None
            
            print("--------------------------------------------------")
            opt = str("OPTION 6").center(50)
            print(opt)
            print("--------------------------------------------------")
            
            while True:
                user_text = input("Enter a word: ")
                format_text = str(user_text).lower()
                cleaned_text = re.sub(r"[,.!#$%^&*90@\d/?';:{}\-+=_]", "", format_text)
                check_words = cleaned_text.split()
                length_of_words = len(check_words)
                
                if length_of_words == 1:
                    result = palindrome(cleaned_text)
                    summary_report["palindrome_checks"].append(result)
                    break
                else:
                    print("[!] One word only.")
                    
            while True:
                x = input("\n[!] Press Q to quit: ")
                if x.lower() == 'q':
                    clear()
                    break
                else:
                    print("[!] Invalid input. Please try again!")

            print()
                
        elif option == 7: #! Quit condition
            clear()
            
            print("--------------------------------------------------")
            title = str("[TEXT ANALYZER]").center(50)
            print(title)
            print("--------------------------------------------------")
            number_of_options = 6
            option_names = {
                1: "Count words",
                2: "Count sentences",
                3: "Find emails",
                4: "Find numbers",
                5: "Replace word",
                6: "Check palindrome"
            }
            for i in range(1, number_of_options + 1):
                count_options_used = option_list.count(i)
                if count_options_used != 0:
                    print(f"[-] '{option_names[i]}' has been used '{count_options_used}' times.")
            print()
            
            print("--------------------------------------------------")
            title = str("[SUMMARY REPORT]").center(50)
            print(title)
            print("--------------------------------------------------")
            for key, value in summary_report.items():
                if value:
                    print(f"[-] {key} -> {value}")

            option_list.clear()
            print()
            break
        
    except:
        clear()
        print(" Invalid input.")