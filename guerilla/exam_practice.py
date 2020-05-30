def eval_with_add(t):
	if t.entry == '+':
		return sum(t.branches[0], t.branches[1])