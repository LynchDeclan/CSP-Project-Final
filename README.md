# CSP-Project-Final
### Video:
<a href="https://drive.google.com/file/d/12zqncOgtF-f5BnLrTTTSoqKS2aWKUcOL/view">One minute video of code running</a>
## Functionality Summarisation:
##### What does it do?
This program consists of three random output generators that the user can select from: A magic 8-ball, a diceroller, and a coin flipper.
This program asks the user for input, and then generates a random output based on them selecting a random option from the list of pre-determined answers. It also includes a system where it asks the user if they want to ask another question, roll another die, or flip another coin. For all of them, there is an option to do have multiple questions, rolls, or flips, and for the latter two, there is also an option to roll multiple dice or flip multiple coins in one turn.
##### Why does it exist / Who is it for?
I want to make this so that I can have some familiarity and mastery of the Python language. It is meant to be a start on what I might create in the future since, at this point, I am not really confident in many aspects of Python yet. This could be for my friends to try out, just for fun. It also provides a useful tool for people to use as an alternative to the web versions of these things. 
## Learned to do something new: 
##### Using while loops
![CSP-Project-Final_project py at main · LynchDeclan_CSP-Project-Final - Opera 1_19_2023 9_51_10 PM](https://user-images.githubusercontent.com/89731702/213534009-4ee4fc0d-ade4-475b-a4a2-1b63d407cac6.png)
![CSP-Project-Final_project py at main · LynchDeclan_CSP-Project-Final - Opera 1_19_2023 9_49_09 PM](https://user-images.githubusercontent.com/89731702/213534038-deecd426-1e76-4e50-b658-d870491b0dcb.png)
## Data Abstraction:
![CSP-Project-Final_project py at main · LynchDeclan_CSP-Project-Final - Opera 1_19_2023 10_02_16 PM](https://user-images.githubusercontent.com/89731702/213536007-3e149e53-814c-44ce-af62-9afbe207b547.png)
![CSP-Project-Final_project py at main · LynchDeclan_CSP-Project-Final - Opera 1_19_2023 10_07_23 PM](https://user-images.githubusercontent.com/89731702/213536962-bc762086-3dad-4d1f-a2b5-b116333ac03d.png)
##### These are examples of data abstraction. It is in these variables that the values are stored for all the different numbers for the different "sides" of the different type sof dice in lists.
##### The values are retrieved in the conditional statements, that, depending on which type of dice the user chose, it would pull a random value from one of the lists and print it out.
##### If I did not include this data abstraction within this part of the program, then there would be nowhere to store the values for the different sides of the different dice. There would be no use for the random function within that section of the code, as there would be no lists to pull random values from. The code simply would not do as it was created to do in the first place.
## Procedural Abstraction:
##### I define three main functions in my program that hold all the code for the three main features of the program, the "eight_ball" function, the "dice_roll" function, and the "coin_flip" function. These functions are called at the beginning of the program, in the "chooser" function, which is the function that starts off the program and makes it possible for the user to use the three main functions (eight_ball, dice_roll, coin_flip). This is the code section that includes:
#### Procedure
#### Algorithm 
##### With Sequencing, Selection, and Iteration
![CSP-Project-Final_project py at main · LynchDeclan_CSP-Project-Final - Opera 1_19_2023 11_41_49 PM](https://user-images.githubusercontent.com/89731702/213555032-cdde9307-e2e7-46a8-9025-706158a68cd8.png)
##### The sequencing that takes place in this specific function ("chooser") is how the computer reads the code from top to bottom, starting with the prompt, called "option", which is the one that asks the user to choose one of three random output generators, consisting of the magic 8-ball, the dice roller, and the coin flipper.
##### Then we we see iteration, through the use of a While Loop, that will keep on running these conditional statements of the code unless the user chooses "exit" in the prompt. 
##### Then we see selection being used in the conditional statements within the While Loop, which checlk whether the user has chosen one of the three inputs. If so, then call the function associated with it. If not, exit the program, or exit it while they choose "exit" specifically, as is checked in the conditional statement that is present outside of the while loop.
##### This procedural abstraction helped me to manage complexity in my code by allowing me to easily call the functions that contained all of the main code for the magic 8-ball, diceroll, and coinflip programs. It al;so allowed me to, after the user had finished with using one of the random output generators, take them back to the start by calling the function "chooser". It helps to manage complexity by giving me a place to put my code and call it whenever I need to, without having to copy and paste gigantic chunks of code when it needs to be used, and it gives the code a place to stay until it is needed and called.
