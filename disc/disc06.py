def nonlocalist():
	"""
	>>> prepend, get = nonlocalist()
	>>> prepend(2)
	>>> prepend(3)
	>>> prepend(4)
	>>> get(0)
	4
	>>> get(1)
	3
	>>> get(2)
	2
	>>> prepend(8)
	>>> get(2)
	3
	"""
	get = lambda x: "Index out of range!"
	def prepend(value):
		nonlocal get
		f = get
		def get(i):
			if i == 0:
				return value
			return f(i - x)
	return prepend, lambda x: get(x)

class Email:
	"""Every email object has 3 instance attributes: the
	message, the sender name, and the recipient name.
	"""
	def __init__(self, msg, sender_name, recipient_name):
		self.message = msg
		self.sender_name = sender_name
		self.recipient_name = recipient_name

class Server:
	"""Each Server has an instance attribute clients, which
	is a dictionary that associates client names with
	client objects.
	"""
	def __init__(self):
		self.clients = {}

	def send(self, email):
		"""Take an email and put it in the inbox of the client
		it is addressed to.
		"""
		server.clients[email.recipient_name].receive(email)

	def register_client(self, client, client_name):
		"""Takes a client object and client_name and adds it
		to the clients instance attribute.
		"""
		self.clients[client_name] = client

class Client:
	"""Every Client has instance attributes name (which is
	used for addressing emails to the client), server
	(which is used to send emails out to other clients), and
	inbox (a list of all emails the client has received).
	"""
	def __init__(self, server, name):
		self.inbox = []
		self.name = name
		self.server = server

	def compose(self, msg, recipient_name):
		"""Send an email with the given message msg to the
		given recipient client.
		"""
		self.server.send(Email(msg, self.name, recipient_name))

	def receive(self, email):
		"""Take an email and add it to the inbox of this
		client.
		"""
		self.inbox.append(email)
class Pet():
	def __init__(self, name, owner):
		self.is_alive = True # It's alive!!!
		self.name = name
		self.owner = owner
	def eat(self, thing):
		print(self.name + " ate a " + str(thing) + "!")
	def talk(self):
		print(self.name)

class Dog(Pet):
	def talk(self):
		print(self.name + ' says woof!')

class Cat(Pet):
	def __init__(self, name, owner, lives=9):
		self.name = name
		self.owner = owner
		self.lives = lives
		self.is_alive = True

	def talk(self):
		""" Print out a cat's greeting.
		>>> Cat('Thomas', 'Tammy').talk()
		Thomas says meow!
		"""
		print(self.name + " says meow!")
	
	def lose_life(self):
		"""Decrements a cat's life by 1. When lives reaches zero, 'is_alive'
		becomes False.
		"""
		if self.is_alive == True:
			self.lives = self.lives - 1
			if self.lives < 0:
				self.is_alive = False
		else: 
			print("This cat has no more lives to lose :(")

class NoisyCat(Cat): # Fill me in!
	"""A Cat that repeats things twice."""
	
	def talk(self):
		"""Talks twice as much as a regular cat.
		>>> NoisyCat('Magic', 'James').talk()
		Magic says meow!
		Magic says meow!
		"""
		Cat.talk(self)
		Cat.talk(self)

class Foo:

	def __init__(self, bar):
		self.bar = bar

	def g(self, x):
		return self.bar + x










