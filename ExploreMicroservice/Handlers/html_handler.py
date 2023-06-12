import http.server

class HtmlHandler:
	@staticmethod
	def handle(handler):
		if True: #logged in
			handler.path = '/Static/explore_forms.html'
		else:
			handler.path = '/Static/explore_forms_nologin.html'
		return http.server.SimpleHTTPRequestHandler.do_GET(handler)