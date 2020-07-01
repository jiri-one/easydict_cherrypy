from settings import file_path
import cherrypy

conf = {
    "global": {
    "server.socket_host": "0.0.0.0",
    "tools.sessions.on": True
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