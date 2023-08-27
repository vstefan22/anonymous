"use strict";

const likes = document.querySelectorAll(".likes");
const dislikes = document.querySelectorAll(".dislikes");
const sort = document.querySelector("#sort");
const select = document.querySelector("#select-option");
const dateCommentSort = document.querySelectorAll(".comment");

const body = document.body;

const interaction = async function (value, interaction, id, postId) {
  const token = Cookies.get("csrftoken");

  await fetch(`/post/${postId}/`, {
    method: "POST",
    credentials: "same-origin",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": token,
    },
    body: JSON.stringify({ value: value, interaction: interaction, id: id }),
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
    Something went wrong, try again later.
  </li>
</ul>`;
    anonymous.insertAdjacentHTML("afterbegin", html);
  });
};

likes.forEach((like) => {
  like.addEventListener("click", function (e) {
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
    console.log(id);

    const postId = like.dataset.postid;

    if (clickedLike.classList.contains("fa-solid")) {
      // 1) Add number of likes and display value in DOM
      const updateNumberOfLikes = 1 + +numberOfLikes.innerHTML;
      numberOfLikes.innerHTML = updateNumberOfLikes;

      // 2) Send data to backend using AJAX
      interaction(1, "like", id, postId);
    }
    if (clickedLike.classList.contains("fa-regular")) {
      // 1) Subtract number of likes and display value in DOM
      const updateNumberOfLikes = 1 - +numberOfLikes.innerHTML;
      numberOfLikes.innerHTML = updateNumberOfLikes;

      // 2) Send data to backend using AJAX
      interaction(-1, "like", id, postId);
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
    const postId = dislike.dataset.postid;

    if (clickedDislike.classList.contains("fa-solid")) {
      // 1) Add number of likes and display value in DOM
      const updateNumberOfDislikes = 1 + +numberOfDislikes.innerHTML;
      numberOfDislikes.innerHTML = updateNumberOfDislikes;

      // 2) Send data to backend using AJAX
      interaction(1, "dislike", id, postId);
    }
    if (clickedDislike.classList.contains("fa-regular")) {
      // 1) Subtract number of likes and display value in DOM
      const updatenumberOfDislikes = 1 - +numberOfDislikes.innerHTML;
      numberOfDislikes.innerHTML = updatenumberOfDislikes;

      // 2) Send data to backend using AJAX
      interaction(-1, "dislike", id, postId);
    }
  });
});

sort.addEventListener("click", function () {
  const modal = document.querySelector(".sort-modal");

  select.classList.toggle("hidden");
  // const sorted = [...comment].sort((a, b) => {
  //   return new Date(b.date) - new Date(a.date);
  // });
  // sorted.forEach((div) => parent.append(div));

  select.addEventListener("change", function (e) {
    const selectedValue = select.value;
    const parent = document.querySelector(".comment-section");
    const comment = document.querySelectorAll(".comment");
    // Remove all comments
    comment.forEach((div) => div.remove());
    if (selectedValue === "likes") {
      const sorted = [...comment].sort((a, b) => {
        return (
          b.children[1].children[0].children[1].innerHTML -
          a.children[1].children[0].children[1].innerHTML
        );
      });
      sorted.forEach((div) => parent.append(div));
    } else if (selectedValue === "dislikes") {
      const sorted = [...comment].sort((a, b) => {
        return (
          b.children[1].children[1].children[1].innerHTML -
          a.children[1].children[1].children[1].innerHTML
        );
      });
      sorted.forEach((div) => parent.append(div));
    } else if (selectedValue === "date") {
      dateCommentSort.forEach((div) => parent.append(div));
    }
    e.preventDefault();
  });
  // Close when click is outside of select element
  body.addEventListener("click", function (e) {
    if (e.target.id === "sort") return;
    if (!select.classList.contains("hidden")) {
      select.classList.add("hidden");
    }
  });
});
