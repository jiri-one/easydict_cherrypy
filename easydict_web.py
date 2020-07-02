# main imports
import cherrypy
# imports from my other files with classes, methods and confs
from easydict_web_conf import conf_desktop
from html_generator import db_search, CreateHtml
from settings import file_path

create_html = CreateHtml()

class EasyDictWeb(object):
	@cherrypy.expose("test")
	def index(self, **kwargs):
		try: # this condition and try statement is necessary for set language correctly; it check: if the ?lang=XXX is changed and if XXX is in known languages, then change default language. Because kwargs["lang"] maybe do not exists, then I need to "try:" it firstly
			if cherrypy.session["lang"] != kwargs["lang"] and kwargs["lang"] in ["cze", "eng"]: # in the future, this small list will be replaced from with DB entries
				cherrypy.session["lang"] = kwargs["lang"]
		except:
			pass

		if 'lang' not in cherrypy.session:
			cherrypy.session["lang"] = "eng"

		main_site = open(file_path(f"index_{cherrypy.session['lang']}.html"), "r", encoding="utf8").read()
		print(cherrypy.url(relative=True))
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
				return "Nothing was found or bad input. Try to search just one word."
		else:
			return "Nothing was found or bad input."
	
	def validate_searchengine_input(self, language, searched_text, fulltext):
		"""This method is here for valitadion input from ajax and normalize the input for search in db."""
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

if __name__ == "__main__":
	easydict = EasyDictWeb()
	easydict.searchengine = SearchEngine()
	cherrypy.quickstart(easydict, '/', conf_desktop)

