# *args = argument collector
# it collects all arguments passed

# if you'd like to pass keys
# **kwargs = collecting all arguments with keys

#def my_func(regular_argument, *args, **kwargs):
    # regular_argument = single regular argument
    # *args = list of arguments, multiple arguments
    # **kwargs = dictionary of arguments with key values

    #in the case of regular argument
    #print("hellow world", regular argument)

    #in the case of *args
    #for argument in args:
        #print(argument)



def my_func_args(*argv):
	for arg in argv:
		print(arg)

my_func_args('Welcome', 'to', 'Corinthians')



def func_kwargs(title, **kwargs):
    print(title)
    for key, value in kwargs.items():
        print(key, value)

func_kwargs("Titulo do post", post1="Corinthians campeão brasileiro", post2="Corinthians campeão da Copa do Brasil")