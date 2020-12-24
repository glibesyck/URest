"""
Module for working with user and terminal.

      ! bold_text
      ! center_text
      ! delay_text
      ! transforming_list
      ! beautiful_print_list
      ! beautiful_print_poems
      ! intro
      ! biography
      ! main_body
      ! outro
"""

import os
from time import sleep

def bold_text(text : str) -> str :
    '''
    Return bold text.
    '''
    return '\033[1m' + text + '\033[0m'

def center_text (text : str) -> str :
    '''
    Return text aligned to the center of terminal.
    '''
    return text.center(os.get_terminal_size().columns)

def delay_text (text : str) :
    '''
    Print text by elementss with delay.
    '''
    for element in text :
        print(element, end ='', flush = True)
        sleep(0.01)

def transforming_list (list_of_tuples : list) -> list :
    '''
    Return transformed list (was list of tuples and now it is just list).
    >>> transforming_list([('first', '12'), ('second', '13'), ('third', '14')])
    ['first (12)', 'second (13)', 'third (14)']
    '''
    new_list = []
    for elem in list_of_tuples :
        new_list.append(elem[0] + ' ' + '(' + elem[1] + ')')
    return new_list

def beautiful_print_list (list_of_smth : list) :
    '''
    Print lists beautifully.
    '''
    print('-'*80)
    for idx in range(len(list_of_smth)) :
        print(idx+1, '-', bold_text(list_of_smth[idx]))
    print('-'*80)

def beautiful_print_poems (poems : list, poems_we_need : list) :
    '''
    Print poems fully if user wants to.
    '''
    print('-'*80)
    for poem in poems :
        if poem[0] in poems_we_need :
            print(bold_text(center_text(poem[0])))
            for string in poem[1] :
                print(string)
            print('-'*80)

def intro () :
    '''
    Print intro for the program.
    '''
    print(center_text(bold_text('Welcome to URest!')))
    main_intro_text = 'URest is a safe-space where you can experience tranquility \
and find out new information about writers.\nThe main aim of the \
project is to create an environment where you feel peace and have a rest \
during tough periods with help of nature landspaces abd scenes \
depicted in films and poetry.\nWilliam Wordsworth is a master \
of describing nature, so you have a great opportunity to meet his worlds \
and his life!\n'
    delay_text(main_intro_text)

def biography () -> tuple :
    '''
    First part of program where user can find out something about the author.
    Return year or 0.
    '''
    year = 0
    print('Do you want to find out something about William Wordworth? (Yes/No)')
    user_input = input()
    while user_input != 'yes' and user_input != 'Yes' and user_input != 'no' and\
    user_input != 'No' :
        print('I don\'t know what it means! Please type "Yes" or "No"!')
        user_input = input()
    if user_input == 'yes' or user_input == 'Yes' :
        print('Any specific year of publishing? (Year as number, 1 as no year)')
        year = input()
        try :
            year = int(year)
        except ValueError :
            print('I don\'t know what it means! Please type year as number!')
            year = input()
    else :
        print('Great, let\'s continue our journey!')
    return year

def main_body () :
    '''
    Print main part of the program.
    Return list of words.
    '''
    main_text = 'I want you to feel inner peace and restore your strength by\
 creating an unique world for you!\n'
    delay_text(main_text)
    list_of_user_keywords = []
    print('Enter a couple of places where you want to be (for example : field,\
 ocean) or what you want to see (for example : daffodil, rainbow) and\
 I\'ll give you some poetry and films! Please type each word with\
 first small letter, in singular form and each followed by ENTER! To end\
 just press ENTER!')
    while True :
        word = input()
        if word :
            list_of_user_keywords.append(word)
        else :
            break
    print('Do you want to see full texts of poems? (Full/Title)')
    answer = input()
    while answer != 'Full' and answer != 'Title' :
        print('I don\'t know what it means! Please type "Full" or "Title"!')
        answer = input()
    return list_of_user_keywords, answer

def outro () :
    '''
    Print outro.
    '''
    print('Here you are! Enjoy your time and remember that it is alright \
to have a rest!')
    print(bold_text(center_text('Take care of yourself!')))
