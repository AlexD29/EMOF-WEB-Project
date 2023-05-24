import http.server

class HtmlHandler:
    @staticmethod
    def handle(handler , id = None):
        html_template = """<!DOCTYPE html><html>  <head>    <title>Question_1</title>    <link rel="stylesheet" href="style.css" />  </head>  <body>    <div id="ID">{{!@#$}}</div>    <div id="container">      <div id="content">        <div          id="question"          class="flex-container-centered rounded-div drop-shadow-effect"        >          What do you think about The Last of Us Season 1?        </div>        <div id="answer-container" class="">          <div id="wheel-container">            <canvas id="wheel-canvas"></canvas>          </div>          <div>            <div id="howyoufeel-form-container">              <form id="howyoufeel-form">                <textarea                  class="drop-shadow-effect"                  placeholder="Write what you think..."                  id="howyoufeel-textarea"                ></textarea>              </form>            </div>            <div              id="howyoufeel-container"              class="rounded-div drop-shadow-effect"            >              <div                id="howyoufeel-header"                class="flex-container-centered drop-shadow-effect"              >                What you feel              </div>              <div id="howyoufeel-tags-container"></div>            </div>          </div>        </div>        <div id="next-btn" class="rounded-div" onclick="nextPage()">          <a>Next</a>        </div>        <div id="back-explore" class="rounded-div">          <button id="back-explore-button">            Back to Explore          </button>        </div>        <div id="back-btn" class="rounded-div" onclick="lastPage()">          <a> Back </a>        </div>      </div>    </div>  </body>  <script src="script.js"></script></html>"""
        if id is not None:
            html_content = html_template.replace("{{!@#$}}",id)
            handler.send_html_response(html_content)
            return
        
        #id is empty
        handler.path = '/Static/error.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(handler)