quiz_data = [
    {
        "question": "What is the correct way to print 'Hello, World!' in Python?",
        "choices": ["print('Hello, World!')", "echo 'Hello, World!'", "printf('Hello, World!')", "System.out.println('Hello, World!')"],
        "answer": "print('Hello, World!')"
    },
    {
        "question": "What data type is the result of: type(5)?",
        "choices": ["int", "float", "str", "type"],
        "answer": "int"
    },
    {
        "question": "Which of the following is used to create a list in Python?",
        "choices": ["{}", "[]", "||", "()"],
        "answer": "[]"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "choices": ["function", "def", "fun", "lambda"],
        "answer": "def"
    },
    {
        "question": "What is the output of len('Python')?",
        "choices": ["6", "5", "7", "Error"],
        "answer": "6"
    },
    {
        "question": "Which symbol is used to comment in Python?",
        "choices": ["//", "/* */", "#", "--"],
        "answer": "#"
    },
    {
        "question": "How do you start a for loop in Python?",
        "choices": ["for (i = 0; i < 10; i++)", "foreach i in range(10)", "for i in range(10):", "loop i in range(10)"],
        "answer": "for i in range(10):"
    },
    {
        "question": "What will be the result of 7 // 2?",
        "choices": ["3.5", "3", "2", "Error"],
        "answer": "3"
    },
    {
        "question": "How do you create a variable in Python?",
        "choices": ["int x = 5", "x = 5", "var x = 5", "let x = 5"],
        "answer": "x = 5"
    },
    {
        "question": "What is the output of 'Python'[-1]?",
        "choices": ["P", "n", "h", "Error"],
        "answer": "n"
    },
    {
        "question": "Which of these is a valid Python variable name?",
        "choices": ["1variable", "variable_name", "variable-name", "variable name"],
        "answer": "variable_name"
    },
    {
        "question": "What is the correct file extension for Python files?",
        "choices": [".py", ".python", ".pt", ".txt"],
        "answer": ".py"
    },
    {
        "question": "Which of the following is not a keyword in Python?",
        "choices": ["if", "while", "for", "switch"],
        "answer": "switch"
    },
    {
        "question": "What is the output of bool(0)?",
        "choices": ["True", "False", "0", "Error"],
        "answer": "False"
    },
    {
        "question": "How do you create a single-line string in Python?",
        "choices": ["Single quotes or double quotes", "Triple quotes", "Curly braces", "Square brackets"],
        "answer": "Single quotes or double quotes"
    },
    {
        "question": "Which function is used to get the length of a list?",
        "choices": ["size()", "len()", "length()", "count()"],
        "answer": "len()"
    },
    {
        "question": "What is the result of 2 ** 3?",
        "choices": ["6", "8", "9", "Error"],
        "answer": "8"
    },
    {
        "question": "Which function is used to read input from the user?",
        "choices": ["scanf()", "input()", "read()", "get()"],
        "answer": "input()"
    },
    {
        "question": "What does the pass statement do?",
        "choices": ["Skips the loop", "Exits the program", "Does nothing", "Stops execution"],
        "answer": "Does nothing"
    },
    {
        "question": "Which of the following is mutable?",
        "choices": ["tuple", "list", "string", "int"],
        "answer": "list"
    },
    {
        "question": "What is the output of 3 * 'Python'?",
        "choices": ["'PythonPythonPython'", "Error", "['Python', 'Python', 'Python']", "'Python*Python*Python'"],
        "answer": "'PythonPythonPython'"
    },
    {
        "question": "Which method can be used to convert a string to lowercase?",
        "choices": ["lower()", "toLower()", "tolowercase()", "convert_lower()"],
        "answer": "lower()"
    },
    {
        "question": "What does the 'break' keyword do in Python?",
        "choices": ["Ends the program", "Exits the current loop", "Pauses the loop", "Skips the current iteration"],
        "answer": "Exits the current loop"
    },
    {
        "question": "How do you create a dictionary in Python?",
        "choices": ["Using {}", "Using []", "Using ()", "Using ||"],
        "answer": "Using {}"
    },
    {
        "question": "Which operator is used for exponentiation in Python?",
        "choices": ["^", "**", "pow()", "exp"],
        "answer": "**"
    },
    {
        "question": "What is the output of type([1, 2, 3])?",
        "choices": ["list", "array", "tuple", "dict"],
        "answer": "list"
    },
    {
        "question": "How do you start a block of code in Python?",
        "choices": ["Using indentation", "Using curly braces {}", "Using square brackets []", "Using parentheses ()"],
        "answer": "Using indentation"
    },
    {
        "question": "What will be the output of 10 % 3?",
        "choices": ["1", "3", "10", "Error"],
        "answer": "1"
    },
    {
        "question": "What is the output of 'Python'.upper()?",
        "choices": ["python", "PYTHON", "Python", "Error"],
        "answer": "PYTHON"
    },
    {
        "question": "How do you handle exceptions in Python?",
        "choices": ["Using if-else statements", "Using try-except blocks", "Using loops", "Using error handling functions"],
        "answer": "Using try-except blocks"
    },
    {
        "question": "What does the 'append()' method do in a list?",
        "choices": ["Adds an element to the end of the list", "Removes the last element", "Sorts the list", "Adds an element at a specific position"],
        "answer": "Adds an element to the end of the list"
    },
    {
        "question": "What is the purpose of the 'return' statement in Python?",
        "choices": ["To print output", "To terminate a loop", "To exit a function and return a value", "To handle exceptions"],
        "answer": "To exit a function and return a value"
    },
    {
        "question": "Which of the following is an immutable data type?",
        "choices": ["list", "set", "tuple", "dictionary"],
        "answer": "tuple"
    },
    {
        "question": "Which method is used to remove an item from a dictionary?",
        "choices": ["delete()", "remove()", "pop()", "discard()"],
        "answer": "pop()"
    },
    {
        "question": "What will be the output of bool([])?",
        "choices": ["True", "False", "None", "Error"],
        "answer": "False"
    },
    {
        "question": "Which of the following is a Python tuple?",
        "choices": ["[1, 2, 3]", "{1, 2, 3}", "(1, 2, 3)", "1, 2, 3"],
        "answer": "(1, 2, 3)"
    },
    {
        "question": "What does 'is' compare in Python?",
        "choices": ["Values", "Memory locations", "Data types", "Lengths"],
        "answer": "Memory locations"
    },
    {
        "question": "Which module is used to generate random numbers in Python?",
        "choices": ["math", "random", "os", "time"],
        "answer": "random"
    },
    {
        "question": "What is the output of int('5.5')?",
        "choices": ["5", "5.5", "Error", "None"],
        "answer": "Error"
    },
    {
        "question": "How do you create a set in Python?",
        "choices": ["Using {}", "Using []", "Using ()", "Using ||"],
        "answer": "Using {}"
    }
]
