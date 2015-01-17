from wolfram_test import *

OUTPUT_CSS = "out.css"
OUTPUT_HTML = "out.html"

css_file = open(OUTPUT_CSS, "w")
html_file = open(OUTPUT_HTML, "w")

# Set-up html file
html_file.write("<html>\n")
html_file.write("<head>\n")
html_file.write("</head>\n")
html_file.write("<body>\n")
html_file.write("<div class=\"wolfram_element\">\n")
html_file.write("<p>\n")



appid = "PG9HJR-22LGXXP97Y"
query = "pi"
value = "Decimal approximation"
w = wolfram(appid)
print w.search(query, value)


# Finish-up html file
html_file.write("</p>\n")
html_file.write("</div>\n")
html_file.write("</body>\n")
html_file.write("

css_file.close()
html_file.close()
