import json
# Load JSON file properly as dictionary
with open("Words.json", "r", encoding="utf-8") as f:
    translations_dict = json.load(f)

CYAN = "\33[36m"
BLUE_BG = "\33[104m"
GREEN = "\33[32m"
RESET = "\33[0m"

print(f"{BLUE_BG}          English to Hindi And Chinese Translator          {RESET}")

def translate_word(word, language):
    word = word.lower()
    if word in translations_dict:
        return translations_dict[word].get(language, "Translation not available for this language.")
    else:
        return f"❌ Sorry, the word '{word}' is not in the dictionary."

def main():
    while True:
        language_choice = input("[1] Hindi\n[2] Chinese\nType 'add' to add new words or 'exit' to quit: ").strip().lower()

        if language_choice == "exit":
            break

        elif "add" in language_choice:
            print(f"{CYAN}Add New Word{RESET}")
            # reading the json file
            with open("Words.json", "r", encoding='utf-8') as f:
                data = json.load(f)
            
             # getting words
            eng_word = input("Enter the English Word: ").capitalize()
            hindi_word = input(f"Enter {eng_word} In Hindi: ").capitalize()
            zhongwen_word = input(f"Enter {eng_word} In Chinese: ").capitalize()
            
            # getting word prononciation
            hindi_word_pronounciation = input(f"Enter the Hindi Word {hindi_word} Pronounciation: ").capitalize() 
            zhongwen_word_pronounciation = input(f"Enter the Chinese Word {zhongwen_word} Pronounciation: ").capitalize()
            
            # full word with pronounciation
            hindi_word = f"{zhongwen_word} ({hindi_word_pronounciation})"
            zhongwen_word = f"{zhongwen_word} ({zhongwen_word_pronounciation})"
            
            # making structure of the words data
            data[eng_word] = {
                "Hindi": hindi_word,
                "Chinese (Simplified)": zhongwen_word
            }
            # dump the data in json file
            with open("Words.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print(f"{GREEN}The Word Added Successfully!{RESET}")
            exit()
        
        elif language_choice == "1" or "hindi" in language_choice:
            language = "Hindi"
        
        elif language_choice == "2" or "chinese" in language_choice:
            language = "Chinese (Simplified)"
        
        else:
            print("Invalid language choice, please choose either 'Hindi' or 'Chinese'.")
            continue

        word = input("Enter an English word to translate: ").strip()
        translation = translate_word(word, language)
        print(f"\n{GREEN}Translation in {language}: {translation}{RESET}\n")

if __name__ == "__main__":
    main()
