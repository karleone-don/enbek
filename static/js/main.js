const screen1 = document.getElementById("screen1")
const screen2 = document.getElementById("screen2")

const conclusionField = document.getElementById("info-col-conclusion")
const adviceField = document.getElementById("info-col-advice")

const spinner = document.getElementById("spinner")
const spinnerText = document.getElementById("spinner-text")

let gender
let age
let education
let experience
let information
let project
let timeManagement
let situation


function changeGender(genderChoice){
    document.getElementById("button-female").style.backgroundColor = "#fff";
    document.getElementById("button-male").style.backgroundColor = "#fff";
    document.getElementById("button-female").style.cursor = "pointer";
    document.getElementById("button-male").style.cursor = "pointer";
    document.getElementById("button-"+genderChoice).style.backgroundColor = "#FF8C1C";
    document.getElementById("button-"+genderChoice).style.cursor = "inherit";
    if (genderChoice == "male"){
        gender = "Мужской"
    } else if (genderChoice == "female"){
        gender = "Женский"
    }
}

function nextScreen(){
    age = document.getElementById("age").value
    education = document.getElementById("education").value
    experience = document.getElementById("experience").value
    information = document.getElementById("information").value
    project = document.getElementById("project").value
    timeManagement = document.getElementById("timeManagement").value
    situation = document.getElementById("situation").value

    $.ajax({
        url: '/process',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            gender: gender,
            age: age,
            education: education,
            experience: experience,
            information: information,
            project: project,
            time_management: timeManagement,
            situation: situation
        }),
        success: function(response) {
            printGenerate(response.conclusion, response.advice)
        }
    });

    screen1.style.animation = "next-screen 3s"
    screen1.addEventListener('animationend', function() {
        screen1.style.display = 'none'
        spinner.style.display = "block"
        spinnerText.style.display = "block";
        spinner.style.animation = "start 2s"
        spinnerText.style.animation = "start 2s"
        spinner.addEventListener('animationend', function() {
            spinner.style.animation = "rotate 2s linear infinite"
            // printGenerate()
        }, {once: true})
    }, {once: true})
}

function printGenerate(conclusion, advice){
    spinner.style.animation = "end 2s"
    spinnerText.style.animation = "end 2s"
    spinner.addEventListener('animationend', function() {
        spinner.style.display = "none"
    })
    spinnerText.addEventListener('animationend', function() {
        spinnerText.style.display = "none"
    })

    screen2.style.display = 'flex'
    screen2.style.animation = "next-screen2 3s"
    conclusionField.innerHTML = conclusion
    adviceField.innerHTML = advice
}

function onMain(){
    window.location.reload();
}