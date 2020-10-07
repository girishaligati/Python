import os
from os.path import join

def list_files(inputpath = os.getcwd(),extension = None):
    '''Lists all the files that are in the inputpath. 
        Works as ls in unix
        extension = 'txt' or ['txt','log'] can be passed '''
    for root,dirs,files in os.walk(inputpath):
        for f in files:
            if extension == None:
                yield os.path.join(root,f)
            elif f.split('.')[-1] in extension:
                yield os.path.join(root,f)
            else: ...

def count_file_types(inputpath=os.getcwd(),extension = 'txt'):
    '''Lists all the files types based on the extension. By Default 'txt' is considered'''
    if (isinstance(extension,(list,tuple,set))):
        for ext in extension:
            return(ext +' === '+ str(sum(1 for _ in list_files(inputpath,ext))))
    elif(isinstance(extension,(str))):
        return(extension +' === '+str(sum(1 for _ in list_files(inputpath,extension))))


def read_file(filename):
    for line in open(filename):
        yield line

def file_length(filename):
    return sum(1 for line in read_file(filename))

def insignificant_lines(filename):
    return sum(1 for line in read_file(filename) if len(line.strip()) == 0 and line.strip().startswith('#'))

def significant_lines(filename):
    return sum(1 for line in read_file(filename) if len(line.strip()) > 0 and not line.strip().startswith("#"))

def line_of_length(filename,length_line=0):
    return sum(1 for line in read_file(filename) if len(line.strip())>=length_line)

def locate(filename,inputpath=os.getcwd()):
    for _file in list_files(inputpath,extension=None):
        if _file.lower().endswith(filename.lower()):
            return(_file)
    # return any(True for _file in list_files(inputpath,extension=None) if _file.lower().endswith(filename.lower()))

def grep(inputpath=os.getcwd(),pattern=None,extension=None):
    for f in list_files(inputpath,extension):
        for line in read_file(f):
            if pattern in line:
                print(f+' === '+line)

    

# print(count_file_types(extension='log'))
# print(locate('getlines.py'))
# for f in list_files(extension=None):
    # count_files_type(extension='log')
    # print(f,length_file(f),significant_lines(f),line_of_length(f,150),cnt_files_type(extension = 'log'),search_file('itators.py'))

# grep(pattern='Girish Kumar')
# print(locate('FileHandling','C:\8780076\Vagrant'))