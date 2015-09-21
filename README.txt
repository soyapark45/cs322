[How to use]
1. Fill up the config at DFA.cfg. 
Provide states, symbols, delta, initial and final states.
ex) 
———DFA.cfg———
States: 0,1,2,3,4,5
Symbols: a,b
Delta: (0,a,1) (0,b,2) (1,a,1) (1,b,1) (2,a,1) (2,b,3) (3,a,4) (3,b,1) (4,a,1) (4,b,5) (5,a,5) (5,b,5)
Initial: 0
Final: 5
————————————
States are given as sequence of name of states seperated by comma.
Symbols, Final are same as States.
Delta are given as tuple (current_state, symbol, next_state).
Initial is one of States. 
2. Provide string when running pyton file. ex) python dfa.py bbaa
3. If given string is accepted by a language of DFA, it will return True otherwise False.

[Build environment]
OS: Window 7
Python version: 3.5.0