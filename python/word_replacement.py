#========== Word Replacement ==========# 

def replace_word():

    string = "I wonder how, I wonder why, yesterday you told me about the blue blue sky."
    word_to_replace = input("Enter the word to replace: ")
    word_replacement = input("Enter the word replacement: ")
    print(string.replace(word_to_replace, word_replacement.upper())) 

##### Code Execution #####
if __name__ == "__main__":
    replace_word()
