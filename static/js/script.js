// Javascript module

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


// Toastr library options
toastr.options = {
  closeButton: true,
  progressBar: true,
  positionClass: "toast-bottom-right",
  preventDuplicates: true,
  showEasing: "swing",
  hideEasing: "swing",
  showMethod: "slideDown",
  hideMethod: "fadeOut",
};  


// Swup library instance
const swup = new Swup({
  containers: ["#swup", ".swup-a"],
  cache: false
});

// on page change, reload some JavaScript functions
// (Swup default behavior removes a standard lifecycle of scripts)
swup.on("contentReplaced", init);



function init() {
  
  if (document.querySelector("form")) {

    let timeout;
    const boxes = $(".box");
    const buttons = $(".btn");
    const form = $("#form");
    const cancelButton = $("#cancel");
    const siglaButton = $("#btn-sigla");
    
    document.querySelector("#form").addEventListener("submit", submitForm);
    boxes.on("input", inspectBoxes);
    cancelButton.click(cancelForm);
    siglaButton.on("click", requestSigla);
    
    inspectBoxes();
    
    function inspectBoxes() {
      clearTimeout(timeout);
      timeout = setTimeout(() => {

      if (
        boxes.filter(function () {
          return this.value == "";
        }).length === 0
      )
        buttons.addClass("btn-enabled");
      
      else {
        if (buttons.hasClass("btn-enabled"))
        buttons.removeClass("btn-enabled");
        }
      }, 1000); // 1 sec.
    }

    
    function submitForm(event) {
      event.preventDefault();
      
      const target = event.target;

      const url = target.getAttribute("data-action");
      const formData = new FormData(target);

      fetch(url, {
        method: "POST",
        body: formData
      })
      .then(response => { console.log(response)
        if (response.status === 200) {
          let redirect = "/app-school/curso/listar" 

          handleAnimateCSS("form", "zoomOutRight", redirect)
          toastr.success("Envio bem-sucedido", "Sucesso");
          return true;
        } 
        else {
          let errorMessage = response.headers.get("Error-Message");

          handleAnimateCSS("form", "headShake")
          toastr.error( errorMessage, "Erro");
          return false;
        }
      })
      .catch((error) => {
        toastr.warning(
          `Problemas encontrados na aplicação. Volte mais tarde, por favor: (${error})`
        );
      })
    }
    
    let url = window.location.pathname.split("?")[0].split("/");
      console.log(url);
    function cancelForm () {
      
      let animation;
      $(".fill-space").css("overflow", "hidden");
      
      switch (url[url.length - 1]) {
        case "novo":
          animation = "hinge";
          break;

        case "remover":
          animation = "bounceOutDown";
          break;
          
        default:
          animation = "fadeOutRight animate__faster";
          break;
        }

          form.removeClass(`animate__animated animate__${animation}`);
          form.addClass(`animate__animated animate__${animation}`);
          form.on("animationend", function () {
            // window.location.href = "/app-school/curso/listar";
            return swup.loadPage({ url: "/app-school/curso/listar" });
          });
        }
      }
      
      
      function requestSigla() {
        let nome = document.querySelector("[name='nome']").value;
        
        if (!nome || !nome.trim()) {
          return toastr.info("Insira um nome não vazio.");
        }
  
        fetch("/app-school/curso/gerar-sigla", {
          method: "POST", 
          headers: { "Accept": "application/json",
                     "Content-Type": "application/json"},
          body: JSON.stringify(nome)
        })
          .then((response) => response.json())
          .then((result) => { 
            document.querySelector("[name='sigla']").value = result
        });
      }
    }
    

init();


function definirCursoEstudante(curso) {
  document.getElementById("curso").value = curso;
}


function handleAnimateCSS(element, animation, url="", customFunc=undefined) {
  
  const prefix = "animate__"
  const animationName = `${prefix}${animation}`;
  const node = document.querySelector(element);

  node.classList.add(`${prefix}animated`, animationName);

  function endAnimate(event) {
    customFunc ? customFunc() : {};
    console.log(url.length);
    if (url.length > 0) { swup.loadPage({ url: url }); } 
    else {node.classList.remove(`${prefix}animated`, animationName);}
  }

  node.addEventListener("animationend", endAnimate);
}