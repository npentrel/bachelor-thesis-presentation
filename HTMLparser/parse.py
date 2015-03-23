from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

# DEBUG-OPTIONS
DEBUG_ALL = 0
DEBUG_TITLE = 0

# STACK
tag_stack = []

# TEXT-VARIABLES
title = ""
subtitle = ""
text = []
offset = 0

#HTML for JSImpress Boilerplate


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if DEBUG_ALL:
            print "Start tag:", tag
        tag_stack.append(tag)
        for attr in attrs:
            if DEBUG_ALL:
                print "     attr:", attr
    def handle_endtag(self, tag):
        if DEBUG_ALL:
            print "End tag  :", tag
        tag_stack.pop()
    def handle_data(self, data):
        global title
        if (tag_stack[top()] == "dc:title"):
            title = data
            if DEBUG_TITLE:
                print tag_stack[top()] ,"Data     :", data
    def handle_comment(self, data):
        if DEBUG_ALL | DEBUG_TITLE:
            print "Comment  :", data
    def handle_entityref(self, name):
        c = unichr(name2codepoint[name])
        if DEBUG_ALL:
            print "Named ent:", c
    def handle_charref(self, name):
        if name.startswith('x'):
            c = unichr(int(name[1:], 16))
        else:
            c = unichr(int(name))
        if DEBUG_ALL:
            print "Num ent  :", c
    def handle_decl(self, data):
        if DEBUG_ALL:
            print "Decl     :", data

#HELPER FUNCTIONS
def top():
    return (len(tag_stack)-1)

def file_strip(file_name, out):
    input_file = open(file_name, 'r')
    for line in input_file:
        pass
    last = line
    input_file = open(file_name, 'r')
    header = 6
    for line in input_file:
        if header:
            header-=1 # just use everything after line 1
        else:
            if (line != last):
                out.write(line)


def presentation_beginning_boilerplate(title, out):
    out.write('<html><head><title>')
    out.write(title)
    out.write('<meta http-equiv="Content-Type" content="text/html;'
        ' charset=UTF-8"> <link href="styles.css" rel="stylesheet" /> </head>'
        '<body> <div id="impress"> <div class="no-support-message"> Sorry! Your'
        ' browser is unable to load this Impress presentation. Please update'
        ' your browser. </div>')

def presentation_slide(title, div, out):
    global offset
    out.write('<div class="step" data-y="')
    out.write(str(offset))
    offset += 1000
    out.write('">')
    out.write(div)
    out.write('</div>')

def presentation_end(out):
    out.write('</div></div><script type="text/javascript" src="impress.js">'
        '</script></body></html>')

def create_presentation():
    out = open('output/out.html', 'w')
    presentation_beginning_boilerplate("Hello World!", out)
    presentation_slide("hello", "<div>test</div>", out)

    file_name = '../export/planetary/narration/measurements/measurement.html'
    file_strip(file_name, out)
#    parser = MyHTMLParser()
#    f = open('../export/planetary/narration/measurements/measurement.html', 'r')
    # print f

 #   for line in f:
 #       parser.feed(line)


    presentation_end(out)



create_presentation()


print "-----------------------------------------------------------"
print "-----------------------------------------------------------"
print "TITLE: ", title
for t in text:
    print t
# https://docs.python.org/2/library/htmlparser.html