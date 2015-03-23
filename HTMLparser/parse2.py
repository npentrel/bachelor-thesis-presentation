from lxml import html
# import requests

# DEBUG-OPTIONS
DEBUG_ALL = 1
DEBUG_TITLE = 0

# STACK
tag_stack = []

# TEXT-VARIABLES
title = ""
subtitle = ""
text = []


def presentation_beginning_boilerplate(title, out):
    out.write('<html><head><title>')
    out.write(title)
    out.write('<meta http-equiv="Content-Type" content="text/html;'
        ' charset=UTF-8"> <link href="styles.css" rel="stylesheet" /> </head>'
        '<body> <div id="impress"> <div class="no-support-message"> Sorry! Your'
        ' browser is unable to load this Impress presentation. Please update'
        ' your browser. </div>')

def presentation_slide(title, div, out):
    out.write('<div class="step">')
    out.write(div)
    out.write('</div>')

def presentation_end(out):
    out.write('</div></div><script type="text/javascript" src="impress.js">'
        '</script></body></html>')

def create_presentation():
    out = open('output/out.html', 'w')
    presentation_beginning_boilerplate("Hello World!", out)
    presentation_slide("hello", "<div>test</div>", out)

    # file_name = '../export/planetary/narration/measurements/measurement.html'
    # file_strip(file_name, out)
    presentation_end(out)





f = open('../export/planetary/narration/measurements/measurement.html', 'r')

data=f.read().replace('\n', '')
tree = html.fromstring(data)
test = tree.xpath('//p/text()')
print (test)

# for line in f:
#    parser.feed(line)

# create_presentation()


print ("-----------------------------------------------------------")
print ("-----------------------------------------------------------")
print ("TITLE: ", title)
for t in text:
    print (t)
# https://docs.python.org/2/library/htmlparser.html