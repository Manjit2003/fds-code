def frequency_words(line):
    freq = {}
    list1 = line.split(" ") 
    for item in list1:
        if item not in freq.keys() : 
            freq[item] = 1 
        else : 
            freq[item] = (freq[item] + 1)
    print(freq)

def longest_word(line):
     longest_word_list = line.split(' ') 
     longest_word = longest_word_list[0]

     for a in longest_word_list:
        if len(longest_word) < len(a) :
             longest_word = a
     print(f'longest word in line is {longest_word} ')

def frequency(line, c): 
    list1 = []
    count = 0
    for a in line:
        list1.append(a) 
    for item in list1:
        if item == c : 
            count += 1
    print(f'the character {c} has been appeared {count} times')

def palindrome(line):
    if line == line[::-1] :
         print("string is palindrome") 
    else : 
        print("string is not palindrome")


line = input('Enter the sentence :')
longest_word(line)
frequency(line, 'o') 
palindrome(line) 
frequency_words(line)