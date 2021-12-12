import "./style.css";

const BASE_URL = "http://localhost:5000";

const $form = document.querySelector("form");
const $message = document.querySelector("#message");
const $output = document.querySelector(".output");
const $button = document.querySelector("#submitForm");

$message.addEventListener("keyup", (e) => {
  // backspace
  if (e.keyCode === 8) {
    $output.classList.remove("spam");
    $output.classList.remove("ham");
    $message.classList.remove("spam");
    $message.classList.remove("ham");
    $output.innerHTML = `<p></p>`;
  }

  // ctrl + enter
  if (e.keyCode === 13 && e.ctrlKey) {
    $button.click();
  }
});

$form.addEventListener("submit", (e) => {
  e.preventDefault();
  const message = $message.value;
  console.log(message);
  fetch(`${BASE_URL}/test`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ message }),
  })
    .then((res) => res.json())
    .then((data) => {
      if (data.result === "ham") {
        $output.classList.remove("spam");
        $output.classList.add("ham");
        $message.classList.remove("spam");
        $message.classList.add("ham");
        $output.innerHTML = `<p>Looks Good</p>`;
      } else {
        $output.classList.remove("ham");
        $output.classList.add("spam");
        $message.classList.remove("ham");
        $message.classList.add("spam");
        $output.innerHTML = `<p>Looks like SPAM !!</p>`;
      }
    })
    .catch((err) => console.log(err));
});
