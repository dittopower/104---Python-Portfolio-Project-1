
#-----Statement of Authorship----------------------------------------#
#
#  By submitting this task the signatories below agree that it
#  represents our own work and that we both contributed to it.  We
#  are aware of the University rule that a student must not
#  act in a manner which constitutes academic dishonesty as stated
#  and explained in QUT's Manual of Policies and Procedures,
#  Section C/5.3 "Academic Integrity" and Section E/2.1 "Student
#  Code of Conduct".
#
#  First student's no: n8888141
#  First student's name: James Clelland
#  Portfolio contribution: 25%
#
#  Second student's no: n8857954
#  Second student's name: Damon Jones
#  Portfolio contribution: 75%
#
#  Contribution percentages refer to the whole portfolio, not just this
#  task.  Percentage contributions should sum to 100%.  A 50/50 split is
#  NOT necessarily expected.  The percentages will not affect your marks
#  except in EXTREME cases.
#
#--------------------------------------------------------------------#


#-----Task Description-----------------------------------------------#
#
#  PSYCHOTHERAPIST
#
#  In this task you create a function which reflects user comments
#  back as questions or vague responses, like a non-directive
#  pyschotherapist.  Your function can be called automatically by our
#  unit tests below, or you can use it interactively by invoking the
#  provided "talk" function in IDLE's shell window.  See the
#  instruction sheet accompanying this template for further detail.
#
#--------------------------------------------------------------------#


#-----Acceptance Tests-----------------------------------------------#
#
#  This section contains the unit tests that your function must
#  pass.  You may not change anything in this section.  NB: When
#  your program is marked the following tests will all be used as
#  well as some additional tests (not provided) to ensure your
#  solution works for other cases.
#
#  NB: The strings below are delimited by single quotes, which is
#  Python's default, unless the string contains a single quote as
#  an apostrophe, in which case the string is delimited by double
#  quotes.  You may NOT change the quote marks in either the
#  function arguments or returned values below.
#

"""
---------- Tests that produce a fixed elicitation response

An empty string
>>> reflect_statement('') # Test 1
"I'm not sure that I understand you fully."

A single word
>>> reflect_statement('Hello') # Test 2
"Tell me what you're really thinking of."

Another single word
>>> reflect_statement('oops') # Test 3
'Try to clarify your thoughts.'

A typical, unhelpful response from the user
>>> reflect_statement('No!') # test 4
'Please go on.'

Some text with no alphabetic characters
>>> reflect_statement('$#|+!!!') # Test 5
'You seem to be having trouble expressing your feelings.'

A single word longer than our list of elicitations
>>> reflect_statement('Supercalifragilisticexpialidocious!') # Test 6
'Pray continue.'

---------- Tests that just return the original sentence as a question

A whole sentence, no punctuation, no reflections
>>> reflect_statement('The cat sat on the mat') # Test 7
'The cat sat on the mat?'

A whole sentence, with punctuation, but no reflections
>>> reflect_statement('The big, fat dog sat on the rug!') # Test 8
'The big, fat dog sat on the rug?'

---------- Tests that reflect words

A whole sentence, no punctuation, one reflection
>>> reflect_statement('The dog sat on my rug') # Test 9
'The dog sat on your rug?'

A whole sentence, no punctuation, multiple reflections
>>> reflect_statement('My elephant sat on our house') # Test 10
'Your elephant sat on your house?'

A whole sentence, some punctuation, multiple reflections,
>>> reflect_statement('We went to a wedding with our cat!') # Test 11
'You went to a wedding with your cat?'

A whole sentence, multiple reflections, with an apostrophe
>>> reflect_statement("I'll eat my hat!") # Test 12
"You'll eat your hat?"

A sentence with capitalised proper nouns that should be left alone
>>> reflect_statement('My best friends are Fred and Barney.') # Test 13
'Your best friends are Fred and Barney?'

---------- Tests that begin with a word we want to omit in the response

A short affirmative sentence
>>> reflect_statement("Yes that's right") # Test 14
"That's right?"

A long negative sentence
>>> reflect_statement("No, you're not listening to me.") # Test 15
"I'm not listening to you?"

---------- Tests with missing punctuation or incorrect capitalisation

A lower-case sentence with no punctuation
>>> reflect_statement('im feeling unwell') # Test 16
"You're feeling unwell?"

Some SMS speak
>>> reflect_statement('i c u') # Test 17
'You see me?'

---------- A full conversation with the psychotherapist
           (This reads better if executed using the talk function)

>>> reflect_statement('I hope your advice can help me!') # Test 18
'You hope my advice can help you?'

>>> reflect_statement("I'm feeling depressed.") # Test 19
"You're feeling depressed?"

>>> reflect_statement("It's because our dog ran away with a cat!") # Test 20
"It's because your dog ran away with a cat?"

>>> reflect_statement('Yes') # Test 21
'Please go on.'

>>> reflect_statement('It happened at my wedding reception.') # Test 22
'It happened at your wedding reception?'

>>> reflect_statement("Yes, we've been very unlucky with our pets.") # Test 23
"You've been very unlucky with your pets?"

>>> reflect_statement("I'm not sure that you're helping my problem.") # Test 24
"You're not sure that I'm helping your problem?"

>>> reflect_statement("You just repeat whatever I say!") # Test 25
'I just repeat whatever you say?'

>>> reflect_statement("I think you're just a machine!") # Test 26
"You think I'm just a machine?"

>>> reflect_statement('Aaargh!') # Test 27
'You seem to be having trouble expressing your feelings.'

"""
#
#--------------------------------------------------------------------#


