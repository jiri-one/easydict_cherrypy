# main imports
import cherrypy
# imports from my other files with classes, methods and confs
from easydict_web_conf import conf
from html_generator import db_search, CreateHtml
from settings import file_path

create_html = CreateHtml()
main_site = open(file_path("main_site.html"), "r", encoding="utf8").read()


class EasyDictWeb(object):
	@cherrypy.expose
	def index(self, **kwargs):
		return main_site

@cherrypy.expose
class SearchEngine(object):
	def POST(self, searched_text):
		if searched_text:
			print(searched_text)
			results = db_search("eng", searched_text, True)
			html = create_html.finish_html(results)
			return html
		else:
			return "zatim nic"

class StringGenerator:
	@cherrypy.expose
	def index(self, **kwargs):
		if 'searched_text' in kwargs:
			results = db_search("eng", kwargs["searched_text"], True)
			html = create_html.finish_html(results)
			print(kwargs)
			return html
		else:
			#return create_html.default_html
			return new_html

	@cherrypy.expose
	def generate(self, my_text):
		print(my_text)


if __name__ == '__main__':
	easydict = EasyDictWeb()
	easydict.searchengine = SearchEngine()
	cherrypy.quickstart(easydict, '/', conf)