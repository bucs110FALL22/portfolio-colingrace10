# Final Project Milestone #5

[Final Project Description](https://docs.google.com/document/d/1j3zgypVjPjzXl4pL1_Wpjvp3GLCW9zcFydkwUjNfNUA/edit?usp=sharing)

# ATP

An Acceptance Test Procedure is a step by step guide to anyone using the software that shows the software works according to the specifications. In the software industry, an **ATP**, must be completed before delivering the software to the customer. The **ATP** should be designed so that someone who has no idea what your Project is or how to run it can follow your instructions and see as much of your project as possible.

This also gives you a checklist of things that must be working by the time you submit your project. You will put together an Acceptance Test Procedure (ATP) at the end of your proposal in tabular format. Note the example one provided here and in the sample proposal. 

**The ATP must:**
1. be thorough and efficient
2. show how ALL of your program features work and that they work correctly
3. include steps that show bugs and how the program handles user errors

Note how the sample ATP in the project description illustrates all of the features of the fictional GUICounter program, and how each step is arranged to set up the next test efficiently without undue repetition.

Also notice that in each instruction, there is only 1 thing that can break:
* Click “Play” button - possible error
    * it doesn’t respond to the event 
* Press LEFT ARROW, hold LEFT ARROW
    * The player doesn’t move or moves in the wrong direction

If you combine actions, then you cannot clearly see the errors:
Press the left arrow to move left and ther right arrow to move right - which one caused the error, the left or the right event?

You ***MUST*** write your ATP in the same tabular fashion illustrated in the sample provided using markdown in your README.md.

Columns must be the same as shown:  
* Step: step number
* Procedure:  exact procedure for tester to follow
* Expected Results:  description of results to be expected - must be EXACT

