'''Docstring'''
from typing import List
import random
def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    letters=[[],[],[]]
    for i in letters:
        n_0=0
        while n_0<3:
            i.append(chr(random.randrange(97, + 26)))
            n_0+=1
    return letters
def get_words(f_0: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    if len(letters) != 9:
        return None
    with open(f_0,'r',encoding='utf-8') as file:
        file.readline()
        file.readline()
        file.readline()
        words = file.readlines()
    words = [word.strip() for word in words if len(word) >= 4 and letters[4] in word]
    words=[x.lower() for x in words]
    words = list(dict.fromkeys(words))
    v_words=[]
    for word in words:
        stat=True
        if set(word).issubset(set(letters)):
            for i in word:
                if word.count(i) > letters.count(i):
                    stat=False
            if stat is True:
                v_words.append(word)
    v_words=list(dict.fromkeys(v_words))
    return v_words
def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish for *nix or Ctrl-Z+Enter
    for Windows.
    Note: the user presses the enter key after entering each word.
    """
    user_words=[]
    while True:
        try:
            word=input()
            user_words.append(word)
        except EOFError:
            break
    return [i.lower() for i in user_words]
def get_pure_user_words(user_words:List[str],letters,words_from_dict:List[str]):
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    v_uwords=[]
    for word in user_words:
        word=word.lower()
        stat=True
        if set(word).issubset(set(letters)):
            for i in word:
                if word.count(i) > letters.count(i):
                    stat=False
            if stat is True:
                v_uwords.append(word)
    v_uwords=list(dict.fromkeys(v_uwords))
    dif=set(v_uwords).difference(words_from_dict)
    return list(dif)
def results(letters,user_input):
    '''Prints results in new file'''
    letters_in_list=letters[0]+letters[1]+letters[2]
    v_words=get_words('en.txt',letters_in_list)
    with open('results.txt','w',encoding='utf-8') as f_0:
        f_0.write(f'''
Number of correct answers:
{len(set(user_input).intersection(set(v_words)))}
Possible words:
{v_words}
Possible words missed by user:
{list(set(v_words).difference(set(user_input)))}
User words:
{user_input}
Words not from dictionary:
{list(set(user_input).difference(set(v_words)))}
''')
