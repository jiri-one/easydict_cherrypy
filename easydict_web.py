import cherrypy
from html_generator import db_search, CreateHtml

create_html = CreateHtml()
main_site = open("main_site.html", "r").read()


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
	cherrypy.quickstart(easydict, '/', "easydict_web.conf")