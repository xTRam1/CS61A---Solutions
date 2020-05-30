class Link:
	empty = ()
	
	def __init__(self, first, rest=empty):
		assert rest is Link.empty or isinstance(rest, Link)
		self.first = first
		self.rest = rest

	def __len__(self):
		if self.rest == ():
			return 1
		return 1 + Link.__len__(self.rest)

	def __getitem__(self, item):
		assert item <= Link.__len__(self)
		if item == 0:
			return self.first
		return Link.__getitem__(self.rest, item - 1)
	
	def __repr__(self):
		if self.rest:
			rest_str = ', ' + repr(self.rest)
		else:
			rest_str = ''
		return 'Link({0}{1})'.format(repr(self.first), rest_str)
	
	def __str__(self):
		string = '<'
		while self.rest is not Link.empty:
			string += str(self.first) + ' '
		self = self.rest
		return string + str(self.first) + '>'


def is_palindrome(seq):
	""" Returns True if the sequence is a palindrome. A palindrome is a sequence
	that reads the same forwards as backwards
	>>> is_palindrome(Link("l", Link("i", Link("n", Link("k")))))
	False
	>>> is_palindrome(["l", "i", "n", "k"])
	False
	>>> is_palindrome("link")
	False
	>>> is_palindrome(Link.empty)
	True
	>>> is_palindrome([])
	True
	>>> is_palindrome("")
	True
	>>> is_palindrome(Link("a", Link("v", Link("a"))))
	True
	>>> is_palindrome(["a", "v", "a"])
	True
	>>> is_palindrome("ava")
	True
	"""
	for i in range(len(seq) // 2):
		first = seq[i]
		last = seq[len(seq) - 1 - i]
		if first is not last:
			return False
	return True

def sum_nums(lnk):
	"""
	>>> a = Link(1, Link(6, Link(7)))
	>>> sum_nums(a)
	14
	"""
	if lnk is Link.empty:
		return 0
	return lnk.first + sum_nums(lnk.rest)	

def multiply_lnks(lst_of_lnks):
	"""
	>>> a = Link(2, Link(3, Link(5)))
	>>> b = Link(6, Link(4, Link(2)))
	>>> c = Link(4, Link(1, Link(0, Link(2))))
	>>> p = multiply_lnks([a, b, c])
	>>> p.first
	48
	>>> p.rest.first
	12
	>>> p.rest.rest.rest is Link.empty
	True
	"""
	product = 1
	for link in lst_of_lnks:
		product = product * link.first

	if True in [link.rest == Link.empty for link in lst_of_lnks]:
		return Link(product)
	else:
		new_list = [link.rest for link in lst_of_lnks]
		return Link(product, multiply_lnks(new_list))

def filter_link(link, f):
	"""
	>>> link = Link(1, Link(2, Link(3)))
	>>> g = filter_link(link, lambda x: x % 2 == 0)
	>>> next(g)
	2
	>>> next(g)
	StopIteration
	>>> list(filter_link(link, lambda x: x % 2 != 0))
	[1, 3]
	"""
	while link is not Link.empty:
		if f(link.first):
			yield link.first
		link = link.rest

def filter_no_iter(link, f):
	"""
	>>> link = Link(1, Link(2, Link(3)))
	>>> list(filter_no_iter(link, lambda x: x % 2 != 0))
	[1, 3]
	"""
	if link is Link.empty:
		return
	elif f(link.first):
		yield link.first
	yield from filter_no_iter(link.rest, f)

def sum_paths_gen(t):
	"""
	>>> t1 = Tree(5)
	>>> next(sum_paths_gen(t1))
	5
	>>> t2 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(9)])
	>>> sorted(sum_paths_gen(t2))
	[6, 7, 10]
	"""
	if t.is_leaf():
		yield t.label
	for b in t.branches:
		for low_sum in sum_paths_gen(b):
			yield low_sum + t.label

class Tree:
	
	def __init__(self, label, branches=[]):
		assert False not in [isinstance(x, Tree) for x in branches] or branches == []
		self.label = label
		self.branches = branches

	def __repr__(self):
		if self.is_leaf():
			return "Tree({0})".format(self.label)
		rest = "Tree({0}".format(self.label)
		for b in self.branches:
			return rest + ',' + repr(b) + ')'

	def is_leaf(self):
		return not self.branches



