var resetButton = document.getElementById("reset-submit-btn");
resetButton.disabled = true;

function checkFormCompletion() {
  var email = document.getElementById("email").value;

  resetButton.disabled = !email;
}

function resetFields(){
  document.getElementById("email").value="";
}

resetFields();
document.getElementById("email").addEventListener("input",checkFormCompletion);


resetButton.addEventListener("click", function (event) {
  event.preventDefault();

  var emailInput = document.getElementById("email");
  var email = emailInput.value;
  var resetErrorMessage = document.getElementById("reset-error-message");

  resetErrorMessage.textContent = "";
  emailInput.classList.remove("kYUBna");

  var xhr = new XMLHttpRequest();
  xhr.open("POST", "/reset");
  xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  xhr.onload = function () {
    if (xhr.status === 200) {
      window.location.href = "admin/all_forms.html";
    } else if (xhr.status === 400) {
      var errorMessage = xhr.responseText;
      if (errorMessage.includes("email")) {
        emailInput.classList.add("kYUBna");
        resetErrorMessage.textContent = errorMessage;
        resetErrorMessage.style.color = "rgb(226, 27, 60)";
      }
      else {
        console.log("Error:", errorMessage);
      }
    } else {
      console.log("Error:", xhr.responseText);
    }
  };
  xhr.onerror = function () {
    console.log("Request failed.");
  };
  var formData =
    "&email=" +
    encodeURIComponent(email);
  xhr.send(formData);
});
