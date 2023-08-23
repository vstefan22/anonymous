"use strict";

const likes = document.querySelectorAll(".likes");
const dislikes = document.querySelectorAll(".dislikes");

const interaction = function (value, interaction, e) {
  e.preventDefault();
  const id = e.srcElement.dataset.id;
  const token = Cookies.get("csrftoken");
  fetch(`http://127.0.0.1:8000/`, {
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
    e.target.classList.toggle("fa-regular");
    e.target.classList.toggle("fa-solid");
  } else {
    interactionNumber = new Number(e.target.parentNode.lastChild.innerHTML) + 1;
    e.target.classList.remove("fa-regular");
    e.target.classList.add("fa-solid");
  }
  e.target.parentNode.lastChild.innerHTML = interactionNumber;
};
// 0 children 11 child nodes activeElement ownerDocument target
// Interaction clicks
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
