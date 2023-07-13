# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 19:17:48 2023

@author: Dusanthan Sivarajah
"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def new_game():
    
    guesses = [] 
    correct_guesses = 0 
    question_num = 1    
    
    for key in questions:
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("\n Enter (A, B, C, or D): ").upper()
        guesses.append(guess)
        
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
        
    
    dispay_score(correct_guesses,guesses)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def check_answer(answer,guess):
    
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!!")
        return 0 
    
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def dispay_score(correct_guesses, guesses):
    
    print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("                 RESULTS")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Answers: ", end = "")
    for i in questions:
        print(questions.get(i), end= " ")
    print()
    print("Guesses: ", end = "")
    
    
    for i in guesses:
        print(i, end= " ")
    print()
    
    score = int((correct_guesses/len(questions)*100)) 
    print("\nYour score is: " + str(score)+ "%")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def play_again():
    
    keep_playing = input("\n Do you want to re-try the quiz? Type yes: ").upper()
    
    if keep_playing == "YES":
        return True
    else: 
        return False
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#The questions are placed in a dictionary(key,value) named questions, where the questions are keys with associated vales.
#By selecting the proper value will determin whether the user chooses the right answer.  
questions = {
    "1) Who was the father of computer?\n":"A",                                       #Charles Babbage
    "2) What is the full form of CPU?\n":"A",                                         #Central Processing Unit
    "3) What is the full form of CU?\n":"D",                                          #Control Unit    
    "4) What is the full form of ALU?\n":"C",                                         #Arithmetic Logic Unit   
    "5) What is the full form of MU?\n":"C",                                          #Memory Unit
    "6) What is the full form of EEPROM?\n":"C",                                      #Electrically Erasable Read Only Memory
    "7) What is the full form of SDRAM?\n":"B",                                       #Synchronous Dynamic Random Access Memory
    "8) Which electronics component is used in first generation computers?\n":"A",    #Vacuum Tubes
    "9) Which is not a correct type of a computer?\n":"D",                            #Mini Frame Computer
    "10) Which part of the computer is considered as Brain of the Computer?\n":"B"    #Central Process Unit
    
    }


#The options is a 2D list(a list of lists) that stores all the possible answeres that the user can select to each of the question shown above.
#Each list corresponds to a key value pair within the dictionary of questions.
options=[["A. Charles Babbage", "B. Dennis Ritchie", "C. Charlie Babbage" , "D. Ken Thompson"],
        ["A. Central Processing Unit", "B. Central Process Unit", "C. Central Programming Unit", "D. Central Progressive Unit"],
        ["A. Compound Unit", "B. Communication Unit", "C. Computer Unit", "D. Control Unit"],
        ["A. Arithmetic Local Unit", "B. Advance Logical Unit", "C. Arithmetic Logic Unit", "D. None of these"],
        ["A. Management Unit", "B. Masked Unit", "C. Memory Unit", "D. Main Unit"],
        ["A. Electrically Erasable Read Access Memory","B. Ethical Electrically Read Only Memory", "C. Electrically Erasable Read Only Memory", "D. None of these"],
        ["A. Special Dynamic Read Access Memory","B. Synchronous Dynamic Random Access Memory", "C. Synchronous Dynamic Read Access Memory", "D. Special Dynamic Random Access Memory"],
        ["A. Vacuum Tubes", "B. Transistors", "C. ULSI Chips", "D. LSI Chips"],
        ["A. Super Computer", "B. Workstations", "C. Personal Computer", "D. Mini Frame Computer"],
        ["A. Random Access Memory",  "B. Central Process Unit", "C. Read Only Memory", "D. Hard Disk"]
]

new_game()

while play_again():
    new_game()
print("GOOD LUCK and GOODBYE! ")