var signUpButton = document.querySelector("#login-submit-btn");

signUpButton.addEventListener("click", function (event) {
  event.preventDefault();

  var emailInput = document.getElementById("email");
  var usernameInput = document.getElementById("username");
  var passwordInput = document.getElementById("password");
  var email = emailInput.value;
  var username = usernameInput.value;
  var password = passwordInput.value;
  var emailErrorMessage = document.getElementById("email-error-message");
  var usernameErrorMessage = document.getElementById("username-error-message");
  var passwordErrorMessage = document.getElementById("password-error-message");

  emailErrorMessage.textContent = "";
  emailInput.classList.remove("kYUBna");
  usernameErrorMessage.textContent = "";
  usernameInput.classList.remove("kYUBna");
  passwordErrorMessage.textContent = "";
  passwordInput.classList.remove("kYUBna");

  var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (email === "") {
    emailInput.classList.add("kYUBna");
    emailErrorMessage.textContent = "Email field should be completed.";
    emailErrorMessage.style.color = "rgb(226, 27, 60)";
  } else if (!emailRegex.test(email)) {
    emailInput.classList.add("kYUBna");
    emailErrorMessage.textContent = "Invalid email.";
    emailErrorMessage.style.color = "rgb(226, 27, 60)";
  }

  if (username === "") {
    usernameInput.classList.add("kYUBna");
    usernameErrorMessage.textContent = "Username field should be completed.";
    usernameErrorMessage.style.color = "rgb(226, 27, 60)";
  } else if (username.length < 4) {
    usernameInput.classList.add("kYUBna");
    usernameErrorMessage.textContent =
      "Username should be at least 4 characters long.";
    usernameErrorMessage.style.color = "rgb(226, 27, 60)";
  }

  if (password === "") {
    passwordInput.classList.add("kYUBna");
    passwordErrorMessage.textContent = "Password field should be completed.";
    passwordErrorMessage.style.color = "rgb(226, 27, 60)";
  } else if (password.length < 6) {
    passwordInput.classList.add("kYUBna");
    passwordErrorMessage.textContent =
      "Password should be at least 6 characters long.";
    passwordErrorMessage.style.color = "rgb(226, 27, 60)";
  }

  if (
    emailRegex.test(email) &&
    username.length >= 4 &&
    password.length >= 6
  ) {

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/signup");
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.onload = function () {
      if (xhr.status === 200) {
        window.location.href = "admin/all_forms.html";
      } else if (xhr.status === 400) {
        var errorMessage = xhr.responseText;
        if (errorMessage.includes("Email") || errorMessage.includes("email")) {
          emailInput.classList.add("kYUBna");
          emailErrorMessage.textContent = errorMessage;
          emailErrorMessage.style.color = "rgb(226, 27, 60)";
        } else if (errorMessage.includes("Username")) {
          usernameInput.classList.add("kYUBna");
          usernameErrorMessage.textContent = errorMessage;
          usernameErrorMessage.style.color = "rgb(226, 27, 60)";
        } else if (errorMessage.includes("password")) {
          passwordInput.classList.add("kYUBna");
          passwordErrorMessage.textContent = errorMessage;
          passwordErrorMessage.style.color = "rgb(226, 27, 60)";
        } else {
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
      "email=" +
      encodeURIComponent(email) +
      "&username=" +
      encodeURIComponent(username) +
      "&password=" +
      encodeURIComponent(password);
    xhr.send(formData);
  }
});
