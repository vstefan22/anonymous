"use strict";

const openModal = document.querySelectorAll(".modal");
const modalContent = document.querySelectorAll(".modal-content");
const close = document.querySelectorAll(".close");
const likes = document.querySelectorAll(".likes");
const dislikes = document.querySelectorAll(".dislikes");
openModal.forEach((el, i) =>
  el.addEventListener("click", function (e) {
    console.log(el);
    modalContent[i].classList.remove("hidden");
    modalContent[i].classList.remove("animation");
  })
);
close.forEach((el, i) =>
  el.addEventListener("click", function () {
    modalContent[i].classList.add("animation");
    // Prevent animation from staying, make animation class remove when animation is finished
    setTimeout(function () {
      modalContent[i].classList.remove("animation");
      modalContent[i].classList.add("hidden");
      console.log("a");
    }, 250);
  })
);
const interaction = function (value, interaction, e) {
  e.preventDefault();
  const id = e.srcElement.dataset.id;
  const token = Cookies.get("csrftoken");
  let xhttp = new XMLHttpRequest();

  xhttp.open("POST", "/", true);
  xhttp.setRequestHeader("X-CSRFToken", token);
  xhttp.setRequestHeader("Content-Type", "application/json");
  xhttp.send([value, interaction, id]);
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
    // e.target.classList.add("hidden");

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
