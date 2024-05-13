# Word Counter

def count_words(text):
    words = text.split()
    return len(words)

def main():
    with open('C:/Users/malhi/OneDrive/Desktop/Git Demo/100-days-of-code/day-002/sample_text.txt', 'r') as file:
        text = file.read()
        word_count = count_words(text)
        print(f"Number of words in the text: {word_count}")

if __name__ == "__main__":
    main()
