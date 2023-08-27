"use strict";

const likes = document.querySelectorAll(".likes");
const dislikes = document.querySelectorAll(".dislikes");

const interaction = async function (value, interaction, id) {
  const token = Cookies.get("csrftoken");
  const hostLocation = window.location;
  await fetch(`${hostLocation}`, {
    method: "POST",
    credentials: "same-origin",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": token,
    },
    body: JSON.stringify({ value: value, interaction: interaction, id: id }),
  }).catch(() => {
    const anonymous = document.querySelector(".anonymous");
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
      Something went wrong, try again later.
    </li>
  </ul>`;
    anonymous.insertAdjacentHTML("afterbegin", html);
  });
};

likes.forEach((like) => {
  like.addEventListener("click", function () {
    const clickedLike = like.querySelector(".fa-thumbs-up");
    const numberOfLikes = like.querySelector(".like");
    if (
      like.nextElementSibling.querySelector(".dislike").classList.contains("active") ||
      like.nextElementSibling.querySelector(".fa-thumbs-down").classList.contains("fa-solid")
    )
      return;
    // Change from solid to regular
    clickedLike.classList.toggle("fa-regular");
    clickedLike.classList.toggle("fa-solid");
    const id = like.dataset.id;

    if (clickedLike.classList.contains("fa-solid")) {
      // 1) Add number of likes and display value in DOM
      const updateNumberOfLikes = 1 + +numberOfLikes.innerHTML;
      numberOfLikes.innerHTML = updateNumberOfLikes;

      // 2) Send data to backend using AJAX
      interaction(1, "like", id);
    }
    if (clickedLike.classList.contains("fa-regular")) {
      // 1) Subtract number of likes and display value in DOM
      const updateNumberOfLikes = 1 - +numberOfLikes.innerHTML;
      numberOfLikes.innerHTML = updateNumberOfLikes;

      // 2) Send data to backend using AJAX
      interaction(-1, "like", id);
    }
  });
});

dislikes.forEach((dislike) => {
  dislike.addEventListener("click", function (e) {
    const clickedDislike = dislike.querySelector(".fa-thumbs-down");
    const numberOfDislikes = dislike.querySelector(".dislike");
    console.log(dislike.previousElementSibling.querySelector(".like"));
    if (
      dislike.previousElementSibling.querySelector(".like").classList.contains("active") ||
      dislike.previousElementSibling.querySelector(".fa-thumbs-up").classList.contains("fa-solid")
    )
      return;
    // Change from solid to regular
    clickedDislike.classList.toggle("fa-regular");
    clickedDislike.classList.toggle("fa-solid");
    const id = dislike.dataset.id;

    if (clickedDislike.classList.contains("fa-solid")) {
      // 1) Add number of likes and display value in DOM
      const updateNumberOfDislikes = 1 + +numberOfDislikes.innerHTML;
      numberOfDislikes.innerHTML = updateNumberOfDislikes;

      // 2) Send data to backend using AJAX
      interaction(1, "dislike", id);
    }
    if (clickedDislike.classList.contains("fa-regular")) {
      // 1) Subtract number of likes and display value in DOM
      const updatenumberOfDislikes = 1 - +numberOfDislikes.innerHTML;
      numberOfDislikes.innerHTML = updatenumberOfDislikes;

      // 2) Send data to backend using AJAX
      interaction(-1, "dislike", id);
    }
  });
});
