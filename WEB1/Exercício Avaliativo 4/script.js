function paginaCarregada() {
  alert("Calcula soma");
}

function soma() {
  const num1 = document.getElementById("num1");
  const num2 = document.getElementById("num2");
  const resultado = document.getElementById("resultado");
  resultado.textContent =
    (parseInt(num1.value) || 0) + (parseInt(num2.value) || 0);
}

function ajudaFocus(input) {
  document.getElementById("ajuda").textContent = "informe um operando";
  input.style.backgroundColor = "cyan";
}

function ajudaBlur(input) {
  document.getElementById("ajuda").textContent = "";
  input.style.backgroundColor = "";
}

function mudaCorResultado(cor) {
  document.getElementById("resultado").style.color = cor;
}
