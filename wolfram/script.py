input_data = open("input.txt", "r")
output_html = open("output.html", "w")
output_css = open("output.css", "w")

# Read in from file
elements = []
for line in input_data:
    temp = line.split(" ")
    elements.append(temp)

# HTML specific functions
def html_header():
    output_html.wrote("<!DOCTYPE html>\n")

def html_open():
    output_html.write("<html>\n")

def html_close():
    output_html.write("</html>\n")

def head_open():
    output_html.write("<head>\n")

def head_close():
    output_html.write("</head>\n")

def body_open():
    output_html.write("<body>\n")

def body_close():
    output_html.write("</body>\n")

def div_open(value):
    output_html.write("<div class=" + value + ">\n")

def div_close():
    output_html.write("</div>\n")

def paragraph_open():
    output_html.write("<p>\n")

def paragraph_close():
    output_html.write("</p>\n")

def header_open(value):
    output_html.write("<h" + value + ">\n")

def header_close(value):
    output_html.write("</h" + value + ">\n")
    
def button_html():
    output_html.write("<a href=\"#\" class=\"btn btn-primary btn-default\">Button</a>\n")

def img_html(x, y):
    output_html.write("<img src=\"http://www.placehold.it/" + x + "x" + y + "\">\n")

def html_includeCSS():
    output_html.write("<link rel=\"stylesheet\" type=\"text/css\" href=\"output_css.\">")

def html_baseSetup():
    output_html.write("<meta charset=\"utf-8\">\n")
    output_html.write("<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n")
    output_html.write("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n")
    output_html.write("<meta name=\"description\" content=\"\">\n")
    output_html.write("<meta name=\"author\" content=\"\">\n")

def html_baseCSSDependencies():
    output_html.write("<link href=\"css/bootstrap.min.css\" rel=\"stylesheet\">\n")

def html_baseJSDependencies():
    output_html.write("<script src=\"js/jquery.js\"></script>\n")
    output_html.write("<script src=\"js/bootstrap.min.js\"></script>\n")
    

# CSS specific functions

def css_open(tag):
    output_css.write("." + tag + " {")

def css_close():
    output_css.write("}")

def css_color(value):
    output_css.write("color: " + value + ";")

def css_backgroundColor(value):
    output_css.write("background-color: " + value + ";")

def css_position(value):
    output_css.write("position: " + value + ";")

def css_right(value):
    output_css.write("right: " + value + ";")

def css_top(value):
    output_css.write("top: " + value + ";")


html_header()
html_open()
head_open()
html_baseSetup()



