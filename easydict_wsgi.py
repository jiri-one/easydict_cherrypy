from easydict_web import EasyDictWeb, SearchEngine
from easydict_web_conf import conf_uwsgi
import cherrypy

easydict = EasyDictWeb()
easydict.searchengine = SearchEngine()
cherrypy.config.update({"tools.sessions.on": True, 'tools.encode.encoding': 'utf-8'})
wsgiapp = cherrypy.Application(easydict, '/', conf_uwsgi)