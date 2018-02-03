def simple_html_tag(tag, msg):
    print ('<{0}>{1}</{0}>'.format(tag, msg))
    print ('<{tag_name}>{content}</{tag_name}>'.format(tag_name=tag, content=msg))

# simple_html_tag('h1', 'Simple HEAD Tile~!!')
# --------------------------------------------------------------

def html_tag(tag):
    ''' html_tag(tag): Simple Closure Example
    - What does Closure Function means??
    - double wrapper function aiming to remember (remain) local var.
    '''
    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))
    return wrap_text

def main():
    tag_h1 = html_tag('h1')     # assign to Normal Variable --> turn to FUNC
    # print(tag_h1)               # <function html_tag.<locals>.wrap_text at 0x0252CC00>
    tag_h1('This is the Closure Example~!!')        # Call func = Print
    a = tag_h1('this is Title~!')                   # Assing to = print (the same)
    print(type(tag_h1('this is Title~!')))          # <class 'NoneType'>


numbers = [8, 3, 1, 2, 5, 4, 7, 6,]     # <class 'list'>
group = {2, 3, 5, 7}                    # <class 'set'>

def sort_priority(numbers, group):
    """ simple closure example : double wrapped function
        aimed to remain function as a value
    """
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)    # key = helper() function

numbers.sort()                  # [1, 2, 3, 4, 5, 6, 7, 8]
sort_priority(numbers, group)   # [2, 3, 5, 7, 1, 4, 6, 8]
print(numbers)                  # sorted -> [2, 3, 5, 7, 1, 4, 6, 8]



# if __name__ == '__main__':
#     _a = html_tag.__doc__
#     print(_a)
#     main()
