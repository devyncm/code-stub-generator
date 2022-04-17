import re

cpp_return_defaults = {
	"bool": "false", 
	"char": "null", 
	"int": "0", 
	"float": "0.0", 
	"double": "0.0", 
	"void": None,
	"std::string": '""' 
}

class Macro:
	regex = re.compile(r"^#")
	base = None
	
	def __init__(self, base):
		self.base = base
	
	def generate_source(self):
		return ""

class Comment:
	regex = re.compile(r"^\/\/")
	base = None
	
	def __init__(self, base):
		self.base = base
		
	def generate_source(self):
		return ""

class Function:
	regex = re.compile(r"\S* \S*\s*\(.*\)")
	base = None
	
	def __init__(self, base):
		self.base = base
		
		parts = re.split(r"[ ()]+", self.base)
		parts = [part for part in parts if part]
		
		self.return_type = parts[0]
		self.name = parts[1]
		
	
	def generate_source(self):
		output = self.base + "{\n\t"
		if self.return_type in cpp_return_defaults and cpp_return_defaults[self.return_type]:
			output += "return " + cpp_return_defaults[self.return_type] + ";"
		else:
			output += "return " + self.return_type + ";"
		output += "\n}\n"
		return output

class Class:
	regex = re.compile("(class)\s.*")
	base = None
	
	def __init__(self, base):
		self.base = base
	
	def generate_source(self):
		return ""
