from settings import file_path
import cherrypy

conf_desktop = {
    "global": {
    "server.socket_host": "0.0.0.0" # use 127.0.0.1 if you dont need to test it on LAN
    },
    "/": {
    "tools.sessions.on": True,
    "tools.encode.encoding": "utf-8"
    },
    "/static": {
    "tools.staticdir.on": True,
    "tools.staticdir.dir": file_path("static")
    },
    "/searchengine": {
    "request.dispatch": cherrypy.dispatch.MethodDispatcher(),
    "tools.response_headers.on": True,
    "tools.response_headers.headers": [('Content-Type', 'text/html')]    
    }
}

conf_uwsgi = dict(conf_desktop)
conf_uwsgi["global"] = {"engine.autoreload.on": False}