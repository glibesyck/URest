"""
Main module of mini-project!
"""

import additional_functions
import interaction_data
import interaction_user

author_file = 'titles.csv'
poems_file = 'POEMS.txt'
films_file = 'keywords.list'

def main_program () :
    '''
    Main program.
    '''
    interaction_user.intro()
    print('-'*80)
    year = interaction_user.biography()
    if year != 1 and year != 0 :
        list_of_books =\
interaction_data.chosen_date(
interaction_data.creating_list_of_books(author_file), int(year))
        interaction_user.beautiful_print_list(
        interaction_user.transforming_list(list_of_books))
    elif year == 1 :
        list_of_books = interaction_data.creating_list_of_books(author_file)
        interaction_user.beautiful_print_list(interaction_user.transforming_list(
        additional_functions.random_choice(list_of_books)))
    list_of_user_keywords, answer = interaction_user.main_body()
    print('The films for you :')
    interaction_user.beautiful_print_list(additional_functions.first_elements(
    additional_functions.sorting_tuples(additional_functions.converting(
    interaction_data.looking_for_films(films_file, list_of_user_keywords)))))
    print('The poems for you :')
    if answer == 'Full' :
        interaction_user.beautiful_print_poems(
        interaction_data.reading_file(poems_file), additional_functions.first_elements(
        additional_functions.sorting_tuples(additional_functions.converting(
        interaction_data.counting_user_words(
        interaction_data.reading_file(poems_file), list_of_user_keywords)))))
    else :
        interaction_user.beautiful_print_list(
        additional_functions.first_elements(
        additional_functions.sorting_tuples(
        additional_functions.converting(
        interaction_data.counting_user_words(
        interaction_data.reading_file(poems_file), list_of_user_keywords)))))
    interaction_user.outro()

if __name__ == '__main__' :
    main_program()
