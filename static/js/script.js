init();

// entrance card effect (runs once)
const cards = document.querySelectorAll(".card");
cards.forEach((card, index) => {
  card.style.animation // checa se já existe animação
    ? (card.style.animation = "")
    : (card.style.animation = `animate-slide 0.7s backwards ${
        index / 7 + 0.3
      }s`);
});

// navigation screen toggle (mobile devices only)
const hamburger = document.querySelector(".hamburger");
const overlay = document.querySelector(".overlay");

hamburger.addEventListener("click", function () {
  hamburger.classList.toggle("active");

  if (overlay.classList.contains("active")) {
    overlay.style.opacity = "0";
    overlay.style.visibility = "hidden";
  } else {
    overlay.style.opacity = "1";
    overlay.style.visibility = "visible";
  }

  overlay.classList.toggle("active");
});

// Swup library instance
const swup = new Swup({
  containers: ["#swup", ".swup-a"],
});



// on page change, reload some JavaScript functions
// (Swup default behavior removes a standard lifecycle of scripts)
swup.on("contentReplaced", init);

function init() {
  if (document.querySelector("form")) {
    let timeout;
    const boxes = $(".box");
    const buttons = $(".btn");

    boxes.on("input", function () {
      clearTimeout(timeout);
      timeout = setTimeout(() => {
        // console.log('parou de digitar')

        if (
          $("input:text").filter(function () {
            return this.value == "";
          }).length === 0
        )
          buttons.addClass("btn-enabled");
        else {
          if (buttons.hasClass("btn-enabled"))
            buttons.removeClass("btn-enabled");
        }
      }, 1000); // 1 sec.
    });

    let form = $("#form");

    form.on("submit", function (event) {
      event.preventDefault();

      const data = new FormData(document.getElementById("form"));

      fetch("/app-school/curso/inserir", {
        method: "POST",
        body: data,
      })
        .then(function (response) {
          if (response.status === 200) {
            form.removeClass("animate__animated animate__zoomOutRight");
            form.addClass("animate__animated animate__zoomOutRight");
            form.on("animationend", function () {
              // window.location.href = "/app-school/curso/listar";
              return swup.loadPage({ url: "/app-school/curso/listar" });
            });
          } 
          
          if (!response.ok) {
            form.removeClass("animate__animated animate__headShake");
            form.addClass("animate__animated animate__headShake");
          }

          console.log(response)
        })
        .then((data) => {
          // console.log("data:asdf " + data);
          // faça alguma coisa com o texto da resposta aqui
        })
        .catch((error) => {
          console.error("deu erro em: " + error);
          // faça alguma coisa com o erro aqui
        });

      // $("body").css("overflow", "hidden");
    });

    $("#cancel").click(function () {
      $("body").css("overflow", "hidden");
      form.removeClass("animate__animated animate__hinge");
      form.addClass("animate__animated animate__hinge");
      form.on("animationend", function () {
        // window.location.href = "/app-school/curso/listar";
        return swup.loadPage({ url: "/app-school/curso/listar" });
      });
    });
  }
}

function definirCursoEstudante(curso) {
  document.getElementById("curso").value = curso;
}

function ajaxToGithub() {}
