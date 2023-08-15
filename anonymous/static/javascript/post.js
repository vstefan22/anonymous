"use strict";
const likes = document.querySelectorAll(".likes");
const dislikes = document.querySelectorAll(".dislikes");
const sort = document.querySelector("#sort");
const select = document.querySelector("#select-option");
const body = document.body;
const dateCommentSort = document.querySelectorAll(".comment");
const interaction = function (value, interaction, e) {
  e.preventDefault();
  const id = e.srcElement.dataset.id;
  const postId = e.srcElement.dataset.postid;
  const token = Cookies.get("csrftoken");

  fetch(`http://127.0.0.1:8000/comment-like/${id}/${postId}/`, {
    method: "POST",
    credentials: "same-origin",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": token,
    },
    body: JSON.stringify({ value: value, interaction: interaction, id: id }),
  });
};

const updateInteraction = function (condition, e) {
  let interactionNumber;
  if (condition === "minus") {
    interactionNumber = new Number(e.target.parentNode.lastChild.innerHTML) - 1;
    e.target.classList.add("fa-regular");
    e.target.classList.remove("fa-solid");
  } else {
    interactionNumber = new Number(e.target.parentNode.lastChild.innerHTML) + 1;
    e.target.classList.remove("fa-regular");
    e.target.classList.add("fa-solid");
  }
  e.target.parentNode.lastChild.innerHTML = interactionNumber;
};

likes.forEach((like) => {
  like.addEventListener("click", function (e) {
    if (e.target.parentNode.lastChild.classList.contains("active")) {
      interaction(-1, "l", e);
      updateInteraction("minus", e);
      e.target.parentNode.lastChild.classList.remove("active");
      return;
    }
    interaction(1, "l", e);
    updateInteraction("plus", e);
    e.target.parentNode.lastChild.classList.add("active");
  });
});

dislikes.forEach((dislike) => {
  dislike.addEventListener("click", function (e) {
    if (e.target.parentNode.lastChild.classList.contains("active")) {
      interaction(-1, "d", e);
      updateInteraction("minus", e);
      e.target.parentNode.lastChild.classList.remove("active");
      return;
    }
    interaction(1, "d", e);
    updateInteraction("plus", e);
    e.target.parentNode.lastChild.classList.add("active");
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
