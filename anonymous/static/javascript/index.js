const openModal = document.querySelectorAll(".modal");
const modalContent = document.querySelectorAll(".modal-content");
const close = document.querySelectorAll(".close");
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
