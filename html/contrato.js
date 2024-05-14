spans = document.querySelectorAll("span")
inputs = document.querySelectorAll("input")
inputs.forEach((input, index) => input.addEventListener("keyup", () => spans[index].textContent = input.value))