#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import string


def is_word_guessed(secret_word,letters_guessed):
     for i in secret_word:
        if i in letters_guessed:
            return True
        else:
            return False
        
        
        
def get_guessed_word(secret_word,letters_guessed):
    for j in secret_word:
        if j not in letters_guessed:
            secret_word=secret_word.replace(j,'_ ')
    return secret_word



def get_available_letter(letters_guessed):
    available_letters=string.ascii_lowercase
    for k in letters_guessed:
        available_letters=available_letters.replace(k,'')
    return available_letters


def no_of_unique_words(string):
    e=0
    l=[]
    for s in string:
        if s not in l:
            e+=1
            l.append(s)
    return e 



def guess_word(secret_word):
    no_of_guesses = 6
    letters_guessed=[]
    total_score=0
    
    print('Welcome to the game Word-Guess!')
    print(f'I am thinking of a word that is {len(secret_word)} letters long')
    print('-------------------------------------')
    
    while True:
        if (no_of_guesses <= 0 and is_word_guessed(secret_word,letters_guessed)==False ) or is_word_guessed(secret_word,letters_guessed)== True:
            if is_word_guessed(secret_word,letters_guessed)==True:
                total_score = no_of_guesses * no_of_unique_words(secret_word)
                print('Congratulations, you won!')
                print(f'Your total score is {total_score}')
            elif no_of_guesses == 0 and is_word_guessed(secret_word,letters_guessed) == False:
                print(f'Sorry you have lost the game, the word was {secret_word} ')
                
        else:
            available_letter=get_available_letter(letters_guessed)
            print(f'You have {no_of_guesses} guesses left.')
            print(f'Available letters : {available_letter}')
            
            
            letter_guessed=input('Please guess a letter : ')
            
            if (letter_guessed.isalpha() == False):
                print('This is not a valid letter.')
                print('--------------------------------------')
            elif (letter_guessed in letters_guessed):
                print('You have already guessed that letter.')
                print('---------------------------------------')
                continue
                
                
            letter_guessed=letter_guessed.lower()
            letters_guessed.append(letter_guessed)
            
            if letter_guessed in secret_word:
                    print(f'Good guess : {get_guessed_word(secret_word,letters_guessed)}')
            elif letter_guessed in ['a','e','i','o','u']:
                print(f'Oops! that letter is not in the word : {get_guessed_word(secret_word,letters_guessed)}')
                no_of_guesses -= 2
            else:
                print(f'Oops! that letter is not in the word : {get_guessed_word(secret_word,letters_guessed)}')
                no_of_guesses -= 1
            print('----------------------------------------')
            continue
        break

        
        
        
words = ['army', 'beautiful', 'became', 'if', 'actually', 'beside', 'between','come','eye','five','fur','imposter', 'problem' ,'revenge' ,'few' ,'circle' ,'district','trade','quota','stop','depressed','disorder','dentist']

secret_word=random.choice(words)

guess_word(secret_word)


# In[ ]:




