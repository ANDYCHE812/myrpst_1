import os
from sys import stdin
from re import sub, split
import pickle
import random


class TextGenerator:
    def __init__(self):
        self.words_dict = {}

    def generate_text(self, length, start_word=None):
        """
        makes the sequence of words
        """
        if start_word == None:
            start_word = random.choice(list(self.words_dict.keys()))
        text = start_word[0:1].upper() + start_word[1:]
        length -= 1
        last_word = start_word
        while length > 0:
            if last_word in self.words_dict.keys():
                current_word = random.choice(self.words_dict[last_word])
                text += ' ' + current_word
                last_word = current_word
                length -= 1
            else:
                break
        return text
        
    def save_model(self, model_path):
        """
        saves the model at "model_path"
        """
        with open(model_path, 'wb') as f:
            pickle.dump(self.words_dict, f, pickle.HIGHEST_PROTOCOL)

    def load_model(self, model_name):
        """
        loads the model from "model_name" file
        """
        with open(model_name, 'rb') as f:
            self.words_dict = pickle.load(f)

    def text_processing(self, text):
        """
        saves all words in a dict of lists
        """
        sentence_list = split('\. |\? |! |\.\.\. |\—', sub('[\n:;\-\t,]', ' ', text))   # splitting text by sentences and deleting punctuation marks
        for sentence in sentence_list:
            words = sentence.split()
            last_word = ''
            for word in words:
                if last_word != '':
                    if last_word in self.words_dict:
                        self.words_dict[last_word].append(word)
                    else:
                        self.words_dict[last_word] = [word]
                else:
                    word.lower()    # making the first word of each sentence lowercased, others supposed to be proper nouns
                last_word = word

    def train(self, path=None):
        """
        searches for text files at 'path' and reads it
        """
        if path != None:
            for file in os.listdir(path):
                if file.endswith('.txt'):
                    with open(os.path.join(path, file), encoding='utf-8') as f:
                        text = f.read()
                        self.text_processing(text)
        else:   # if there is no path to files, text is read from stdin
            text = ''
            for s in stdin:
                text += s
                self.text_processing(text)
