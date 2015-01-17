from webpage_setup import *

OUTPUT_HTML = "out.html"

css_file = open(OUTPUT_HTML, "w")
appid = "PG9HJR-22LGXXP97Y"
basicStructureTop()
bodyTop()

setUpButton(1)
bodyBottom()
basicStructureBottom()
css_file.close()
