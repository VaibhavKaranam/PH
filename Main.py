#!/usr/bin/env python
import webbrowser
import os

# KeyWords
KeyWordsDict = {'Mathematics': {'Misc': ['solve', 'equation', 'inequality', 'find', 'prove', 'algebraic',
                                         'algebra', 'expression']},
                'Physics': {'Misc': ['velocity']},
                'Environmental Science': {'Misc': ['renewable']},
                'Chemistry': {'Misc': ['solution']},
                'Computer Science': {'Misc': ['algorithm'],
                                     'Back End': ['django', 'node.js', 'flask', 'java', 'python', 'ruby',
                                                  'scala', 'swift', 'c', 'pascal', 'go', 'groovy''AI'],
                                     'Front End': ['javascript', 'html', 'css', 'design', 'jquery', 'UI', 'UX',
                                                   'Angular', 'copy pasting', 'web fonts']},
                'Sports': {'Misc': ['lineup', 'starters', 'tennis', 'boxing', 'wii sports']}
}


# Classes
class Employee:
	
	def __init__(self, name, email, number, rating, skill=""):
		self.name = name
		self.email = email
		self.number = number
		self.skill = skill
		self.rating = rating
		self.task = ""
		pass
	
	def __str__(self):
		return "Employee - %s at %s and %s, Rating of %s at %s." \
			% (self.name, self.email, self.number,self.rating, self.skill)
	
	def assign_task(self, task):
		self.task = task
		pass


# List of Employees
EmployeesList = []

# Dictionary of Task and Their Difficulty Levels
TasksList = []


# Error Message
def error(type):
	print("Error: %s" % type)


# Adding Employees
def add_employee(name, email, number, rating, skill):
	if name.len() > 50 or name.len() < 1:
		error("Character limit for name is 50 letters")
	if rating > 10 or rating < 1:
		error("Rate must be a value between 1 and 10")
	new_employee = Employee(name, email, number, rating, skill)
	EmployeesList.append(new_employee)


# Printing List of Employees
def print_employees():
	for employee in EmployeesList:
		print(employee)


# Break Down of the Task
def break_task(task):
	for job_type in KeyWordsDict.keys():
		for job_type_genre in KeyWordsDict[job_type].keys():
			for word in KeyWordsDict[job_type][job_type_genre]:
				if word in task:
					if job_type_genre == "Misc":
						return job_type
					else:
						return job_type_genre


def open_website(url):
	webbrowser.open(url=url)


headers = ["Content-type: text/html"]
qs = os.environ['QUERY_STRING']

def send_headers():
	for h in headers:
		print(h)
		print("\n")

def send_form():
	    print ('''
	    <html>
	      <body>
	          <form action='cgi-bin/hellobetter.py' method='get'>
	              <label for="myname">Enter Your Name</label>
	              <input id="myname" type="text" name="firstname" value="Nada" />
	              <input type="submit">
	          </form>
	      </body>
	    </html>
	    ''')

def send_page(name):
	print('''
	<html>
	      <body>
	      <h1>Hello {0}</h1>
	      </body>
	      </html>
	      '''.format(name))


if not qs:
	send_headers()
	send_form()
else:
	if 'firstname' in qs:
		name = qs.split('=')[1]
	else:
		name = 'No Name Provided'
		send_headers()
		send_page(name)
