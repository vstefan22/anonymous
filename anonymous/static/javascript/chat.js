"use strict";

const changeChatName = document.querySelectorAll(".fa-pen-to-square");
const deleteChat = document.querySelectorAll(".fa-trash");

changeChatName.forEach((button) => {
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

        fetch(`/chat/`, {
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

    const modal = document.querySelector(".modal");
    modal.classList.remove("deactive");
    modal.style.opacity = 1;

    const yes = document.querySelector(".yes");
    const numberOfChats = document.querySelector("#numberChats");

    yes.addEventListener("click", function () {
      const token = Cookies.get("csrftoken");
      fetch(`/delete-chat/`, {
        method: "POST",
        credentials: "same-origin",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": token,
        },
        body: JSON.stringify({ action: "Delete Chat", id: roomId }),
      }).catch(() => {
        const anonymous = document.querySelector(".container");
        const html = `<ul class="messages">
        <li
          style="
            background-color: red;
            width: fit-content;
            font-weight: bold;
            margin-left: 10%;
            padding: 10px;
            color: white;
            font-family: 'Courier New', Courier, monospace;
          "
        >
          Something went wrong, chat is not deleted. Try again later.
        </li>
      </ul>`;
        anonymous.insertAdjacentHTML("afterbegin", html);
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
      numberOfChats.innerHTML = new Number(numberOfChats.innerHTML) - 1;
    });
  });
});
