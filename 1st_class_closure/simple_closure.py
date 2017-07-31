def simple_html_tag(tag, msg):
    print ('<{0}>{1}</{0}>'.format(tag, msg))
    print ('<{tag_name}>{content}</{tag_name}>'.format(tag_name=tag, content=msg))


# simple_html_tag('h1', 'Simple HEAD Tile~!!')
# --------------------------------------------------------------

''' Simple Closure Example
    - What does Closer Function means??
    - double wrapper function aiming to remember (remain) local var.
'''
def html_tag(tag):
    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))
    return wrap_text

def main():
    tag_h1 = html_tag('h1')     # assign to Normal Variable --> turn to FUNC
    # print(tag_h1)               # <function html_tag.<locals>.wrap_text at 0x0252CC00>

    tag_h1('This is the Closure Example~!!')        # Call func = Print
    a = tag_h1('this is Title~!')                   # Assing to = print (the same)

    print(type(tag_h1('this is Title~!')))          # <class 'NoneType'>


if __name__ == '__main__':
    main()
