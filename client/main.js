import "./style.css";

const BASE_URL = "http://localhost:5000";

const $form = document.querySelector("form");
const $message = document.querySelector("#message");
const $output = document.querySelector(".output");
const $button = document.querySelector("#submitForm");

$message.addEventListener("keyup", (e) => {
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
      console.log(data);
      $output.innerHTML = `<p>${JSON.stringify(data, undefined, 2)}</p>`;
    })
    .catch((err) => console.log(err));
});
