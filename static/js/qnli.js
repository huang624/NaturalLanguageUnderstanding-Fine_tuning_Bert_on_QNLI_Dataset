const button = document.getElementById("btn-submit");
const resultBox = document.getElementById("results-div");
const spinner = document.createElement("span");
spinner.classList.add("spinner-grow");
spinner.classList.add("spinner-grow-sm");
spinner.setAttribute("role", "status");
spinner.setAttribute("aria-hidden", true);

function toggleButtonState() {
  if (button.disabled) {
    button.disabled = false;
    button.removeChild(spinner);
    button.innerText = "Compute";
  } else {
    button.innerText = "Loading...";
    button.insertBefore(spinner, button.firstChild);
    button.disabled = true;
  }
}

function toggleResultBox(show = true) {
  if (show === true) {
    resultBox.style.display = "block";
  } else {
    resultBox.style.display = "none";
  }
}

function successResultBox() {
  resultBox.classList.remove("alert-danger");
  resultBox.classList.add("alert-success");
}

function failResultBox() {
  resultBox.classList.remove("alert-success");
  resultBox.classList.add("alert-danger");
}

function fillTextGenResult(modelOutput) {
  let outputString = modelOutput;
  resultBox.innerHTML = outputString;
}

async function submitForm(event) {
  event.preventDefault();

  const question = document.getElementById("question-1").value;
  const sentence = document.getElementById("sentance-1").value;
  
  console.log(question);
  toggleButtonState();
  toggleResultBox(false);
  try {
    await fetch("/qnli", {
      method: "POST",
      body: JSON.stringify({ question, sentence }),
      headers: new Headers({
        "Content-Type": "application/json; charset=UTF-8",
      }),
    })
      .then(async (response) => {
        if (!response.ok) {
          const errorDetail = JSON.stringify(await response.json());
          throw new Error(
            `Request failed for ${response.statusText} (${response.status}): ${errorDetail}`
          );
        }
        return response.json();
      })
      .then((data) => {
        console.log(data);
        successResultBox();
        fillTextGenResult(data);
      });
  } catch (error) {
    console.error(error);
    failResultBox();
    resultBox.innerText = error;
  } finally {
    toggleButtonState();
    toggleResultBox();
  }
}

button.addEventListener("click", submitForm, false);
