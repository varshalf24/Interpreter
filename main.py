import sys, traceback
from optparse import OptionParser
from interpret import Interpreter, Repl
from common import Error

parser = OptionParser(usage='Usage: main.py  filename')

(options, args) = parser.parse_args()

if len(args) > 1:
    parser.print_help()
    sys.exit(1)

io = None

if args:
    vm = Interpreter.from_file(args[0], history=20, io=io)
else:
    print 'FileName is required'
