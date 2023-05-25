const id = document.getElementById('ID').textContent;
//const API_URL = "http://localhost:8087/forms-microservice/"
const API_URL = "http://localhost:8070/forms-microservice/"

let formInfo = {}
let pageCounter = 0;
let numberOfPages = 2;

async function fetchData() {
  try {
	setDefault()
    const response = await fetch(API_URL + "data/" + id + ".json")
    const data = await response.json()
    formInfo = data[0]
	numberOfPages = formInfo.questions.length + 2;
    
    console.log(formInfo)
	updatePage()
  } catch (err) {
    console.log('error: ' + err)
  }
  
}

fetchData()

//selected emotions
let selectedEmotions = {};

function updateTagsContainer() {
	let tagsContainer = document.getElementById('howyoufeel-tags-container');
	
	// Remove all existing tags
	while (tagsContainer.firstChild) {
		tagsContainer.removeChild(tagsContainer.firstChild);
	}
	
	// Add tags for the current page
	(selectedEmotions[pageCounter] || []).forEach(emotion => {
		let color = emotions_list.find(emotions => emotions.find(e => e.name == emotion)).find(e => e.name == emotion).color;
		let tag = document.createElement("div")
		let text = document.createTextNode(emotion);

		tag.appendChild(text);
		tag.style.backgroundColor = color;
		tag.id = emotion + "-" + pageCounter;
		
		tagsContainer.appendChild(tag);
	});
}

function setDefault(){
	try{
		document.getElementById("next-btn").style.visibility = "hidden"
		document.getElementById("back-explore-button").style.visibility = "hidden"
		document.getElementById("back-btn").style.visibility = "hidden"
		document.getElementById("howyoufeel-header").style.visibility = "hidden"
		document.getElementById("answer-container").style.visibility = "hidden"
		document.getElementById("next-btn").innerHTML = "Next"
	}
	catch(e){
		console.log(e)
	}
}

function checkFormInput() {
    
    for(let i = 1; i < numberOfPages - 1 ; i++) {
        if(!selectedEmotions[i] || selectedEmotions[i].length === 0) {
            
            return i;
        }
    }

    return -1;
}

function sendData() {
    
    let incompletePageIndex = checkFormInput();
    if(incompletePageIndex !== -1) {
        alert("Trebuie sa selectezi cel putin un sentiment pentru fiecare pagina.");

		console.log("Nu trimitem \"data\" :((")
		console.log(selectedEmotions)
        
        pageCounter = incompletePageIndex;
        updatePage();
        return;
    }

   
    const data = {
        formInfo: formInfo,
        selectedEmotions: selectedEmotions
    };

	console.log("Trimitem \"data\" <3")
	console.log(selectedEmotions)

    fetch(API_URL + '/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        // Aici poti prelucra raspunsul primit de la server
        console.log('Success:', data);

		// Trimit clientul la ultima pagina
		pageCounter++;
		updatePage();
    })
    .catch((error) => {
        // Aici pot gestiona eventualele erori
        console.error('Error:', error);
    });
}

function updateDescriptionPage(){
	document.getElementById("question").innerHTML = formInfo.description
	document.getElementById("next-btn").style.visibility = "visible"
}

function updateFinalPage(){
	document.getElementById("question").innerHTML = formInfo.ending
	document.getElementById("back-explore-button").style.visibility = "visible"
}

function updateQuestionPage(){
	if(pageCounter == numberOfPages - 2){
		document.getElementById("next-btn").innerHTML = "Finish"
	}
	document.getElementById("question").innerHTML = formInfo.questions[pageCounter - 1]
	document.getElementById("next-btn").style.visibility = "visible"
	document.getElementById("back-btn").style.visibility = "visible"
	document.getElementById("answer-container").style.visibility = "visible"

}

function updatePage(){
	setDefault()
	if(pageCounter == 0){
		updateDescriptionPage()
	}
	else if(pageCounter == numberOfPages - 1){
		updateFinalPage()
	}
	else{
		updateQuestionPage()
	}
	updateTagsContainer();
}

function nextPage(){
	if(pageCounter == numberOfPages - 2)
		sendData()
	else {
		pageCounter++;
		updatePage();
	}
}

function lastPage(){
	if(pageCounter == 0)
		return;
	
	pageCounter--;
	updatePage();
}

