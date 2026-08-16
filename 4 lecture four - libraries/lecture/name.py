# FROM LECTURE
# FROM 19:13

# command-line arguments
# the sys module 
# mainly used to input values into the application without prompting using sys.argv[].
# using the command line will feel faster as you get more comfortable programming,
# ie entering values on the command line might be faster for testing different values
# as opposed to constantly entering values in an input prompt.

'''
>>> dir(sys)
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', 
 '__spec__', '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__', '_base_executable', '_baserepl', '_clear_internal_caches', 
 '_clear_type_cache', '_clear_type_descriptors', '_current_exceptions', '_current_frames', '_debugmallocstats', '_dump_tracelets', 
 '_enablelegacywindowsfsencoding', '_framework', '_get_cpu_count_config', '_getframe', '_getframemodulename', '_git', '_home', '_is_gil_enabled', 
 '_is_immortal', '_is_interned', '_jit', '_setprofileallthreads', '_settraceallthreads', '_stdlib_dir', '_vpath', '_xoptions', 
 'activate_stack_trampoline', 'addaudithook', 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 
 'builtin_module_names', 'byteorder', 'call_tracing', 'copyright', 'deactivate_stack_trampoline', 'displayhook', 'dllhandle', 
 'dont_write_bytecode', 'exc_info', 'excepthook', 'exception', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 
 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth', 'get_int_max_str_digits', 'getallocatedblocks', 'getdefaultencoding', 
 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 
 'gettrace', 'getunicodeinternedsize', 'getwindowsversion', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 
 'is_remote_debug_enabled', 'is_stack_trampoline_active', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'monitoring', 'orig_argv', 'path', 
 'path_hooks', 'path_importer_cache', 'platform', 'platlibdir', 'prefix', 'ps1', 'ps2', 'pycache_prefix', 'remote_exec', 'set_asyncgen_hooks', 
 'set_coroutine_origin_tracking_depth', 'set_int_max_str_digits', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 
 'stdin', 'stdlib_module_names', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info', 'warnoptions', 'winver']
 '''


import sys

# print("hello, my name is", sys.argv[1])
# input in the interpreter: python name.py Lincia
# output would be "hello, my name is Lincia"

# sys.argv[1] pulls the name i put on the intepreter line 
# because the name of the file is stored at index 0


print(sys.argv)
# input in the interpreter: python name.py Lincia
# output is ['name.py', 'Lincia']


# the below can give an indexError as that's one of the 
# most common errors whenever you're dealing with a list, dict, tuple etc
# to prevent this, we can use a try-except block 
# try:
#     print("hello, my name is", sys.argv[1])
# except IndexError:
#     print("Too few arguments")




# we can also write an if-elif-else block to get around this.
# you don't always have to do a try-exception block if you 
# can succintly and intelligently take care of the things you're
# worried about using a conditional.
# this way, we can also instruct the user a little better
# we can't have multiple else statemets
# if len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")
# else:
#     print("hello, my name is", sys.argv[1])



# if we remove the else block like below, to separate different parts of the code,
# we'll get an IndexError if nothing is inputted because the print statement will 
# always try to go for the first index despite us checking the length in the conditional
# Check for errors
# if len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")

# Print name tags
# print("hello, my name is", sys.argv[1])




# to fix the above bug, we can use sys.exit as below
# Check for errors
# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")

# Print name tags
# print("hello, my name is", sys.argv[1])




# this is a way to print more than one name inputted
# this prints the program name (name.py) store at index 0 though
# Check for errors
# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")

# Print name tags
# for arg in sys.argv:
#     print("hello, my name is", arg)




# to remove index 0 (the name of the program), we can use slicing as below
# SLICING
# Check for errors
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

# Print name tags
for arg in sys.argv[1:]:
    print("hello, my name is", arg)




