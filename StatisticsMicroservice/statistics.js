var formName;
function fetchData() {
  fetch("/data")
    .then((response) => response.json())
    .then((data) => {
      document.getElementById('title').innerHTML="Here's what people felt about the questions from " + data.form_name + ":";
      formName = data.form_name;
      createCanvasElements(data.data);
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}
fetchData();

function createCanvasElements(data) {
  const container = document.getElementById("container");
  container.innerHTML = "";
  data.forEach((item, index) => {
    const canvas = document.createElement("canvas");
    canvas.id = `${formName}Question${index+1}`;
    container.appendChild(canvas);
    createChart(canvas.id, item.question, item.answers);
  });
}

function extractNumberFromCanvasId(canvasId) {
  const regex = /(\d+)$/;
  const matches = canvasId.match(regex);
  if (matches && matches.length > 1) {
    return parseInt(matches[1]);
  }
  return null;
}

const colorMapping = {
  Grief: [41,131,197],
  Sadness: [116,168,218],
  Pensiveness: [160,192,229],
  Loathing: [137,115,179], 
  Disgust: [163,144,196], 
  Boredom: [185,170,211], 
  Rage: [240,91,97], 
  Anger: [242,115,109], 
  Annoyance: [244,141,128], 
  Vigilance: [246,146,61], 
  Anticipation: [249,173,102], 
  Interest: [252,196,135], 
  Ecstasy: [255,202,5],
  Joy: [255,220,123],
  Serenity: [255,237,159],
  Admiration: [138,198,80],
  Trust: [171,210,106],
  Acceptance: [202,223,139],
  Terror: [0,165,81],
  Fear: [48,181,117],
  Apprehension: [122,198,152],
  Amazement: [0,153,205],
  Surprise: [54,174,215],
  Distraction: [137,199,228],
  Disapproval: [195,218,239],
  Remorse: [201,200,228],
  Contempt: [234,187,191],
  Aggresiveness: [251,198,178],
  Optimism: [255,241,202],
  Love: [242,245,201],
  Submission: [178,219,177],
  Awe: [169,213,195],
};

function createChart(canvasId, question, answers) {
  Chart.defaults.backgroundColor = '#fff';
  Chart.defaults.borderColor = '#36A2EB';
  Chart.defaults.color = '#000';
  Chart.defaults.font.size = 16;
  
  const canvas = document.getElementById(canvasId);
  const ctx = canvas.getContext("2d");

  const totalCount = answers.length;

  const Answers = {};

  answers.forEach((answer) => {
    const emotions = answer.split(",");
    emotions.forEach((emotion) => {
      const trimmedEmotion = emotion.trim();
      if (Answers.hasOwnProperty(trimmedEmotion)) {
        Answers[trimmedEmotion]++;
      } else {
        Answers[trimmedEmotion] = 1;
      }
    });
  });

  const sortedAnswers = Object.keys(Answers).sort(
    (a, b) => Answers[b] - Answers[a]
  );

  const labels = sortedAnswers;
  const data = sortedAnswers.map((answer) => Answers[answer]);

  const colors = sortedAnswers.map((answer) => {
    const rgb = colorMapping[answer];
    return `rgb(${rgb.join(', ')})`;
  });

  canvas.setAttribute('data-question', question);
  canvas.setAttribute('data-answers', answers.join(','));

  const chart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: labels,
      datasets: [
        {
          label: "",
          data: data, 
          borderWidth: 1,
          backgroundColor: colors, 
        },
      ],
    },
    options: {
      plugins: {
        legend: {
          display: false,
        },
        title: {
          display: true,
          text: extractNumberFromCanvasId(canvasId) + ". " + question,
          font: {
            size: 30,
          },
        },
      },
      scales: {
        y: {
          beginAtZero: true,
          max: totalCount, 
          stepSize: 1, 
          ticks: {
            precision: 0,
            callback: function (value) {
              if (value % 1 === 0) {
                return value;
              }
              return null;
            },
          },
        },
      },
    },
  });
}

document.getElementById('downloadHTMLButton').addEventListener('click', function() {
  const htmlContent = document.documentElement.outerHTML;
  const modifiedHTML = excludeElements(htmlContent);

  const parser = new DOMParser();
  const doc = parser.parseFromString(modifiedHTML, 'text/html');

  const container = doc.getElementById('container');
  container.innerHTML=``;
  const canvases = Array.from(document.querySelectorAll('canvas'));

  const imagePromises = canvases.map((canvas) => {
    return new Promise((resolve) => {
      const tempImage = new Image();
      tempImage.onload = () => {
        const tempCanvas = document.createElement('canvas');
        const tempCtx = tempCanvas.getContext('2d');
        const rectWidth = canvas.width + 60;
        const rectHeight = canvas.height + 60;
        tempCanvas.width = rectWidth;
        tempCanvas.height = rectHeight;
        tempCtx.fillStyle = '#ffffff';
        tempCtx.fillRect(0, 0, rectWidth, rectHeight);

        const offsetX = (rectWidth - canvas.width) / 2;
        const offsetY = (rectHeight - canvas.height) / 2;

        tempCtx.drawImage(tempImage, offsetX, offsetY);

        const imageBase64 = tempCanvas.toDataURL();
        const imageElement = document.createElement('img');
        imageElement.src = imageBase64;
        container.appendChild(imageElement);
        resolve();
      };
      tempImage.src = canvas.toDataURL();
    });
  });

  Promise.all(imagePromises).then(() => {
    const serializer = new XMLSerializer();
    const modifiedHTMLString = serializer.serializeToString(doc);
    const blob = new Blob([modifiedHTMLString], { type: 'text/html' });
    const fileName = formName + ".html";
    saveAs(blob, fileName);
  });
});

