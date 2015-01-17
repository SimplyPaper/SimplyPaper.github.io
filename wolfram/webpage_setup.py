from wolfram_test import *

OUTPUT_HTML = "out.html"

css_file = open(OUTPUT_HTML, "w")
appid = "PG9HJR-22LGXXP97Y"
def basicStructureTop():
    css_file.write("<!DOCTYPE html>\n<html>\n")
def basicStructureBottom():
    css_file.write("</html>")
def head(value):
    css_file.write("<head>\n")
    css_file.write(value)
    css_file.write("</head>\n")
def bodyTop():
    css_file.write("<body>\n")
def bodyBottom():
    css_file.write("</body>\n")
def setUpWolfram(appid,query,value):
    css_file.write("<div class=\"wolfram_element\">\n")
    css_file.write("<p>\n")
    w = wolfram(appid)
    result = w.search(query, value)
    css_file.write(value + " " + result + "\n")
    css_file.write("</p>\n")
    css_file.write("</div>\n")
def setUpButton(appid):
    css_file.write("<button type = \"button\" id = \"butt" + str(appid) + "\">\n Button" + str(appid) +"\n</button>")
def styleTop():
    css_file.write("<style>")
def styleBot():
    css_file.write("</style>\n")
def setItemSpot(appid,posx,posy,height,width):
    css_file.write("#" + appid + " {\n")
    css_file.write("height: "+ str(height) + "px;\n")
    css_file.write("width: " + str(width) + "px;\n")
    css_file.write("position: absolute;\n")
    css_file.write("left: " + str(posx) + "px;\n")
    css_file.write("top: " + str(posy) + "px;\n")
    
basicStructureTop()
styleTop()
setItemSpot("butt1",150,100,60,100)
styleBot()
head("Header")
bodyTop()
setUpWolfram(appid,"pi","Property")
setUpButton(1)
bodyBottom()
basicStructureBottom()
css_file.close()
