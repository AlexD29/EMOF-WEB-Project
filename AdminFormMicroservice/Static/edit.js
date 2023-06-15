document.getElementById("logout-btn").addEventListener("click", function(event) {
	event.preventDefault();
  
	document.cookie = "sessionId=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
  
	window.location.href = "http://127.0.0.1:8050/signupLogin/static/login.html";
});

const container = document.getElementById('questions-container');
let maxInputAllowed = 15;
let questions_elements = []
let questions = [];
const myURL = "http://127.0.0.1:8050/admin-forms-microservice"

//const formID = "sNiLgqTiV7GrxGNh" 
const formID = document.getElementById('FORM_ID').textContent

//load preloaded questions if this is the case
fetch(myURL + '/update/' + formID + '.json', {
		method: 'GET'
	})
	.then(response => {
		if (!response.ok) {
			throw new Error('Network response was not ok');
		}
		return response.json();
	})
	.then(data => {
		// Apelam functia loadData cu datele primite
		console.log(data)
		loadData(data);
	})
	.catch(error => {
		console.error('There has been a problem with your fetch operation:', error);
	});

function loadData(formData) {
	console.log(formData)

	// Incarcam numele formularului
	document.getElementById('form-name-input').value = formData.name;

	// Incarcam descrierea formularului
	document.getElementById('form-description-input').value = formData.description;

	// Incarcam finalizarea formularului
	document.getElementById('form-ending-input').value = formData.ending;

	// Incarcam intrebarile
	for (let i = 0; i < Object.keys(formData.questions).length; i++) {
		const key = (i + 1).toString() 
		if(formData.questions[key] !== undefined)
			loadQuestion(formData.questions[key]);
	}

	// Incarcam tag-urile
	document.getElementById('form-tags-input').value = formData.tags.join(" ");
}

function loadQuestion(text) {

	let input = document.createElement('input');
	input.value = text;

	input.classList.add("flex-container-centered", "rounded-div", "drop-shadow-effect", "question-input")
	container.appendChild(input);
	questions_elements.push(input);
}

function addQuestion() {
	if (questions_elements.length >= maxInputAllowed) {
		alert('You can add maximum ' + maxInputAllowed + ' questions.');
		return;
	}

	let input = document.createElement('input');

	input.placeholder = 'Type something';

	input.classList.add("flex-container-centered", "rounded-div", "drop-shadow-effect", "question-input")
	container.appendChild(input);
	questions_elements.push(input);
}

function deleteQuestion() {
	if (questions_elements.length > 0) {

		let lastChild = container.lastChild;
		container.removeChild(lastChild);
		questions_elements.pop(lastChild)

	} else {
		alert('You dont have any questions to delete');
		return;
	}
}

function validateQuestion(text) {

	if (text == null) return "Weird error , text is null"
	if (text.length < 20) return "No question under 20 characters allowed"
	if (text.length > 1000) return "No question bigger than 1000 characters allowed"

	return true
}

function validateName(name) {
	if (name == null) return "Name is null"
	if (name.length < 6) return "No name under 6 characters allowed"
	if (name.length > 100) return "No name bigger than 100 characters allowed"

	console.log(name);

	return true
}

function validateDescription(text) {
	if (text == null) return "Description is null"
	if (text.length < 20) return "No description under 20 characters allowed"
	if (text.length > 1000) return "No description bigger than 1000 characters allowed"

	console.log(text);

	return true
}

function validateEnding(text) {
	if (text == null) return "Ending is null"
	if (text.length < 10) return "No ending under 10 characters allowed"
	if (text.length > 100) return "No ending bigger than 100 characters allowed"

	console.log(text);

	return true
}

function validateTags(tagsList) {

	// To be done 
	console.log(tagsList)

	return true
}

function validateForm() {

	const name = document.getElementById('form-name-input').value;
	if (validateName(name) !== true) {
		return validateName(name)
	}

	const description = document.getElementById('form-description-input').value;
	if (validateDescription(description) !== true) {
		return validateDescription(description)
	}

	const ending = document.getElementById('form-ending-input').value;
	if (validateEnding(ending) !== true) {
		return validateEnding(ending)
	}

	const unfiltrated_tags = document.getElementById('form-tags-input').value.split(" ");
	const tags = unfiltrated_tags.filter(token => {
		return !(/\s|\.|,/.test(token));
	});

	if (validateTags(tags) !== true) {
		return validateTags(tags)
	}

	if (questions_elements.length == 0) {
		return "You have no questions added"
	}

	for (let i = 0; i < questions_elements.length; i++) {
		const text = questions_elements[i].value;

		const result = validateQuestion(text)

		if (result !== true) {
			return result;
		}
	}

	let questionsDict = {};
	questions_elements.forEach((element, index) => {
		const key = (index + 1).toString(); // Construim cheia ca un șir
		questionsDict[key] = element.value; // Adăugăm cheia și valoarea în dicționar
	});
	/*
	make a json from values above and return it
	*/
	const formData = {
		"name": name,
		"description": description,
		"ending": ending,
		"tags": tags,
		"questions": questionsDict,
		"id" : formID
	};

	return formData;
}

function postFormData(formData) {

	fetch(myURL + '/update', {
			method: 'PUT',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(formData)
		})
		.then(response => {
			if (response.ok) {
				alert('Form edited successfully!');
				window.location.href = 'http://127.0.0.1:8050/admin/';
			} else {
				throw new Error('Failed to edit form.');
			}
		})
		.catch(error => {
			alert('Error: ' + error.message);
		});
}

function create() {
	const result = validateForm();

	if (typeof result === 'string') {
		alert("Error: " + result);
		return;
	}

	console.log(result)
	postFormData(result);
}