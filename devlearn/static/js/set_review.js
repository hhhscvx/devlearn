document.addEventListener("DOMContentLoaded", (_) => {
  let reviewBtn = document.getElementById("review");
  let completedPercent = reviewBtn.dataset.completedPercent;
  completedPercent = Math.floor(parseFloat(completedPercent.replace(",", ".")));

  let blockReviewNotAllowed = document.getElementById("reviewNotAllowed");
  let reviewModal = document.getElementById("reviewModal");
  let closeBtn = document.querySelector(".close");
  let timer;

  form = document.getElementById("form-review");
  firstElem = form.elements[0];
  lastElem = form.elements[form.elements.length - 1];

  reviewBtn.addEventListener("click", (event) => {
    event.preventDefault();
    if (timer) {
      clearTimeout(timer);
    }

    if (completedPercent < 80) {
      blockReviewNotAllowed.style.display = "block";
      setTimeout(() => {
        blockReviewNotAllowed.style.opacity = 1;
      }, 10);
      timer = setTimeout(() => {
        blockReviewNotAllowed.style.opacity = 0;
        setTimeout(() => {
          blockReviewNotAllowed.style.display = "none";
        }, 500);
      }, 5000);
    } else {
      reviewModal.style.display = "block";
    }
  });

  closeBtn.addEventListener("click", () => {
    reviewModal.style.display = "none";
  });

  window.addEventListener("click", (event) => {
    if (event.target == reviewModal) {
      reviewModal.style.display = "none";
    }
  });

  // firstElem.onkeydown = function (e) {
  //   if (e.key == "Tab" && e.shiftKey) {
  //     lastElem.focus();
  //     return false;
  //   }
  // };

  // lastElem.onkeydown = function (e) {
  //   if (e.key == "Tab" && !e.shiftKey) {
  //     firstElem.focus();
  //     return false;
  //   }
  // };

  // console.log(form.elements);
  // form.elements.review.focus();
});
