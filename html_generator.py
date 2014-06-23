import os, webbrowser

def create_layout():
	title = raw_input("Type a Page Title:")
	h2 = raw_input("Type a Paragraph Title:")
	h1 = raw_input("Type a Company Name:")
	h3 = raw_input("Type Some Content:")

	with open ('css.css', 'w') as css:
		css.write("body {margin: 0;padding: 0;font-family: \"Helvetica Neue\", Helvetica, Arial, sans-serif;color: #444;}")
		css.write("header {font-size: large; color: #E0E0E0; background-color: #2B2B2B;height: 35px;width: 100%;opacity: .9;margin-bottom: 10px; text-align: left}")
		css.write("div.jumbo {padding: 10px 0 30px 0;background-color: #eeeeee;-webkit-border-radius: 6px;-moz-border-radius: 6px;border-radius: 6px;}")
		css.write("h2 {font-size: 5em;large;margin-top: 40px;text-align: center;letter-spacing: -2px; text-align: center})")
		css.write(".container {width: 940px;margin: 0 auto;}")
		css.write("h3 {font-size: 1.7em;font-weight: 100;margin-top: 30px;text-align: center;letter-spacing: -1px;color: #999;}")
		css.write("header h1.logo {margin: 0;font-size: 1.7em;color: #fff;text-transform: uppercase;float: left;}")
		css.close()

	with open ('index.html', 'w') as html:
		html.write("<!DOCTYPE html><html><head></head><link rel=\"stylesheet\" type =\"text/css\" href=\"css.css\"><title>%s</title><body><header><div class=\"container\"><h1 class=\"logo\">%s</h1></div></header></h1><div class=\"container\"><div class=\"jumbo\"><h2>%s</h2><h3>%s</h3></div></div><p></p></body></html>" % (title, h1,h2,h3))
		html.close()
	
create_layout()
webbrowser.open('file://%s' % os.path.abspath('index.html'))


