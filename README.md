# hangman_ash
### Game description: 
This is a program runs the hangman game from command line. 
Program chooses a random word from a text stored locally, if file not 
found locally it downloads it from web into a specific directory. 
Program then randomly selected a word which is greater in size then 
the minimum value users enters to start the program.
#####Then the game begins...
####To start the game:
<ol>
<li>First open command line
<li>Go to the directory where program is located
<li>Type in the following:

```
python hang_man.py -m (minimum length of word)
```
<li>Program then displays the mystery word status by displaying __ 

```
 _  _  _  _  _  _  _  _
```
<li>Program also gives option of letter to choose from and update list 

```
 _  _  T  T _ I _ _  
Pick from these letters: A B C D E F G H ~~ J K L M O P Q R S ~~ U V W X Y Z
Guess a letter:
```
<li>Program will output an error message in the input is not one letter only

```
Invalid input, please enter a letter
```
<li>Program will keep running until user loses or wins

```

            |‾‾‾‾‾‾‾|
            |       O
            |      /|\
            |      / \
            |

Sorry you lose, the correct word was: JUTTYING
```


### Code description 
This program has 6 methods:
<ol>
<li><b>__init__(self, min_limit)</b>: Initializes the object and taking minimum word limit as argument.
<li><b> access_doc(self)</b>: In this method program searches to see if it can find the word doc locally if not it downloads it from a URL and stores in a predefined location. 
<li><b>assign_word(self)</b>: This method takes in the word doc from previous method and assigns a random word that is greater than or equal to min length.
 <li><b>hang_display(self, wrong)</b>: This method prints out different stages of hangman according to number of wrong variable, which is passed up by the following method hangman_game.
<li><b>hangman_game(self)</b>: This method starts the game, where it taken in guess input from user, validates and execute game functions.
<li><b>main()</b>: Driver function that calls the initializes the class.


#### Code Inputs
The program takes in:
<ol>
<li> A string character
<li> A Text file
</ol>

#### Code Outputs
The program outputs:
<ol>
<li> Error message if input fails validation
<li> Hangman status
<li> Word status by displaying blank lines 
<li> Letters users can choose from
<li> If user won or lost

