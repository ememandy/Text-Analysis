#Purpose of Program: Text analysis and the statistical distribution of words 
#Author: Emem-Akeabasi Etop Andy
#Date: 10th March, 2021
#Copyright: (c)Emem Andy 2021

import re

class Books:
    username = input("Enter a username: ") #asks the user for a username 
    novel_name = input("Enter the name of the novel: ") #asks the name of the novel    

    def __init__(self, username, novel_name):
        self.username = username
        self.novel_name
        
class Novels(Books):
    
    
    def __init__(self, username, novel_name, novel_path, process_file, my_novel, clean_words, words, novel_characters, chr_length,
    blank_spaces, blank_length, blank_space_percent, word_counts, dict_key, total_word_count, output_file, f):
        Books.__init__(self, username, novel_name)
        self.novel_path = novel_path
        self.process_file = process_file
        self.my_novel = my_novel
        self.clean_words = clean_words
        self.words = words 
        self.novel_characters = novel_characters
        self.chr_length = chr_length
        self.blank_spaces = blank_spaces
        self.blank_length = blank_length
        self.blank_space_percent = blank_space_percent
        self.word_counts = word_counts
        self.dict_key = dict_key
        self.total_word_count = total_word_count
        self.output_file = output_file
        self.f = f
    
    
    @classmethod
    #Method for getting the file path from user 
    def get_user_input(self):
        
        while True:
            try:
                
                self.novel_path = input("Enter the full path of the file (use backslash, q/Q to quit): ")
                if self.novel_path == 'q' or self.novel_path == 'Q':
                    break
                else:
                    open(self.novel_path) 

            except FileNotFoundError:
                print("File does not exist!")
                continue

            else:
                print("We found your txt file!!") #success message for correct file path
                self.process_file = input("Would you like to process this file or not (y/n): ")
                if self.process_file == 'y':
                    self.read_novel(self.novel_path) #makes a call to the function that handles the processing
                else:
                    break
            
            return self.novel_path

    @classmethod
    #Method for processing novels
    def read_novel(self, book_path):
        self.novel_path = book_path #passes the argument book_path to the self.novel_path attribute
        
        
        with open(self.novel_path, 'r') as self.my_novel: #this is to open the file
            self.my_novel.seek(0) #seek to the start of the file
            self.my_novel = self.my_novel.read().replace("\n", " ").replace("\r", " ").replace("'", "") #replaces each new line, single quote with nothing

            self.clean_words = re.sub(r"[^a-zA-Z]+", " ", self.my_novel)  #this takes out all the special characters  
            self.words = re.split(r"\W", self.clean_words) #returns each word in the file 
            

            self.novel_characters = re.findall(r"\w", self.my_novel) #return each character in the file 
            self.chr_length = len(self.novel_characters) #total number of characters
                
            self.blank_spaces = re.findall(r"\s", self.my_novel) #returns each blank space in the txt file
            self.blank_length = len(self.blank_spaces) #total number of blank spaces
            
            self.blank_space_percent = (self.blank_length/self.chr_length) * 100 #calculation of percentage of blank spaces
            
            self.word_counts = dict()

            #for loop, loops through to increment the occurence of each word
            for word in self.words:
                if word in self.word_counts:
                    self.word_counts[word] += 1
                else:
                    self.word_counts[word] = 1
            
            self.dict_key = self.word_counts.keys() #this gets the keys of the dictionary
            self.total_word_count = len(self.dict_key) #counts the number of words that are in the dictionary
            
            print("Processing Done!!")
            
            try:
                #this populates the output file with the necessary and correct information
                with open(f"{self.username}-PartA-{self.novel_name}Analysis.txt", "w+") as self.output_file:
                    self.output_file.write(f"\nName of text: {self.novel_name}\n")
                    self.output_file.write(f"\nTotal Non-blank Character Count: {self.chr_length}\n")
                    self.output_file.write(f"\nTotal Blank Character Count: {self.blank_length}\n")
                    self.output_file.write(f"\nPercentage Blank Character: {self.blank_space_percent:{5}.{3}}\n")
                    self.output_file.write(f"\nTotal Word Count: {self.total_word_count}\n") 
                    self.output_file.write("\nWord, Count:")
                    for key, value in self.word_counts.items(): #for loop to get the key,value of the dictionary items
                        self.output_file.write(f"\n{key}: {value} ") 
                    self.output_file.close()

                #prints the name and location of the output file
                print(f"File Name: {self.output_file.name}")
                print(f"File Location: Current Working Directory")
            
            #handles output file error 
            except IOError:
                with open(self.output_file, 'a') as self.f:
                    self.f.write("ERROR: Unable to write to file!")
        return 0

n = Novels.get_user_input()
