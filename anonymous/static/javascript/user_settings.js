"use strict";

const accountInfo = document.querySelector(".account-info");
const buttonClicked = document.querySelector("#delete-account");
const blogsPosted = document.querySelector(".blogs-posted");
const sort = document.querySelector("#sort");
const select = document.querySelector("#select-option");
const dateBlogSort = document.querySelectorAll(".blog");

buttonClicked.addEventListener("click", function (e) {
  e.preventDefault();
  const html = `<ul class="messages">
        <li>
          Are you sure you want to delete your account? If you delete account you won't be able to get data again and all blogs, chats, and comments will be lost! Are you sure you want to procceed?
        </li>
        <button id = "yes">Yes, I want to delete my account!</button>
        <button id = "cancel">Cancel </button>
      </ul>`;
  accountInfo.insertAdjacentHTML("afterbegin", html);

  const yes = document.querySelector("#yes");
  const cancel = document.querySelector("#cancel");
  yes.addEventListener("click", function () {
    const token = Cookies.get("csrftoken");
    fetch(`/user-settings/`, {
      method: "POST",
      credentials: "same-origin",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": token,
      },
    });
    cancel.addEventListener("click", function () {
      document.querySelector(".messages").classList.add("hidden");
    });
  });
});

blogsPosted.lastChild.previousSibling.classList.add("hidden");

sort.addEventListener("click", function () {
  select.classList.toggle("hidden");
  select.addEventListener("change", function (e) {
    const selectedValue = select.value;
    const parent = document.querySelector(".blogs-posted");
    const blog = document.querySelectorAll(".blog");

    // Remove all blogs
    blog.forEach((div) => div.remove());
    if (selectedValue === "likes") {
      const sorted = [...blog].sort((a, b) => {
        return (
          b.children[1].children[0].children[1].innerHTML -
          a.children[1].children[0].children[1].innerHTML
        );
      });
      sorted.forEach((div) => parent.append(div));
    } else if (selectedValue === "dislikes") {
      const sorted = [...blog].sort((a, b) => {
        return (
          b.children[1].children[1].children[1].innerHTML -
          a.children[1].children[1].children[1].innerHTML
        );
      });
      sorted.forEach((div) => parent.append(div));
    } else if (selectedValue === "date") {
      dateBlogSort.forEach((div) => parent.append(div));
    }
    if (selectedValue === "views") {
      const sorted = [...blog].sort((a, b) => {
        console.log();
        return (
          b.children[0].querySelector(".fa-regular").innerHTML -
          a.children[0].querySelector(".fa-regular").innerHTML
        );
      });
      sorted.forEach((div) => parent.append(div));
    }
    e.preventDefault();
  });
  // Close when click is outside of select element
  const container = document.querySelector(".container");
  container.addEventListener("click", function (e) {
    if (e.target.id === "sort") return;
    if (!select.classList.contains("hidden")) {
      select.classList.add("hidden");
    }
  });
});