#-----Data For Your Function-----------------------------------------#
#
#  The following variables contain the data that your function must
#  use to perform its task.  NB: You may NOT change the values of
#  either of these variables.

# These pairs are used to "reflect" sentences into questions
reflections = \
[["I",          "you"],
 ["i",          "you"],
 ["We",         "you"],
 ["we",         "you"],
 ["We're",      "you're"],
 ["we're",      "you're"],
 ["I'm",        "you're"],
 ["i'm",        "you're"],
 ["im",         "you're"],
 ["this",       "that"],
 ["This",       "that"],
 ["am",         "are"],
 ["Am",         "are"],
 ["My",         "your"],
 ["my",         "your"],
 ["you",        "I"], # Grammar: Sometimes "me" is better
 ["You",        "I"],
 ["u",          "me"],
 ["I'd",        "you'd"],
 ["I'll",       "you'll"],
 ["We'd",       "you'd"],
 ["we'd",       "you'd"],
 ["We'll",      "you'll"],
 ["we'll",      "you'll"],
 ["You're",     "I'm"],
 ["you're",     "I'm"],
 ["ur",         "I'm"],
 ["c",          "see"],
 ["I've",       "you've"],
 ["We've",      "you've"],
 ["we've",      "you've"],
 ["Our",        "your"],
 ["our",        "your"],
 ["was",        "were"],
 ["Was",        "were"],
 ["were",       "was"],
 ["Were",       "was"],
 ["me",         "you"],
 ["your",       "my"],
 ["Your",       "my"]]


# These vague responses aim to elicit further comments from the user
elicitations = \
["I'm not sure that I understand you fully.",
 "Please elaborate.",
 "I'd like to hear more.",
 "Please go on.",
 "Try to clarify your thoughts.",
 "Tell me what you're really thinking of.",
 "Please go into detail.",
 "You seem to be having trouble expressing your feelings.",
 "Please continue.",
 "Tell me more.",
 "I'd like you to give me more detail.",
 "Pray continue."]

#
#--------------------------------------------------------------------#


#-----Code for Interaction-------------------------------------------#
#
# The following function is provided to allow you to interact
# with your reflect_statement function so that you can have a
# conversation with the psychotherapist

def talk():
    # Any of these responses will stop the interaction
    farewells = ["Bye", "bye", "Goodbye", "goodbye", "Bye.", \
                 "Goodbye.", "quit", "exit", "stop"]
    # Start the conversation
    reply = raw_input("Hello, what seems to be your problem? ")
    # Keep prompting and responding until one of the "farewells" is typed
    while not reply in farewells:
        reply = raw_input(reflect_statement(reply) + " ")
    # End the conversation
    print "Goodbye."

#
#--------------------------------------------------------------------#


#-----Students' Solution---------------------------------------------#
#
#  Complete the task by filling in the template below.


##### CREATE YOUR SOLUTION BY REPLACING THE FOLLOWING "STUB" FUNCTION

# Dummy function that just returns the argument unchanged
def reflect_statement(statement):

    from random import randint
##  idenftify words
    spaces = [0]    
    words = []
    for pos in range (statement.count(' ')):			 
        spaces.append(statement.find(' '))
        statement = statement.replace(' ', '?',1)
##    print spaces

## Create Word list        
    for pos in range (len(spaces)):
        start = spaces[pos]
        if pos == (len(spaces)-1):
            end = len(statement)
        else:
            end = spaces[pos+1]
        words.append(statement[start:end].replace('?',''))

##    print words

##     elicitations check
    if len(words) <= 1:
        if len(statement)-1 > len(elicitations):
            statement = elicitations[len(elicitations)-1]
        else:
            statement = elicitations[len(statement)]
        return statement
## Remove yes and no from sentence start
    lostwords = ['yes', 'Yes', 'yes,', 'Yes,', 'no', 'No', 'no,', 'No,']
    for indexs in range (len(lostwords)):
        if words[0] == lostwords[indexs]:
            words.remove(lostwords[indexs])
## Lose end  punctuation
    if words[len(words)-1][len(words[len(words)-1])-1].isalpha() == False:
        words[len(words)-1]= words[len(words)-1][:(len(words[len(words)-1])-1)]
        
#### statement redirection (replace with reflections)
    reflections.sort(key=lambda reflection: len(reflection[0]), reverse = True)
    for word in range(len(words)):
        for index in range(len(reflections)):
            if reflections[index][0] == words[word]:
                words[word]=words[word].replace(reflections[index][0],reflections[index][1])
                break
##    print words
## reply assembly
    statement = ''
    for each in range(len(words)):
        statement = statement + ' ' + words[each]           
        if statement[0] == ' ':                                 # No space for first word
            statement = statement[1:]
## Check end for extra space or punctuation, then add a ?            
    if (statement[len(statement)-1] == ' ') or (statement[len(statement)-1].isalpha() == False):
        statement = statement[:len(statement)-1] + '?'
    else:
        statement = statement + '?'
    statement = statement[0].capitalize() + statement[1:]
## return statement as reply    
    return statement 

#
#--------------------------------------------------------------------#


#-----Automatic Testing----------------------------------------------#
#
#  The following code will automatically run the acceptance tests
#  when the program is "run".  If you want to prevent the tests
#  from running, and test your function manually using the "talk"
#  function provided, comment out the code below.
#
if __name__ == '__main__':
    from doctest import testmod
    testmod(verbose=True)
#
#--------------------------------------------------------------------#

