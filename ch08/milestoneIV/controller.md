# Final Project Milestone #3

[Final Project Description](https://docs.google.com/document/d/1j3zgypVjPjzXl4pL1_Wpjvp3GLCW9zcFydkwUjNfNUA/edit?usp=sharing)

Complete this document in **your** portfolio (CH 10).

If you haven't already, you should now begin to code your Controller.

Define your Controller in the `FinalProject/src/` folder in your portfolio.

Although you will probably need to alter it further, you should try to write as much of the conroller as you can. You can always change things later.

## Models Design

You should have the following in your Controller class

1. A single event loop that handles all events
    * if you are responding to events in the model, that is incorrect and will cause problems. You should only handle events in one class, the controller
    * You may have subloops for submenus with different event loops for different states (*Start menu / game / end menu*), but you should never respond to events more than once in each loop (or frame loop)

***

## Controller

Answer the following questions about your controller class

1. do you have a mainloop?
    * if you have sub loops, are they exclusive? i.e. only 1 will ever run at a time

2. Are you responding to events first in your loop?

3. Are you updating models after events?

4. Are you re-drawing the background, THEN each screen element every frame?

5. Are you calling pygame.flip() or pygame.update() at the end of your mainloop
