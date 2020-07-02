from easydict_web import EasyDictWeb, SearchEngine
from easydict_web_conf import conf_uwsgi
import cherrypy

easydict = EasyDictWeb()
easydict.searchengine = SearchEngine()
wsgiapp = cherrypy.Application(easydict, '/', conf_uwsgi)