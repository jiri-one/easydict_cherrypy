# main imports
import cherrypy
# imports from my other files with classes, methods and confs
from easydict_web_conf import conf
from html_generator import db_search, CreateHtml
from settings import file_path

create_html = CreateHtml()
main_site = open(file_path("index.html"), "r", encoding="utf8").read()


class EasyDictWeb(object):
	@cherrypy.expose
	def index(self, **kwargs):
		return main_site

@cherrypy.expose
class SearchEngine(object):
	def POST(self, language, searched_text, fulltext):
		if language and searched_text and fulltext:
			print(language, searched_text, fulltext)
			try:				
				language, searched_text, fulltext = self.validate_searchengine_input(language, searched_text, fulltext)
				results = db_search(language, searched_text, fulltext)
				html = create_html.finish_html(results)
				return html
			except:
				return "Nothing was found or bad input."
		else:
			return "Nothing was found or bad input."
	
	def validate_searchengine_input(self, language, searched_text, fulltext):
		"""This function is here for valitadion input from ajax and normalize the input for search in db."""
		#language check
		if language == "Czech":
			language = "cze"
		else:
			language = "eng"
		#fulltext check
		if fulltext == "true":
			fulltext = True
		else:
			fulltext = False
		#check of searched_text
		if len(searched_text.split()) == 1: #check if the input is just one word
			print(language, searched_text, fulltext)
			return language, searched_text, fulltext	

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