"""Typing test implementation"""

from queue import Empty
from tkinter import E
from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    # END PROBLEM 1
    empty = []
    for i in range(len(paragraphs)):
        if select(paragraphs[i]):
            empty.append(paragraphs[i])
    if k > len(empty)-1:
        return ''
    else:
        return empty[k]
    '''把符合的数据放到empty这个新list里面'''

def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    
    def exist(paragraph):
        for i in range(len(topic)):
            topic[i] = lower(topic[i])
            paragraph0 = split(remove_punctuation(paragraph))
            j = 0
            for j in range(len(paragraph0)):
                paragraph0[j] = lower(paragraph0[j])
                if topic[i] == paragraph0[j]:
                    sign = True # return 会停止循环，所以用signal
                    break
                else:
                    sign = False
            if sign == True:
                return True
        if sign == False:
            return False
    return exist
    


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words, reference_words = split(typed), split(reference)
    # BEGIN PROBLEM 3
    if len(typed) == 0:
        return 0.0
    else:
        count = 0
        for j in range(len(typed_words)):
                if(len(reference_words) > j):
                    if typed_words[j] == reference_words[j]:
                        count += 1
        return count / len(typed_words) * 100


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    if typed == "":
        return 0.0
    else:
        return len(typed) / 5 * 60 / elapsed
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    result = limit
    for i in range(len(valid_words)):
        if valid_words[i] == user_word:
            return user_word
        else:
            result = min(diff_function(user_word, valid_words[i], limit), result)
    if result == limit:
        for i in range(len(valid_words)):
            if diff_function(user_word, valid_words[i], limit) == limit:
                return valid_words[i]
        return user_word
    else:
        for i in range(len(valid_words)):
            if diff_function(user_word, valid_words[i], limit) == result:
                return valid_words[i]


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    i = 0
    def diff(start, goal, i):
        if i > limit:
            return i
        elif len(goal) == 0:
            return i + len(start) - len(goal)
        elif len(start) == 0:
            return i + len(goal) - len(start)
        elif start[0] != goal[0]:
            i += 1
            return diff(start[1:],goal[1:],i)
        else:
            return diff(start[1:],goal[1:],i)
        #Note slice recursion for list典型范例
    if start == goal:
        return 0
    elif len(start) == 0:
        return len(goal)
    elif len(goal) == 0:
        return len(start)
    else:
        return diff(start=start,goal=goal,i=i)


def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    if limit < 0:
        return 0
    elif len(start) == 0 and len(goal) == 0:
        return 0
    elif len(start) == 0 or len(goal) == 0:
        return max(len(goal),len(start))
    elif start[0] == goal[0]:
        return pawssible_patches(start[1:],goal[1:],limit)
    else:
        add = pawssible_patches(start, goal[1:], limit - 1)  # Fill in these lines
        remove = pawssible_patches(start[1:], goal, limit - 1) 
        # 删除之后第二个word还是本身
        substitute = pawssible_patches(start[1:], goal[1:], limit - 1)
        return min(add, remove, substitute)+1


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""


###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    total = 0
    for i in range(len(typed)):
        if(len(prompt) > i):
            if typed[i] == prompt[i]:
                total += 1
            else:
                break
    send({'id': user_id, 'progress': total / len(prompt)})
    return total / len(prompt)
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    new = []
    for i in times_per_player:
        new.append([i[j] - i[j-1] for j in range(1,len(i))])
    return game(words,new)


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    player_indices = range(len(all_times(game)))  # contains an *index* for each player
    word_indices = range(len(all_words(game)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    print(player_indices)
    fastest = [[] for _ in player_indices]
    print(fastest)
    for i in word_indices:
        min_time = float('inf')
        player = 0
        for j in player_indices:
            if time(game,j,i) < min_time:
                min_time = time(game,j,i)
                player = j
        fastest[player].append(word_at(game,i))
        print(fastest[player])
    return fastest

    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)