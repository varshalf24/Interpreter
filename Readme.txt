Interpreter for Python
	
	The project is intended to interpret the python code written in python language. To execute the python code we need to run the below command

			“python main.py [fileName.py]”

The interpreter first parses the input file given by parse.py file and then after parsing organize them as tokens by tokens.py file. In the tokens file,
The syntax tree structure is formed based on the operation and the priority given in the common.py. Then the interpreter.py files interpretes the flattened tree
Structure and gives the output. 

