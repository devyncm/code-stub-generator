import sys

from SourceGenerator import SourceGenerator

if len(sys.argv) < 2:
	import mainGUI

srcgen = SourceGenerator()
for path in sys.argv[1:]:
	srcgen.generate(path)