const emotions_list = [
	[{ color: "#ffffff" ,name: ""}],
	[{ color: '#2983c5', name: 'Grief' },
	{ color: '#8973b3', name: 'Loathing' },
	{ color: '#f05b61', name: 'Rage' },
	{ color: '#f6923d', name: 'Vigilance' },
	{ color: '#ffca05', name: 'Ecstasy' },
	{ color: '#8ac650', name: 'Admiration' },
	{ color: '#00a551', name: 'Terror' },
	{ color: '#0099cd', name: 'Amazement' }],
	[{ color: '#74a8da', name: 'Sadness' },
	{ color: '#a390c4', name: 'Disgust' },
	{ color: '#f2736d', name: 'Anger' },
	{ color: '#f9ad66', name: 'Anticipation' },
	{ color: '#ffdc7b', name: 'Joy' },
	{ color: '#abd26a', name: 'Trust' },
	{ color: '#30b575', name: 'Fear' },
	{ color: '#36aed7', name: 'Surprise' }],
	[{ color: '#a0c0e5', name: 'Pensiveness' },
	{ color: '#b9aad3', name: 'Boredom' },
	{ color: '#f48d80', name: 'Annoyance' },
	{ color: '#fcc487', name: 'Interest' },
	{ color: '#ffed9f', name: 'Serenity' },
	{ color: '#cadf8b', name: 'Acceptance' },
	{ color: '#7ac698', name: 'Apprehension' },
	{ color: '#89c7e4', name: 'Distraction' }],
	[{ color: '#C9C8E4', name: 'Remorse' },
	{ color: '#EABBBF', name: 'Contempt' },
	{ color: '#FBC6B2', name: 'Aggresiveness' },
	{ color: '#FFF1CA', name: 'Optimism' },
	{ color: '#F2F5C9', name: 'Love' },
	{ color: '#B2DBB1', name: 'Submission' },
	{ color: '#A9D5C3', name: 'Awe' },
	{ color: '#C3DAEF', name: 'Disapproval' }]
  ];



// Set up canvas
const canvas = document.getElementById('wheel-canvas');
canvas.width = document.getElementById('wheel-container').offsetWidth;
canvas.height = document.getElementById('wheel-container').offsetHeight;
const context = canvas.getContext('2d');


// Draw each emotion segment
for (let k = 4; k >= 0; k--) {
	
	let angle = (2 * Math.PI) / emotions_list[k].length;
	let ratio = (k + 1 ) / 5;
	let width = ratio * canvas.width;
	let height = ratio * canvas.height;
	let radius = Math.min(width, height) / 2;

	for (let i = 0; i < emotions_list[k].length; i++) {

		let startAngle = -Math.PI / 2 + i * angle;
		let endAngle = -Math.PI / 2 + (i + 1) * angle;

		if(k == 4){
			startAngle = -Math.PI / 2 + i * angle + angle/2;
			endAngle = -Math.PI / 2 + (i + 1) * angle + angle/2;
		}

		context.beginPath();
		context.moveTo(canvas.width / 2, canvas.height / 2);
		context.arc(canvas.width / 2, canvas.height / 2, radius, startAngle, endAngle);
		context.closePath();

		context.fillStyle = emotions_list[k][i].color;
		context.fill();

		let x = (canvas.width / 2 - (radius - 30) * Math.cos(Math.PI / 2 + i * angle + angle / 2));
		let y = (canvas.height / 2 - (radius - 30) * Math.sin(Math.PI / 2 + i * angle + angle / 2));

		if(k == 4){
			x = (canvas.width / 2 - (radius - 30) * Math.cos(Math.PI / 2 + i * angle + angle));
			y = (canvas.height / 2 - (radius - 30) * Math.sin(Math.PI / 2 + i * angle + angle));
		}

		context.save();
		context.textAlign = 'center';

		// Set up stroke for text
		context.strokeStyle = 'black';
		context.lineWidth = 1;

		context.font = '11px Arial';
		//context.strokeText(emotions_list[k][i].name, x, y);
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
				
				///Calculate what emotion the user clicked on
				const a = x - canvas.width/2;
				const b = y - canvas.height/2;
				const distance = Math.sqrt(a*a + b*b);

				const h = distance/(canvas.width/2) * 5

				circle_number = parseInt(h,10)
				
				if(circle_number == k && k != 0){
					
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



