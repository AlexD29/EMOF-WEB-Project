import http.server

class HtmlEditHandler:
    @staticmethod
    def handle(handler , id = None):
        html_template = """
        <!DOCTYPE html>
<html>

<head>
  <title>Edit Formular</title>
  <link href="emof.css" rel="stylesheet" />
  <link href="style.css" rel="stylesheet" />
</head>

<body>
	<div id="FORM_ID" style="display:none;">{{!@#$}}</div>
  <div id="container">
    <div class="landing-section-header">
      <header id="landing-header-id" class="landing-header" role="banner" itemscope="">
        <div class="landing-header-elements">
          <a href="/admin/all_forms.html" class="logo-link">
            <img alt="" src="logo.png" class="logo_landing" />
          </a>
          <nav id="landing-header_menu" class="landing-header_menu landing-header_menu--microsite"
            aria-label="Navigation" data-translated="1" itemscope="">
            <ul id="menu-landing-header_menu-left" class="landing-header_menu-left">
              <li id="menu-item-92366" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-92366">
                <a><span class="your-formulars">Create Formular</span></a>
              </li>
              <li id="menu-item-92365"
                class="back-button menu-item menu-item-type-custom menu-item-object-custom menu-item-92365">
                <a href="../../admin/all_forms.html" data-tracking-id="sign-up-top-bar" itemprop="url">Back</a>
              </li>
            </ul>
            <ul class="landing-header_menu-right first-in-focus">
              <li class="icon-before-nav">
                <a><span class="menu-item-text">AlexD29</span></a>
              </li>
              <li class="landing-button logout_button">
                <a href="/login.html" itemprop="url">Log out</a>
              </li>
            </ul>
          </nav>
        </div>
      </header>
    </div>
    <input id="form-name-input" placeholder="Enter the form name" class="form-text-input flex-container-centered rounded-div drop-shadow-effect question-input">
    <input id="form-description-input" placeholder="Enter the form description" class="form-text-input flex-container-centered rounded-div drop-shadow-effect question-input">
    <input id="form-ending-input" placeholder="Enter the form ending" class="form-text-input flex-container-centered rounded-div drop-shadow-effect question-input">
    <input id="form-tags-input" placeholder="Enter one word tags separated by space (Optional)" class="form-text-input flex-container-centered rounded-div drop-shadow-effect question-input">
    <div id="questions-container">
      <div class="flex-container-centered">
        
        <button id="add-btn" class="rounded-div drop-shadow-effect" onclick="addQuestion()">
          + Add question
        </button>
        <button id="del-btn" class="rounded-div drop-shadow-effect" onclick="deleteQuestion()">
          - Delete question
        </button>
      </div>

      <div id="next-btn" class="rounded-div" onclick="create()">
        <a> Done </a>
      </div>
    </div>
  </div>
</body>
<script src="edit.js"></script>

</html>
        """
        if id is not None:
            html_content = html_template.replace("{{!@#$}}",id)
            handler.send_html_response(html_content)
            return
        
        #id is empty
        handler.path = '/Static/error.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(handler)