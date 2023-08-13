"use strict";

const chnageName = document.querySelectorAll(".fa-pen-to-square");

chnageName.forEach((button) => {
  button.addEventListener("click", function (e) {
    e.preventDefault();
    const clickedValue = e.target.closest(".room-name");
    console.log(clickedValue);
    const roomId = e.target.dataset.id;
    console.log(roomId);
    const clickedName = clickedValue.querySelector(".room-title");
    clickedName.classList.add("hidden");
    const html = `<input type="text" class='name-change' placeholder="${clickedName.innerHTML}">`;
    clickedValue.insertAdjacentHTML("afterbegin", html);
    const inputField = document.querySelector(".name-change");
    inputField.addEventListener("click", function (e) {
      e.preventDefault();
    });
    inputField.addEventListener("keypress", function (e) {
      if (e.key === "Enter") {
        e.preventDefault();
        const value = inputField.value;
        console.log(value);
        const token = Cookies.get("csrftoken");
        fetch(`http://127.0.0.1:8000/chat/`, {
          method: "POST",
          credentials: "same-origin",
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": token,
          },
          body: JSON.stringify({ data: value, id: roomId }),
        });

        inputField.classList.add("hidden");
        clickedName.classList.remove("hidden");
        clickedName.innerHTML = value;
      }
    });
  });
});
