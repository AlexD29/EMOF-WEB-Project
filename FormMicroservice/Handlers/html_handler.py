import http.server

class HtmlHandler:
    @staticmethod
    def handle(handler , id = None):
        html_template = """<!DOCTYPE html>
<html>

<head>
	<title>Question_1</title>
	<style>
		body {
			background-repeat: no-repeat;
			background-attachment: fixed;
			background-color: rgb(161, 252, 57);
			/* For browsers that do not support gradients */
			background-image: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);
			background-size: cover;
			margin: 0;
			padding: 0;
			box-sizing: border-box;
			font-family: Montserrat, "Noto Sans Arabic", "Helvetica Neue", Helvetica, Arial, sans-serif;
		}

		#ID {
			display: none;
		}

		#header {
			height: 2rem;
			background-color: #1bc908;
			justify-content: center;
		}

		#form-title {
			height: 5rem;
			background-color: rgb(14, 212, 230);
			justify-content: center;
			font-size: 2rem;
			font-weight: bold;
		}

		#header-incomplete {
			height: 2rem;
			background-color: #f05907;
			justify-content: center;
		}

		#content {
			padding: 1rem 13% 1rem 13%;
		}

		#next-btn,
		#back-btn {

			width: 5rem;
			text-align: center;
			background-color: green;
			font-size: 30px;
			transition-duration: 0.4s;
		}

		#next-btn:hover {
			background-color: #7836f4;
			color: white;
		}

		#back-btn:hover {
			background-color: #f45c36;
			color: white;
		}

		#back-btn {
			left: 8%;
		}

		#next-btn {
			right: 8%
		}

		#next-btn>a,
		#back-btn>a {
			color: white;
		}

		#next-btn>a,
		#back-btn>a:link {
			text-decoration: none;
		}

		#next-btn,
		#back-btn {
			position: fixed;
			color: white;
			bottom: 2rem;
			width: 3rem;
			padding: 0.75rem;
			text-align: center;
			background-color: green;
			font-size: large;
			transition-duration: 0.4s;
		}

		#wheel-canvas {
			width: 100%;
			height: 100%;
		}

		#wheel-container {
			width: 550px;
			height: 550px;
			margin: auto;
		}


		#howyoufeel-container {
			width: 400px;
			height: 280px;
		}

		#howyoufeel-header {
			background-color: #1165ba;
			border-radius: 25px 25px 0 0;
			height: 2.5rem;
			justify-content: center;
			color: white;
			font-size: large;

		}

		#howyoufeel-textarea {
			width: 100%;
			height: 10rem;
			margin: 2rem 0 2rem 0;
			resize: none;
			outline: none;
			border-radius: 1rem;
			border: 0px;
			font-size: large;
		}

		#howyoufeel-textarea::placeholder {
			font-weight: bold;
			font-size: large;
			align-content: center;
			text-align: center;
		}
        
        #user-info-container{
			margin: 5rem 0rem;
        }

		#question {
			overflow: auto;
			display: block;
			margin: 0rem 0rem 0rem 0rem;
			height: 80px;
			
			font-size: 30px;
			justify-content: center;
			padding: 1rem 1rem 1rem 1rem;
		}

		#answer-container {
			padding: 2rem 0 2rem 0;
			display: flex;
			justify-content: space-between;
			align-items: center;
		}

		.flex-container-centered {
			display: flex;
			justify-content: center;
			align-items: center;
		}

		.drop-shadow-effect {
			box-shadow: 0 2px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
		}

		.rounded-div {
			border-radius: 25px;
			background-color: #FFFFFF;
		}

		#howyoufeel-tags-container {
			display: flex;
			flex-wrap: wrap;
		}

		#howyoufeel-tags-container>div {
			margin: 10px;
			border: 0px;
			background: #fff0f0;
			border-radius: 5px;
			padding: 0.5rem;
		}

		.tag:hover {
			background-color: rgb(0, 162, 255);
		}

		@media only screen and (max-width: 1450px) {

			#answer-container {
				display: block;
			}

			#howyoufeel-container {
				margin: 0 auto;
			}

			#howyoufeel-form-container {
				padding: 0 12rem 0 12rem;
			}

			#question {
				font-size: 25px;
			}

		}

		@media only screen and (max-width: 768px) {


			#question {
				font-size: 20px;
			}

		}


		#complete_text {
			font-size: 25px;
			font-weight: bold;
		}


		#instructions {
			font-size: 20px;
		}

		#back-explore {
			background-color: transparent;
		}

		#back-explore-button {
			display: block;
			margin: 20px 10px 10px 40%;
			background-color: #002554;
			/* a shade of green */
			border: none;
			border-radius: 20px;
			/* adjust the value to increase or decrease the roundness */
			color: white;
			text-align: center;
			font-size: 20px;
			padding: 20px 40px;
			text-decoration: none;
			transition: background-color 0.3s ease;
		}

		#back-explore-button:hover {
			background-color: #0c4ec8;
			/* a darker shade of green */
		}
	</style>
</head>

<body>
	<div id="ID">{{!@#$}}</div>
	<div id="container">
		<div id="content">
			<div id="question" class="flex-container-centered rounded-div drop-shadow-effect">  </div>
        	<div id="user-info-container" class="flex-container-centered rounded-div drop-shadow-effect"></div>
			<div id="answer-container" class="">
				<div id="wheel-container"> <canvas id="wheel-canvas"></canvas> </div>
				<div>
					<div id="howyoufeel-form-container">
						<form id="howyoufeel-form"> <textarea class="drop-shadow-effect"
								placeholder="Write what you think..." id="howyoufeel-textarea"></textarea> </form>
					</div>
					<div id="howyoufeel-container" class="rounded-div drop-shadow-effect">
						<div id="howyoufeel-header" class="flex-container-centered drop-shadow-effect"> What you feel
						</div>
						<div id="howyoufeel-tags-container"></div>
					</div>
				</div>
			</div>
			<div id="next-btn" class="rounded-div" onclick="nextPage()"> <a>Next</a> </div>
			<div id="back-explore" class="rounded-div"> <button id="back-explore-button"> Back to Explore </button>
			</div>
			<div id="back-btn" class="rounded-div" onclick="lastPage()"> <a> Back </a> </div>
		</div>
	</div>
<script>
const id = document.getElementById('ID').textContent;
const API_URL = "http://127.0.0.1:8050/forms-microservice/"

let formInfo = {}
let pageCounter = 0;
let numberOfPages = 2;
let userInfoResponses = [];

const startTime = new Date();

async function fetchData() {
	try {
		setDefault()
		const response = await fetch(API_URL + id + ".json")
		const data = await response.json()
		formInfo = data
        const userInfoQuestions = formInfo.questions.getUserInfoQuestions
        delete formInfo.questions.getUserInfoQuestions
        formInfo.userInfoQuestions = userInfoQuestions
		numberOfPages = Object.keys(formInfo.questions).length + 2;

		console.log(formInfo)
		updatePage()
	} catch (err) {
		console.log('error: ' + err)
	}

}

fetchData()

let selectedEmotions = {};

function updateTagsContainer() {
	let tagsContainer = document.getElementById('howyoufeel-tags-container');

	while (tagsContainer.firstChild) {
		tagsContainer.removeChild(tagsContainer.firstChild);
	}

	(selectedEmotions[pageCounter] || []).forEach(emotion => {
		let color = emotions_list.find(emotions => emotions.find(e => e.name == emotion)).find(e => e.name ==
			emotion).color;
		let tag = document.createElement("div")
		let text = document.createTextNode(emotion);

		tag.appendChild(text);
		tag.style.backgroundColor = color;
		tag.id = emotion + "-" + pageCounter;

		tagsContainer.appendChild(tag);
	});
}

function setDefault() {
	try {
		document.getElementById("next-btn").style.visibility = "hidden"
        document.getElementById("user-info-container").style.visibility = "hidden"
        document.getElementById("user-info-container").innerHTML = ""
		document.getElementById("back-explore-button").style.visibility = "hidden"
		document.getElementById("back-btn").style.visibility = "hidden"
		document.getElementById("howyoufeel-header").style.visibility = "hidden"
		document.getElementById("answer-container").style.visibility = "hidden"
		document.getElementById("next-btn").innerHTML = "Next"
	} catch (e) {
		console.log(e)
	}
}

function checkFormInput() {

	for (let i = 1; i < numberOfPages - 1; i++) {
		if (!selectedEmotions[i] || selectedEmotions[i].length === 0) {

			return i;
		}
	}

	return -1;
}

function sendData() {

	let incompletePageIndex = checkFormInput();
	if (incompletePageIndex !== -1) {
		alert("Trebuie sa selectezi cel putin un sentiment pentru fiecare pagina.");

		console.log("Nu trimitem data :((")
		console.log(selectedEmotions)

		pageCounter = incompletePageIndex;
		updatePage();
		return;
	}

	console.log("Trimitem data <3")
    
    const endTime = new Date();
  	let timeDiff = endTime - startTime; //in ms
  	// strip the ms
  	timeDiff /= 1000;

  	// get seconds 
  	const seconds = Math.round(timeDiff);
    
    let dataToSend = selectedEmotions;
    dataToSend.duration = seconds + " seconds"; 
    dataToSend.userInfo = userInfoResponses;
    
	console.log(dataToSend)

	fetch(API_URL + 'submit/' + id, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(dataToSend)
		})
		.then(response => response.json())
		.then(data => {
			console.log('Success:', data);

			pageCounter++;
			updatePage();
		})
		.catch((error) => {
			console.error('Error:', error);
		});
}

function updateDescriptionPage() {
	document.getElementById("question").innerHTML = formInfo.description
	document.getElementById("next-btn").style.visibility = "visible"
    document.getElementById("user-info-container").style.visibility = "visible"
    
    // Parcurgem toate întrebările și creăm un input pentru fiecare
	formInfo.userInfoQuestions.forEach(question => {
		console.log(question)
		createUserInputQuestion(question);
	});	

    
}

function updateFinalPage() {
	document.getElementById("question").innerHTML = formInfo.ending
	document.getElementById("back-explore-button").style.visibility = "visible"
}

function updateQuestionPage() {
	if (pageCounter == numberOfPages - 2) {
		document.getElementById("next-btn").innerHTML = "Finish"
	}
	document.getElementById("question").innerHTML = formInfo.questions[pageCounter]
	document.getElementById("next-btn").style.visibility = "visible"
    if(pageCounter > 1){
		document.getElementById("back-btn").style.visibility = "visible"
	}
	document.getElementById("answer-container").style.visibility = "visible"

}

function updatePage() {
	setDefault()
	if (pageCounter == 0) {
		updateDescriptionPage()
	} else if (pageCounter == numberOfPages - 1) {
		updateFinalPage()
	} else {
		updateQuestionPage()
	}
	updateTagsContainer();
}

function nextPage() {
	if(pageCounter == 0)
		userInfoResponses = getUserInfoResponses();
        if(!validateResponses()) {
			alert("Fiecare raspuns trebuie sa contina maximum un singur cuvant.");
			return;
    }

	if (pageCounter == numberOfPages - 2)
		sendData();
	else {
		pageCounter++;
		updatePage();
	}
}

function lastPage() {
	if (pageCounter <= 1)
		return;

	pageCounter--;
	updatePage();
}

function createUserInputQuestion(question) {
    // Obținem containerul pentru a adăuga noi input-uri
    const container = document.getElementById('user-info-container');

    // Aplicăm stilurile pentru container direct în JavaScript
    container.style.display = 'flex';
    container.style.flexDirection = 'column';
    container.style.justifyContent = 'center';
    container.style.alignItems = 'center';
    container.style.width = '100%';

    // Crearea div-ului
    const divElement = document.createElement("div");
    divElement.style.margin = "10px 0"; // Stilizare în JavaScript
    divElement.style.display = 'flex'; // Adăugăm flex pentru a centra conținutul
    divElement.style.flexDirection = 'column'; // Folosim flex-direction pentru a pune conținutul pe rânduri
    divElement.style.alignItems = 'center'; // Centrăm conținutul pe linie

    // Crearea și stilizarea label-ului
    const labelElement = document.createElement("label");
    labelElement.innerHTML = question;
    labelElement.htmlFor = question.replace(/\s/g, "-"); // Adăugăm id-ul pentru label
    labelElement.style.display = 'block'; // Face ca eticheta să apară pe linia sa

    // Crearea input-ului
    const inputElement = document.createElement("input");
    inputElement.type = "text"; // tipul input-ului
    inputElement.id = question.replace(/\s/g, "-"); // id-ul input-ului este același ca label-ul pentru accesibilitate
    inputElement.style.marginTop = '10px'; // Adăugăm margin-top pentru a separa input-ul de label

    // Adăugăm label și input în div
    divElement.appendChild(labelElement);
    divElement.appendChild(inputElement);

    // Adăugăm div în container
    container.appendChild(divElement);
}

function getUserInfoResponses() {
    // Obținem toate inputurile din containerul de întrebări
    const inputs = document.getElementById('user-info-container').getElementsByTagName('input');

    // Vom stoca perechile întrebare - răspuns aici
    let responses = [];

    // Parcurgem toate inputurile și extragem textul întrebării și răspunsul
    for (let i = 0; i < inputs.length; i++) {
        let input = inputs[i];
        // id-ul inputului este textul întrebării (fără spații)
        let questionText = input.id.replace(/-/g, " ");
        // valoarea inputului este răspunsul
        let answer = input.value;
        // Adăugăm perechea la listă
        responses.push({question: questionText, answer: answer});
    }

    return responses;
}

function validateResponses() {
    let isValid = true;
		
	userInfoResponses.forEach(responseItem => {
		// Împărțim răspunsul în cuvinte
		let words = responseItem.answer.split(' ');
		// Dacă numărul de cuvinte este mai mare de 1, setăm isValid ca false
		if(words.length > 1) {
			isValid = false;
		}
	});	
	
    return isValid;
}


const emotions_list = [
	[{
		color: "#ffffff",
		name: ""
	}],
	[{
			color: '#2983c5',
			name: 'Grief'
		},
		{
			color: '#8973b3',
			name: 'Loathing'
		},
		{
			color: '#f05b61',
			name: 'Rage'
		},
		{
			color: '#f6923d',
			name: 'Vigilance'
		},
		{
			color: '#ffca05',
			name: 'Ecstasy'
		},
		{
			color: '#8ac650',
			name: 'Admiration'
		},
		{
			color: '#00a551',
			name: 'Terror'
		},
		{
			color: '#0099cd',
			name: 'Amazement'
		}
	],
	[{
			color: '#74a8da',
			name: 'Sadness'
		},
		{
			color: '#a390c4',
			name: 'Disgust'
		},
		{
			color: '#f2736d',
			name: 'Anger'
		},
		{
			color: '#f9ad66',
			name: 'Anticipation'
		},
		{
			color: '#ffdc7b',
			name: 'Joy'
		},
		{
			color: '#abd26a',
			name: 'Trust'
		},
		{
			color: '#30b575',
			name: 'Fear'
		},
		{
			color: '#36aed7',
			name: 'Surprise'
		}
	],
	[{
			color: '#a0c0e5',
			name: 'Pensiveness'
		},
		{
			color: '#b9aad3',
			name: 'Boredom'
		},
		{
			color: '#f48d80',
			name: 'Annoyance'
		},
		{
			color: '#fcc487',
			name: 'Interest'
		},
		{
			color: '#ffed9f',
			name: 'Serenity'
		},
		{
			color: '#cadf8b',
			name: 'Acceptance'
		},
		{
			color: '#7ac698',
			name: 'Apprehension'
		},
		{
			color: '#89c7e4',
			name: 'Distraction'
		}
	],
	[{
			color: '#C9C8E4',
			name: 'Remorse'
		},
		{
			color: '#EABBBF',
			name: 'Contempt'
		},
		{
			color: '#FBC6B2',
			name: 'Aggresiveness'
		},
		{
			color: '#FFF1CA',
			name: 'Optimism'
		},
		{
			color: '#F2F5C9',
			name: 'Love'
		},
		{
			color: '#B2DBB1',
			name: 'Submission'
		},
		{
			color: '#A9D5C3',
			name: 'Awe'
		},
		{
			color: '#C3DAEF',
			name: 'Disapproval'
		}
	]
];


const canvas = document.getElementById('wheel-canvas');
canvas.width = document.getElementById('wheel-container').offsetWidth;
canvas.height = document.getElementById('wheel-container').offsetHeight;
const context = canvas.getContext('2d');

for (let k = 4; k >= 0; k--) {

	let angle = (2 * Math.PI) / emotions_list[k].length;
	let ratio = (k + 1) / 5;
	let width = ratio * canvas.width;
	let height = ratio * canvas.height;
	let radius = Math.min(width, height) / 2;

	for (let i = 0; i < emotions_list[k].length; i++) {

		let startAngle = -Math.PI / 2 + i * angle;
		let endAngle = -Math.PI / 2 + (i + 1) * angle;

		if (k == 4) {
			startAngle = -Math.PI / 2 + i * angle + angle / 2;
			endAngle = -Math.PI / 2 + (i + 1) * angle + angle / 2;
		}

		context.beginPath();
		context.moveTo(canvas.width / 2, canvas.height / 2);
		context.arc(canvas.width / 2, canvas.height / 2, radius, startAngle, endAngle);
		context.closePath();

		context.fillStyle = emotions_list[k][i].color;
		context.fill();

		let x = (canvas.width / 2 - (radius - 30) * Math.cos(Math.PI / 2 + i * angle + angle / 2));
		let y = (canvas.height / 2 - (radius - 30) * Math.sin(Math.PI / 2 + i * angle + angle / 2));

		if (k == 4) {
			x = (canvas.width / 2 - (radius - 30) * Math.cos(Math.PI / 2 + i * angle + angle));
			y = (canvas.height / 2 - (radius - 30) * Math.sin(Math.PI / 2 + i * angle + angle));
		}

		context.save();
		context.textAlign = 'center';

		context.strokeStyle = 'black';
		context.lineWidth = 1;

		context.font = '11px Arial';
		context.fillStyle = 'black';
		context.fillText(emotions_list[k][i].name, x, y);
		context.restore();

		const segment = {
			x: canvas.width / 2,
			y: canvas.height / 2,
			radius: radius,
			startAngle: startAngle,
			endAngle: endAngle,
		};

		canvas.addEventListener("click", function (event) {
			const rect = canvas.getBoundingClientRect();

			const x = event.clientX - rect.left;
			const y = event.clientY - rect.top;

			context.beginPath();

			context.arc(
				segment.x,
				segment.y,
				segment.radius,
				segment.startAngle,
				segment.endAngle
			);
			context.lineTo(segment.x, segment.y);
			context.closePath();

			if (context.isPointInPath(x, y)) {

				const a = x - canvas.width / 2;
				const b = y - canvas.height / 2;
				const distance = Math.sqrt(a * a + b * b);

				const h = distance / (canvas.width / 2) * 5

				circle_number = parseInt(h, 10)

				if (circle_number == k && k != 0) {

					emotion = emotions_list[circle_number][i].name;
					color = emotions_list[circle_number][i].color;

					let tagsContainer = document.getElementById('howyoufeel-tags-container');

					if (!selectedEmotions[pageCounter]) {
						selectedEmotions[pageCounter] = [];
					}

					if (!selectedEmotions[pageCounter].includes(emotion)) {
						selectedEmotions[pageCounter].push(emotion);
					} else {
						const index = selectedEmotions[pageCounter].indexOf(emotion);
						if (index > -1) {
							selectedEmotions[pageCounter].splice(index, 1);
						}
					}

					updateTagsContainer();

				}
			}
		});
	}

}
	</script>
</body>

</html>"""
        if id is not None:
            html_content = html_template.replace("{{!@#$}}",id)
            handler.send_html_response(html_content)
            return
        
        #id is empty
        handler.path = '/Static/error.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(handler)