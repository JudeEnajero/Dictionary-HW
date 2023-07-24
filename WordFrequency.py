def count_word_frequency(file_path):
    word_frequency = {}
    
    with open(file_path, 'r') as file:
        for line in file:
        
            words = line.strip().split()
            
            
            for word in words:
                
                word = word.strip('.,!?:"()')
                word = word.lower()
                
                if word:
                    if word in word_frequency:
                        word_frequency[word] += 1
                    else:
                        word_frequency[word] = 1
                        
    return word_frequency

def display_word_frequency(word_frequency):
    print("Word frequency:")
    for word, frequency in word_frequency.items():
        print(f"{word}: {frequency}")

if __name__ == "__main__":
    file_path = "sometext.txt"
    word_frequency = count_word_frequency(file_path)
    display_word_frequency(word_frequency)