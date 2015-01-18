input_data = open("input.txt", "r")
output_html = open("output.html", "w")
output_css = open("output.css", "w")

# Read in from file
elements = []
for line in input_data:
    temp = line.split(" ")
    elements.append(temp)
    print temp

# HTML specific functions
def html_header():
    output_html.write("<!DOCTYPE html>\n")

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
    output_html.write("<div class=" + "\"" + value + "\""+ ">\n")

def div_close():
    output_html.write("</div>\n")

def paragraph_open():
    output_html.write("<p>\n")

def paragraph_close():
    output_html.write("</p>\n")

def place_text(text):
    output_html.write(text + "\n")

def header_open(value):
    output_html.write("<h" + value + ">\n")

def header_close(value):
    output_html.write("</h" + value + ">\n")
    
def button_html(value):
    output_html.write("<a href=\"#\" class=\"btn btn-" + value + " btn-default\">Sample Button</a>\n")

def img_html(x, y):
    output_html.write("<img src=\"http://www.placehold.it/" + x + "x" + y + "\">\n")

def html_includeCSS():
    output_html.write("<link rel=\"stylesheet\" type=\"text/css\" href=\"output_css.css\">")

def html_baseSetup():
    output_html.write("<meta charset=\"utf-8\">\n")
    output_html.write("<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n")
    output_html.write("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n")
    output_html.write("<meta name=\"description\" content=\"\">\n")
    output_html.write("<meta name=\"author\" content=\"\">\n")

def html_baseCSSDependencies():
    output_html.write("<link href=\"bootstrap.min.css\" rel=\"stylesheet\">\n")

def html_baseJSDependencies():
    output_html.write("<script src=\"jquery.js\"></script>\n")
    output_html.write("<script src=\"bootstrap.min.js\"></script>\n")
    

# CSS specific functions

def css_open(tag):
    output_css.write("." + tag + " {\n")

def css_close():
    output_css.write("}\n")

def css_color(value):
    output_css.write("color: " + value + ";\n")

def css_backgroundColor(value):
    output_css.write("background-color: " + value + ";\n")

def css_position(value):
    output_css.write("position: " + value + ";\n")

def css_height(value):
    output_css.write("height: " + value + "px;\n")

def css_width(value):
    output_css.write("width: " + value + "px;\n")

def css_left(value):
    output_css.write("left: " + value + "px;\n")

def css_top(value):
    output_css.write("top: " + value + "px;\n")


html_header()
html_open()
head_open()
html_baseSetup()
html_includeCSS()
html_baseCSSDependencies()
head_close()
body_open()

print "starting loop"
for x in range(len(elements)):
    print "iteration" + str(x)
    temp = elements[x]
    if (temp[0] == "text"):
        idVal = "text" + str(x)
        position = "absolute"
        size = str(temp[1])
        color = temp[2]
        left = str(temp[3])
        top = str(temp[4])
        height = str(temp[5])
        width = str(temp[6])

        div_open("container")
        div_open(idVal)

        paragraph_open()
        header_open(size)
        place_text("Sample text")
        header_close(size)
        paragraph_close()

        div_close()
        div_close()

        css_open(idVal)
        css_position(position)
        css_height(height)
        css_width(width)
        css_color(color)
        css_left(left)
        css_top(top)
        css_close()
        
    elif (temp[0] == "image"):
        idVal = "image" + str(x)
        position = "absolute"
        left = str(temp[1])
        top = str(temp[2])
        height = str(temp[3])
        width = str(temp[4])

        div_open("container")
        div_open(idVal)

        img_html(width, height)

        div_close()
        div_close()

        css_open(idVal)
        css_position(position)
        css_height(height)
        css_width(width)
        css_left(left)
        css_top(top)
        css_close()
        
    elif (temp[0] == "button"):
        idVal = "button" + str(x)
        idVal2 = "btncolor" + str(x)
        position = "absolute"
        backgroundColor = temp[1]
        color = temp[2]
        left = str(temp[3])
        top = str(temp[4])
        height = str(temp[5])
        length = str(temp[6])

        div_open("container")
        div_open(idVal)

        button_html(idVal2)

        div_close()
        div_close()

        css_open(idVal)
        css_position(position)
        css_height(height)
        css_width(width)
        css_left(left)
        css_top(top)
        css_close()

        css_open(idVal2)
        css_backgroundColor(backgroundColor)
        css_color(color)
        css_close()
    else:
        pass

html_baseJSDependencies()
body_close()
html_close()


output_html.close()
output_css.close()
