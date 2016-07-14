def p_decorate(func):
	def func_wrapper(*args, **kwargs):
		return "<p>{0}</p>".format(func(*args, **kwargs))
	return func_wrapper

def strong_decorate(func):
    def func_wrapper(*args, **kwargs):
        return "<strong>{0}</strong>".format(func(*args, **kwargs))
    return func_wrapper

def div_decorate(func):
    def func_wrapper(*args, **kwargs):
        return "<div>{0}</div>".format(func(*args, **kwargs))
    return func_wrapper

class Person(object):
	def __init__(self):
		self.name = "John"
		self.family = "Doe"

	@div_decorate
	@p_decorate
	@strong_decorate
	def get_fullname(self):
		"""HOLOOOOOOOOOOO"""
		return self.name+" "+self.family

my_person = Person()
print my_person.get_fullname()

def tags(tag_name):
	def tags_decorator(func):
		def func_wrapper(name):
			"""SHIT!!!!!!!!!"""
			return "<{0}>{1}</{0}>".format(tag_name, func(name))
		return func_wrapper
	return tags_decorator

@tags("div")
@tags("p")
@tags("strong")
def get_text(name):
	return "Hello "+name

print get_text("John")
print get_text.__name__
print get_text.__doc__
print get_text.__module__

from functools import wraps

def tags(tag_name):
	def tags_decorator(func):
		@wraps(func)
		def func_wrapper(name):
			return "<{0}>{1}</{0}>".format(tag_name, func(name))
		return func_wrapper
	return tags_decorator

@tags("div")
@tags("p")
@tags("strong")
def get_text(name):
	"""returns BITCH"""
	return "Hello "+name

print get_text("see this fist???")
print get_text.__name__
print get_text.__doc__
print get_text.__module__

class myDecorator(object):
	def __init__(self, f):
		print "inside myDecorator.__init__()"
		self.func = f # Prove that function definition has completed

	def __call__(self):
		print "OVER HERE "+self.func.__name__
		print "inside myDecorator.__call__()"
		self.func()

@myDecorator
def aFunction():
	print "inside aFunction()"

print "Finished decorating aFunction()"

aFunction()

class entryExit(object):
	def __init__(self, f):
		self.f = f

	def __call__(self):
		print "Entering", self.f.__name__
		self.f()
		print "Exited", self.f.__name__

@entryExit
def func1():
	print "inside func1()"

@entryExit
def func2():
	print "inside func2()"

func1()
func2()

def simple_decorator(decorator):
	def new_decorator(f):
		g = decorator(f)
		g.__name__ = f.__name__
		g.__doc__ = f.__doc__
		g.__dict__.update(f.__dict__)
		return g
	new_decorator.__name__ = decorator.__name__
	new_decorator.__doc__ = decorator.__doc__
	new_decorator.__dict__.update(decorator.__dict__)
	return new_decorator

@simple_decorator
def my_simple_logging_decorator(func):
	def you_will_never_see_this_name(*args, **kwargs):
		print 'calling the {0} bitch'.format(func.__name__)
		return func(*args, **kwargs)
	return you_will_never_see_this_name

@my_simple_logging_decorator
def double(x):
	'Doubles a number.'
	return 2 * x
 
assert double.__name__ == 'double'
assert double.__doc__ == 'Doubles a number.'
print double(155)