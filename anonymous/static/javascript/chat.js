"use strict";

const chnageName = document.querySelectorAll(".fa-pen-to-square");
const deleteChat = document.querySelectorAll(".fa-trash");

chnageName.forEach((button) => {
  button.addEventListener("click", function (e) {
    e.preventDefault();
    const clickedValue = e.target.closest(".room-name");
    const roomId = e.target.dataset.id;
    const clickedName = clickedValue.querySelector(".room-title");
    const html = `<input type="text" class='name-change' placeholder="${clickedName.innerHTML}">`;

    clickedName.classList.add("hidden");
    clickedValue.insertAdjacentHTML("afterbegin", html);

    const inputField = document.querySelector(".name-change");
    inputField.addEventListener("click", function (e) {
      e.preventDefault();
    });
    inputField.addEventListener("keypress", function (e) {
      if (e.key === "Enter") {
        e.preventDefault();
        const value = inputField.value;
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

deleteChat.forEach((chat) => {
  chat.addEventListener("click", function (e) {
    e.preventDefault();
    const roomId = e.target.dataset.id;
    const roomDiv = e.target.closest(".room");
    console.log(roomDiv);
    const modal = document.querySelector(".modal");
    const yes = document.querySelector(".yes");
    modal.classList.remove("deactive");
    modal.style.opacity = 1;
    yes.addEventListener("click", function () {
      const token = Cookies.get("csrftoken");
      fetch(`http://127.0.0.1:8000/delete-chat/`, {
        method: "POST",
        credentials: "same-origin",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": token,
        },
        body: JSON.stringify({ action: "Delete Chat", id: roomId }),
      });
      function fadeOut(element) {
        let opacity = 1;
        setInterval(function () {
          if (opacity > 0) {
            opacity -= 0.1;
            element.style.opacity = opacity;
          }
        }, 20);
      }
      fadeOut(roomDiv);
      fadeOut(modal);
      roomDiv.classList.add("hidden");
      modal.classList.add("hidden");
    });
  });
});
