import http.server

class HtmlHandler:
	@staticmethod
	def handle(handler):
		handler.path = '/Static/admin.html'
		return http.server.SimpleHTTPRequestHandler.do_GET(handler)