function excludeElements(htmlContent) {
  var parser = new DOMParser();
  var doc = parser.parseFromString(htmlContent, 'text/html');

  // Remove elements that need to be excluded
  var elementsToExclude = [
    doc.getElementById('downloadButton'),
    doc.getElementById('download'),
    doc.querySelector('div.landing-section-header'), // Exclude landing-section-header div
    doc.querySelector('script[src="StatisticsMicroservice\\statistics.js"]'), // Exclude script element for statistics.js
    doc.querySelector('script[src="https://cdn.jsdelivr.net/npm/chart.js"]'), // Exclude script element for chart.js
    doc.querySelector('script[src="https://cdnjs.cloudflare.com/ajax/libs/FileSaver.js/2.0.5/FileSaver.min.js"]'), // Exclude script element for FileSaver.min.js
    doc.querySelector('link[rel="icon"]') // Exclude link element with rel="icon"
  ];

  elementsToExclude.forEach(function(element) {
    if (element) {
      element.parentNode.removeChild(element);
    }
  });

  // Remove script elements
  const scriptElements = doc.querySelectorAll("script");
  scriptElements.forEach((script) => script.remove());

  // Replace canvas elements with img elements containing the chart images
  const canvasElements = doc.querySelectorAll("canvas");
  canvasElements.forEach((canvas) => {
    const imageBase64 = canvas.getAttribute("data-chart-image");
    const imgElement = doc.createElement("img");
    imgElement.src = imageBase64;
    canvas.parentNode.replaceChild(imgElement, canvas);
  });

  // Inline CSS styles from external CSS files
  var styleElements = doc.querySelectorAll('link[rel="stylesheet"]');
  styleElements.forEach(function(styleElement) {
    var cssContent = '';
    var href = styleElement.getAttribute('href');
    var xhr = new XMLHttpRequest();
    xhr.open('GET', href, false);
    xhr.onreadystatechange = function() {
      if (xhr.readyState === 4 && xhr.status === 200) {
        cssContent = xhr.responseText;
      }
    };
    xhr.send();

    var style = doc.createElement('style');
    style.innerHTML = cssContent;
    styleElement.parentNode.replaceChild(style, styleElement);
  });

  return doc.documentElement.outerHTML;
}

document.getElementById('downloadCSVButton').addEventListener('click', function() {
  const data = getDataFromCanvasElements();
  const csvContent = convertToCSV(data);
  const encodedURI = encodeURI(csvContent);
  const link = document.createElement('a');
  link.setAttribute('href', 'data:text/csv;charset=utf-8,' + encodedURI);
  const fileName = formName + ".csv";
  link.setAttribute('download', fileName);
  link.style.display = 'none';
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
})

function getDataFromCanvasElements() {
  const canvasElements = document.querySelectorAll('canvas');
  const data = [];

  canvasElements.forEach((canvas) => {
    const question = canvas.getAttribute('data-question');
    const answers = canvas.getAttribute('data-answers').split(',');

    const Answers = {};
    answers.forEach((answer) => {
      const trimmedAnswer = answer.trim();
      if (Answers.hasOwnProperty(trimmedAnswer)) {
        Answers[trimmedAnswer]++;
      } else {
        Answers[trimmedAnswer] = 1;
      }
    });

    data.push({ question, Answers });
  });

  return data;
}

function convertToCSV(data) {
  let csv = 'Question,Answer,Count\n';

  data.forEach((item, index) => {
    const { question, Answers } = item;

    // Add the question row with an empty answer and count
    csv += `"${index + 1}. ${question}",,\n`;

    Object.entries(Answers).forEach(([answer, count]) => {
      // Add a new row for each answer and count
      csv += `,"${answer}",${count}\n`;
    });
  });

  return csv;
}

document.getElementById('downloadJSONButton').addEventListener('click', function() {
  const data = getDataFromCanvasElements();
  const jsonData = JSON.stringify(data, null, 2);
  const encodedURI = encodeURI(jsonData);
  const link = document.createElement('a');
  link.setAttribute('href', 'data:application/json;charset=utf-8,' + encodedURI);
  const fileName = formName + ".json";
  link.setAttribute('download', fileName);
  link.style.display = 'none';
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
});













