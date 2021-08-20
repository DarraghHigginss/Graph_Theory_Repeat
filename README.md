## G00373984:
# Description
This is a program Written in Python 3 that takes a regular expression and a file as command line arguments and outputs the number of matches for the regular expression within the file. You may limit yourself to regular languages, with the concatenation operator ., the or operator |, and the Kleene star *.


# Instructions on how to use:
To run the application:
Have python installed and set up on the machine.
Clone the repo to your machine - git clone (  https://github.com/DarraghHigginss/Graph_Theory_Repeat  ).
Once the Repo has been cloned ls into the repo.
cd into the project 
In Debian enter in python3 reg.py to see results

Have a script editor such as Visual Studio/Vs code.

# Documentation:

# Questions to be Answered:
Explain the difference between regular expressions in infix notation and those in postfix notation.

Explain how Thompson's construction works for regular expressions.

Explain what is meant by the term irregular language in the context of regular expressions.

1: firstly we can start with identifying what a regular expression is. Regular expressions came about in 1951 from a mathematician known as Stephen Cole Kleene.
   He described regular languages using his mathematical notation called regular events. A regular expression also known as regex, is a string of text that allows you to create      patterns that help match, locate, and manage text. These strings are compared to this pattern to see if they fit the pattern defined by the expression. Regex is a combination      of two types of characters, literals and special characters. Regular expressions are used in search engines, search and replace dialog boxes of word processors and text            editors, examples of this can be seen in Visual studio code in the search function whereby the user can enter in a regular expression into the search box, they can choose to      just find or find and replace a certain item using a regular expression. examples of special characters '' , '^', '$' , '.' , '|' , '?' , '*' , '+' , '(' , ')' '{' '[]'
   Difference between regular expressions in Infix and PostFix Notation.
   Regular expressions in Infix Notation occur where the operators are written in between their operands.  
   Regular expressions in Postfix Notation occur where the operators are used after their operands.
   
2:A State class is created first, which includes a self state, label, arrows, and an accept state. The arrow labels are labeled, the arrows are a list of states to point to, and  accept is a boolean indicating whether or not this is an accept state.After that, an NFA class is created with a self state, start state, and end state that will be used to    check for matches in a match function later.The Shunting Yard Algorithm generated a postfix expression, which was then converted to an NFA via a function. After creating a stack, we loop through the postfix expression from left to right.
 
3: A regular expression is a set of characters that employs a special syntax to find or match other strings or collections of strings. In the UNIX realm, regular expressions are commonly employed In Python, the re module provides full support for Perl-style regular expressions.If an error occurs while compiling or utilizing a regular expression, the 're' module raises the re.error exception. When employed in regular expression, there are a number of characters that have unique meaning.All you need is a lookup table or a finite-state automaton to recognize a regular language. Languages that aren't described by regular grammars are known as non-regular languages. To recognize them, they need more powerful machines than FSAs, up to a Turing machine for an unlimited language. With optional options, the 'MATCH' function tries to match RE pattern to string. re.match(pattern, string, flags=0) Syntax ,Pattern: To be matched regular expression. String: This would be a search for a pattern at the start of the string to match.Flags: You have the option of specifying different flags. With optional flags syntax, the ‘SEARCH' function looks for the first occurrence of the RE pattern within a string. re.search(pattern, string, flags=0) is the syntax.The regular expression to be matched is referred to as the pattern.Unless max is specified, the ‘SUB' function, often known as Search and Replace, replaces all occurrences of the RE pattern in string with repl, substituting all occurrences.This method returns a string that has been changed. The regular phrase to be matched is referred to as the pattern.Max: The maximum number of occurrences that can be substituted.
 
 
 #Research:
 There are two key components to this regular expression project.The Thompson Construction Algorithm and the Shunting Yard Algorithm
To completely comprehend the purpose and significance of these two items, I had to conduct extensive research into what they were and what they meant.
On the course module, there was a lot of information to help explain what these were. I was able to obtain a good understanding of what was required to run this code thanks to the lecture videos.

*Thompsons Construction Algorithm*
The Thompson Construction Algorithm is a method for converting regular phrases into NFA diagrams.
A State class is created first, which includes a self state, label, arrows, and an accept state. The arrow labels are labeled, the arrows are a list of states to point to, and accept is a boolean indicating whether or not this is an accept state.After that, an NFA class is created with a self state, start state, and end state that will be used to check for matches in a match function later.The Shunting Yard Algorithm generated a postfix expression, which was then converted to an NFA via a function. After creating a stack, we loop through the postfix expression from left to right.

*Shunting yard algorithm*
To convert infix to postfix expressions, the Shunting Yard Algorithm is utilized. We implement this by stacking the operators and then reversing their order in the phrase. The operands are all printed after they've been read. If there are any operands among the incoming symbols, print them. If the incoming symbol is a left parenthesis, it will be pushed onto the stack.Remove the right parenthesis from the incoming symbol then pop and print the stack symbols until a left parenthesis appears. Remove and discard the left parenthesis. Push the incoming operator onto the stack if the incoming symbol is an operator and the stack is empty or has a left parenthesis on top.
Push the incoming symbol to the top of the stack if it has a greater precedence than the top-of-the-stack operator or the same precedence as the top-of-the-stack operator and is right associative.Continue to pop the stack until the incoming symbol is not a lower-priority operator than the top-priority operator, or has the same precedence as the top-priority operator and is left associative.At the end of the expression, pop and print all operators on the stack until there are no parentheses left.



#Referenced links:
http://mathcenter.oxford.emory.edu/site/cs171/shuntingYardAlgorithm/
https://medium.com/swlh/visualizing-thompsons-construction-algorithm-for-nfas-step-by-step-f92ef378581b
https://www.computerhope.com/jargon/r/regex.htm
https://www.tutorialspoint.com/python3/python_reg_expressions.htm


