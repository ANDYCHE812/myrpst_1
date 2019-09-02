the task on programming "language model" ("языковая модель")
=========================================

it is an utility program, which generates its own texts based on the texts given.
bigram language model is used: for each word it creates a list of words, that can be placed after it.

Features
--------

- Russian version of the book called 'The Life and Strange Surprizing Adventures of Robinson Crusoe ...' 
(originally written by Daniel Defoe) was used for so-called training my 'model.pkl' (also posted it)
- Python 3.x.x
- Some comments in the source code that would probably make it clear to you
- It tries to do it properly:)

Installation
------------

0) just copy and paste all the files.

for running it:

1) type in terminal: 'python train.py --input-dir 'path_to_text_files' --model your_model_name.pkl'
it will run 'train.py'. at 'path_to_text_files' there should be at least 1 '*.txt' file. it will be used for 'training'
'your_model_name.pkl'

2) type in terminal: 'python generate.py --model your_model_name.pkl --seed your_word --length 17'
it will run 'generate.py'. '--model' argument expects to get the string with your_model_name.pkl.
'--seed', which is an optional argument, expects to get a word, You'd like to get your sequence starting with (None by default).
'length' argument expects to get an integer value with the length of a result sequence, for eg. , now it equals to 17
(equals 1 by default).

Also, You have no need to run 'TextGenerator.py' at all. Once it is run separately, it will do nothing special.

Support
-------

If you are having issues, please let me know:
andrew_che@protonmail.com
