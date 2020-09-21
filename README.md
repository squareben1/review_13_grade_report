# Review 13

Simple observed Kata focused on TDD process.

## Retro

Fairly happy with this review. I switched back to Python after doing the last few in Ruby and, even though I've mainly been using Python recently, for some reason I kept blanking on how certain functions/processes worked in this langage. Possibly something to do with being under observation and maybe my subconcious protesting for the more intuitive .join() method in Ruby...

Either way, not as fluent as I would have liked. Some obvious mistakes that shouldn't have been made regardless of language.

Chose to use Chicago-style TDD rather than London (building out each piece of functionality fully before moving onto next). In this simple context it really only meant counting multiple greens before moving onto ambers but still useful to think about the differences, as I'd intended.

Stuck fairly well to good TDD process. Definitely did the fastest thing to make a test pass, rather than try to get the most optinal/graceful approach straight away. This allowed for some satisfying refactors.

Extracted count_colour() functions for each colour for sake of SRP.

## 🦆
Pleased with how I spoke through my process aloud. Further evidence for helpful this is. 

Probably my last review for a while! 😢

Katherine had minor but useful feedback:
1. Function Naming: Use VERBS! Original function was named ```grade_checker(string)``` which sounds like an object/class rather than a function. Changed to ```check_grades()```
2. Commit Messages: these were short and non-descriptive during this review for sake of speed under time-pressure but feedback is still valuable; they should be DESCRIPTIVE, for example "Can count single red grades" rather than "single red". 
3. List Vs. Array:
   
    List = Dynamic

    Array = Fixed (in a statically typed language for example; "creating an array of length 5 of int type")


## Initial Requirements Gathering

```
Review 13 - School Reports

IN - String of comma sep grades
OUT - Simple summary report
Green = over 75
Amber = 50-74
Red = < 50

Always seperated by comma and space OR just comma

    In	    |	  Out
-------------------------
“75”		| “Green: 1”
“75, 76”	| “Green: 2”
“50”		| “Amber: 1”
“50, 51”	| “Amber: 2”
“49”		| “Red: 1”
"10, 50, 70, 100" | "Green: 1\nAmber: 2\nRed: 1"
```