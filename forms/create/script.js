const container = document.getElementById('questions-container');
var maxInputAllowed = 15;
var inputCount = 0;
let questions_elements = [];

function addQuestion() {
	if (inputCount >= maxInputAllowed) {
		alert('You can add maximum ' + maxInputAllowed + ' questions.');
		return;
	}
	inputCount++;
	let input = document.createElement('input');
	input.placeholder = 'Type something';
	input.classList.add("flex-container-centered","rounded-div","drop-shadow-effect","question-input")
	container.appendChild(input);
	questions_elements.push(input);
}

function deleteQuestion() {
	if(inputCount > 0) {
		inputCount--;
		
		let lastChild = container.lastChild; 
		container.removeChild(lastChild);
		questions_elements.pop(lastChild)

	}
	else{
		alert('You dont have any questions to delete');
		return;
	}
}

function validateQuestion(text){
	
	if(text.length < 20) return "No question under 20 characters allowed"
	if(text.length > 1000) return "No question bigger than 1000 characters allowed"

	return true
}

function validateForm(){
	const len = questions_elements.length;
	if(len < 1){
		return "You have no questions added"
	}

	for (let i = 0; i < questions_elements.length; i++) { 
		const text = questions_elements[i].value; 
		
		const result = validateQuestion(text)

		if(result !== true){
			return result;
		}
	}

	return true;
}


function create(){
	
	const result = validateForm();
	
	if(result !== true){
		alert("Error : " + result);
		return;
	}

	let questions = questions_elements.map((question,index) => (index + 1) + "."+ question.value)

	alert("Form created !! These are your questions : " + questions);
	window.location.href = "../../admin.html";


}