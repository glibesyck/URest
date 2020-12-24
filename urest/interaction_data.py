"""
Functions for working with different data-bases.

For working with "POEMS.txt" :
     ! reading_file
     ! counting_user_words
------------------------------
For working with "titles.csv" :
     ! creating_list_of_books
     ! chosen_date
------------------------------
For working with "keywords.list" :
     ! looking_for_films
"""
import pandas as pd

def reading_file (file_of_poems : str) -> list :
    '''
    Return the list of tuples where the first elements are the names of poems
    and the second elements are lists of strings of the poem.
    '''
    general_list = [] #our end list
    lines = [] #for lines from file
    with open (file_of_poems, 'r', encoding = 'utf-8') as poems :
        for line in poems :
            line = line.strip()
            lines.append(line)
    for line in lines :
        if line.startswith("\"") : #the title of poem begins with "\""
            new_strings_poem = [] #list for new poem
            idx = lines.index(line)
            poem_string = lines[idx+1]
            while idx+2 < len(lines) and not poem_string.startswith("\"") :
            #adding all strings till the moment we see next poem or end of file
                new_strings_poem.append(poem_string)
                idx+=1
                poem_string = lines[idx+1]
            general_list.append((line, new_strings_poem)) #adding poem title
    return general_list

def counting_user_words (poems : list, keywords : list) -> dict :
    '''
    Return the dictionary where keys are the names of poems and values are numbers
    how many times keywords appeared in the poems.
    >>> counting_user_words(reading_file('POEMS.txt'), ['rainbow'])
    {'"FIDELITY"': 2, '"My heart leaps up..."': 2, '"ODE"': 2}
    '''
    poem_dict = {}
    for keyword in keywords :
        for poem in poems :
            for string_of_poem in poem[1] :
                if keyword in string_of_poem or keyword.capitalize() in string_of_poem :
                    poem_dict[poem[0]] = poem_dict.get(poem[0], 1) + 1
    return poem_dict

def creating_list_of_books (file : str) -> list :
    '''
    Return the list of tuples of titles of books where user can find out
    something about author's biography and their date of publication.
    '''
    list_of_books = []
    dataframe_author = pd.read_csv(file)
    dataframe_author = dataframe_author[['Title', 'Date of creation/publication', 'Topics']]
    #we only nedd these columns
    dataframe_author.dropna(subset = ['Date of creation/publication'], inplace = True)
    #drop all columns where no language mentioned
    dataframe_author = dataframe_author.loc[
        dataframe_author['Topics'].str.contains('biography')|\
        dataframe_author['Topics'].str.contains('Biography')]
    #looking for titles that are reffered to biography
    for _, row in dataframe_author.iterrows() :
        book_tuple = (row['Title'], row['Date of creation/publication'])
        list_of_books.append(book_tuple)
    list_of_books = list(set(list_of_books)) #avoid same books
    return list_of_books

def chosen_date (list_of_books : list, year : int) -> list :
    '''
    Return the list of titles of books which were published in the given year
    or most close to that year.
    >>> chosen_date(creating_list_of_books('titles.csv'), 1900)
    [('Poems', '1889'),\
 ('The poetical works of Wordsworth : with memoir, explanatory notes, &c', '1889'),\
 ('Wordsworth centenary : souvenir handbook', '1950'), ('Westmorland Gazette', '1950'),\
 ('The letters of William and Dorothy Wordsworth', '1969')]
    '''
    list_of_exact_books = []
    idx_year = 0
    while len(list_of_exact_books) < 5 :
        for book in list_of_books :
            if int(book[1]) == year + idx_year or int(book[1]) == year - idx_year :
                list_of_exact_books.append(book)
        idx_year += 1
    return list_of_exact_books

def looking_for_films (file : str, keywords : list) -> dict :
    '''
    Return the dictionary of films that have exact keyword with value equals to
    number of keywords that are reffered to this film.
    '''
    dict_of_films = {}
    with open (file, 'r', encoding = 'utf-8', errors = 'ignore') as file_films :
        for line in file_films :
            film, film_keyword = line.strip().split('\t')[0],\
                                 line.strip().split('\t')[-1]
            for our_keyword in keywords :
                if our_keyword in film_keyword and '{' not in film and film[0].isupper() :
                # by "{" we drop TV-series and by isupper we drop list of keywords
                # at the beginning of file
                    dict_of_films[film] = dict_of_films.get(film, 0) + 1
    return dict_of_films
