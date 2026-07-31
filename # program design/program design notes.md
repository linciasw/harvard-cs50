# Program Design 



## Before coding
1. What is the user trying to do?

2. What happens first?

3. What happens next?

4. What information exists?

5. Which information is one thing?

6. Which information is many things?

7. Which things have multiple pieces of information?

8. What can the user do?

9. What repeats?

10. Where does the program make decisions?



## Before writing EVERY function 
1. What is this function's one job?

2. What information does it need?

3. Where does that information come from?

4. Does it change any data?

5. Does it need to return anything?

6. What could go wrong?

---


## Question to ask

Instead of asking, "What Python concept should I use?", ask:
"What pattern is happening?"

Because Python concepts are just solutions to recurring patterns:
One thing → dictionary
Many things → list
Repeat until done → while
Repeat over a collection → for
Make a choice → if
Perform one job → function
Need to give information back → return


## High leverage skill

the highest-leverage habit: before writing any function, write a comment-only skeleton first.

```python

show menu
get user choice
while choice != 'quit':
if choice == 'add':
ask for expense details
 append to list
elif choice == 'view':
 loop through list, print each
 get user choice again -->
```

Once that skeleton reads correctly in English, filling in real code is almost mechanical. You're not "bad at logic" — you're skipping the English-skeleton step and trying to go straight from problem to Python, which is a much bigger jump than problem → plain description → Python.

And yes — practice matters too, but deliberate practice: after finishing a feature, go back and ask "why did I choose a list here and not a dict?" Naming your own reasoning after the fact trains you to do it up front next time.