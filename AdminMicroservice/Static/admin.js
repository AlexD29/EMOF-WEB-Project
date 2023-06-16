function escapeHtml(unsafe)
{
    return String(unsafe)
         .replace(/&/g, "&amp;")
         .replace(/</g, "&lt;")
         .replace(/>/g, "&gt;")
         .replace(/"/g, "&quot;")
         .replace(/'/g, "&#039;");
 }

async function fetchUserForms(query_string) {
    formList = document.getElementById("form-list-main")
    formList.innerText = '';
    await fetch(`/admin/admin-api/users/${encodeURIComponent('${{{user_id}}}')}/forms` + query_string).then(response => response.json()).then(data => {
        if(data.length > 0) {
          Array.prototype.forEach.call(data, form => displayForm(form));
        }
        else {
          formList.innerHTML = '<h1 class="no-content-text">No Forms Here</h1>';
        }
    }).catch(error => {
      console.log(error)
      formList.innerHTML = '<h1 class="no-content-text">No Forms Here</h1>';
    });
}

function displayForm(form) {
    let formList = document.getElementById("form-list-main");
    let thisForm = document.createElement("section");
    console.log(form.image)
    if(form.status == "draft") {
      thisForm.innerHTML = `
            <div class="form-info-pane">
              <div class="form-heading">
                <h1>
                ${escapeHtml(form.title)}
                </h1>
                <span class="form-item draft-form-bubble">
                  Draft
                </span>
              </div>
              <div class="form-info">
                <p>
                  Description: ${escapeHtml(form.description)}
                </p>
                <p>
                  Questions: ${escapeHtml(form.nr_questions)}
                </p>
              </div>
            </div>
            <div class="form-admin-buttons">
            </div>
      `;
      buttons = thisForm.getElementsByClassName("form-admin-buttons")[0];
      launchButton = document.createElement('a');
      launchButton.classList.add("emphasised-button")
      launchButton.classList.add("button")
      launchButton.innerText = "Launch"; 
      launchButton.addEventListener("click",((form_id) => function (){launchForm(form_id)})(form.id));
      buttons.appendChild(launchButton);
      
      editButton = document.createElement('a');
      editButton.classList.add("active-button")
      editButton.classList.add("button")
      editButton.innerText = "Edit"; 
      editButton.addEventListener("click",((form_id) => function (){editForm(form_id)})(form.id));
      buttons.appendChild(editButton);

      viewButton = document.createElement('a');
      viewButton.classList.add("unselectable-button")
      viewButton.classList.add("button")
      viewButton.innerText = "View Statistics"; 
      buttons.appendChild(viewButton);

      deleteButton = document.createElement('a');
      deleteButton.classList.add("delete-button")
      deleteButton.classList.add("button")
      deleteButton.innerText = "Delete"; 
      deleteButton.addEventListener("click",((form_id) => function (){deleteForm(form_id)})(form.id));
      buttons.appendChild(deleteButton);
    }
    else if(form.status == "active") {
      thisForm.innerHTML = `
            <div class="form-info-pane">
              <div class="form-heading">
                <h1>
                ${escapeHtml(form.title)}
                </h1>
                <span class="form-item active-form-bubble">
                  Active Form
                </span>
              </div>
              <div class="form-info">
                <p>
                  Description: ${escapeHtml(form.description)}
                </p>
                <p>
                  Questions: ${escapeHtml(form.nr_questions)}
                </p>
                <p>
                  <strong>Responses: ${escapeHtml(form.nr_responses)}</strong>
                </p>
              </div>
            </div>
            <div class="form-admin-buttons">
            </div>
      `;
      buttons = thisForm.getElementsByClassName("form-admin-buttons")[0];
      closeButton = document.createElement('a');
      closeButton.classList.add("emphasised-button")
      closeButton.classList.add("button")
      closeButton.innerText = "Close"; 
      closeButton.addEventListener("click",((form_id) => function (){closeForm(form_id)})(form.id));
      buttons.appendChild(closeButton);
      
      editButton = document.createElement('a');
      editButton.classList.add("active-button")
      editButton.classList.add("button")
      editButton.innerText = "Edit"; 
      editButton.addEventListener("click",((form_id) => function (){editForm(form_id)})(form.id));
      buttons.appendChild(editButton);

      viewButton = document.createElement('a');
      viewButton.classList.add("active-button")
      viewButton.classList.add("button")
      viewButton.innerText = "View Statistics"; 
      viewButton.addEventListener("click",((form_id) => function (){statsForm(form_id)})(form.id));
      buttons.appendChild(viewButton);

      deleteButton = document.createElement('a');
      deleteButton.classList.add("delete-button")
      deleteButton.classList.add("button")
      deleteButton.innerText = "Delete"; 
      deleteButton.addEventListener("click",((form_id) => function (){deleteForm(form_id)})(form.id));
      buttons.appendChild(deleteButton);
    }
    else if(form.status == "closed") {
      thisForm.innerHTML = `
            <div class="form-info-pane">
              <div class="form-heading">
                <h1>
                  ${escapeHtml(form.title)}
                </h1>
                <span class="form-item closed-form-bubble">
                  Closed Form
                </span>
              </div>
              <div class="form-info">
                <p>
                  Description: ${escapeHtml(form.description)}
                </p>
                <p>
                  Questions: ${escapeHtml(form.nr_questions)}
                </p>
                <p>
                  <strong>Responses: ${escapeHtml(form.nr_responses)}</strong>
                </p>
              </div>
            </div>
            <div class="form-admin-buttons">
            </div>
      `;
      buttons = thisForm.getElementsByClassName("form-admin-buttons")[0];

      viewButton = document.createElement('a');
      viewButton.classList.add("emphasised-button")
      viewButton.classList.add("button")
      viewButton.innerText = "View Statistics"; 
      viewButton.addEventListener("click",((form_id) => function (){statsForm(form_id)})(form.id));
      buttons.appendChild(viewButton);

      deleteButton = document.createElement('a');
      deleteButton.classList.add("delete-button")
      deleteButton.classList.add("button")
      deleteButton.innerText = "Delete"; 
      deleteButton.addEventListener("click",((form_id) => function (){deleteForm(form_id)})(form.id));
      buttons.appendChild(deleteButton);
    }

    formList.appendChild(thisForm);
}

function selectFormButton(id) {
  let buttons = document.getElementById("categories-button-wrapper");
  for(let i = 0; i < buttons.children.length; ++i){
    if(buttons.children[i].classList.contains("active-button")) {
      buttons.children[i].classList.remove("active-button");
    }
    if(buttons.children[i].classList.contains("inactive-button")) {
      buttons.children[i].classList.remove("inactive-button");
    }
    if(buttons.children[i].id === id) {
      buttons.children[i].classList.add("active-button");
    }
    else {
      buttons.children[i].classList.add("inactive-button");
    }
  }
}

function displayClosedForms() {
  selectFormButton("closed-forms-button");
  fetchUserForms('?filter=closed');
}
function displayDraftForms() {
  selectFormButton("drafts-button");
  fetchUserForms('?filter=draft');
}
function displayAllForms() {
  selectFormButton("all-forms-button");
  fetchUserForms('');
}
function displayActiveForms() {
  selectFormButton("active-forms-button");
  fetchUserForms('?filter=active');
}

function popup_confirm(str, callback) {
  el = document.getElementById("confirm-dialog");
  document.getElementById("title-confirm-dialog").innerText = str;
  btns = document.getElementById("confirm-dialog-buttons");
  oldYes = document.getElementById("yes-confirm-button")
  oldCancel = document.getElementById("cancel-confirm-button")

  yes = oldYes.cloneNode(true);
  cancel = oldCancel.cloneNode(true);
  yes.addEventListener("click", ((clbck) => function () {clbck(); document.getElementById("confirm-dialog").style.visibility = 'hidden'})(callback))
  cancel.addEventListener("click", (() => {document.getElementById("confirm-dialog").style.visibility = 'hidden'}))
  btns.replaceChild(yes,oldYes);
  btns.replaceChild(cancel,oldCancel);
  el.style.visibility = 'visible';
}

function refresh_selection() {
  let buttons = document.getElementById("categories-button-wrapper");
  for(let i = 0; i < buttons.children.length; ++i){
    if(buttons.children[i].classList.contains("active-button")) {
      buttons.children[i].click();
      return;
    }
  }
}

function deleteForm(form_id) {
  popup_confirm("Are you sure you want to delete the Form?", (
    (formId) => function() {
      fetch(`/admin/admin-api/forms/${encodeURIComponent(form_id)}`,{method:'DELETE'}).then(response => {
        if(response.status == 200) {
          //alert("Deleted "+formId)
          refresh_selection();
        }
      }).catch(error => {
        console.log(error)
        alert("Error deleting "+form_id)
      });
    })(form_id));
}
function launchForm(form_id) {
  popup_confirm("Are you sure you want to launch the Form?", (
    (formId) => function() {
      fetch(`/admin/admin-api/forms/${encodeURIComponent(form_id)}`,{method:'PATCH', body:JSON.stringify({status:'active'})}).then(response => {
        if(response.status == 200) {
          //alert("Launched "+formId)
          refresh_selection();
        }
      }).catch(error => {
        console.log(error)
        alert("Error launching "+form_id)
      });
    })(form_id));
}
function closeForm(form_id) {
  popup_confirm("Are you sure you want to close the Form?", (
    (formId) => function() {
      fetch(`/admin/admin-api/forms/${encodeURIComponent(form_id)}`,{
              method:'PATCH', 
              headers: {'Content-Type': 'application/json'}, 
              body:JSON.stringify({status:'closed'})}
      ).then(response => {
          if(response.status == 200) {
            //alert("Launched "+formId)
            refresh_selection();
          }
      }).catch(error => {
        console.log(error)
        alert("Error closing "+form_id)
      });
    })(form_id));
}
function editForm(form_id) {
  window.location.href = `/admin-forms-microservice/update/${encodeURIComponent(form_id)}.html`;
}
function statsForm(form_id) {
  window.location.href = `/forms-microservice/${encodeURIComponent(form_id)}.html`;
}
displayAllForms()

document.getElementById("logout-btn").addEventListener("click", function(event) {
	event.preventDefault();

	document.cookie = "sessionId=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";

	window.location.href = "http://127.0.0.1:8050/signupLogin/static/login.html";
});