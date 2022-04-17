import re
from pathlib import Path

from StmtTypes import *

class SourceGenerator:
	classifiers = [Macro, Comment, Function, Class]
	
	def classify_statement(self, stmt):
		for classifier in self.classifiers:
			if classifier.regex.search(stmt):
				classification = classifier(stmt)
				return classification.generate_source()
		return ""

	def generate(self, path):
		with open(path, "r") as header:
			text = header.read()
			source = ""
			for stmt in text.split(";"):
				source += self.classify_statement(re.sub(r"[\r\n]+", "", stmt))
			
			header_path = Path(path)
			output_path = header_path.with_suffix(".cpp")
			with open(output_path, "w") as source_file:
				source_file.write(source)
