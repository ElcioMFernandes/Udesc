class ValidadorIdade {
  constructor(dataNasc) {
    this.dataNasc = new Date(dataNasc);
    this.hoje = new Date();
  }

  getIdade() {
    let idade = this.hoje.getFullYear() - this.dataNasc.getFullYear();
    const mes = this.hoje.getMonth() - this.dataNasc.getMonth();
    if (
      mes < 0 ||
      (mes === 0 && this.hoje.getDate() < this.dataNasc.getDate())
    ) {
      idade--;
    }
    return idade;
  }

  maiorDeIdade() {
    return this.getIdade() >= 18;
  }
}

const input = document.getElementById("dataNasc");
const msg = document.getElementById("msgIdade");
const form = document.getElementById("formNasc");

input.addEventListener("input", function () {
  if (!input.value) {
    msg.textContent = "";
    msg.className = "mensagem";
    return;
  }
  const validador = new ValidadorIdade(input.value);
  if (!validador.maiorDeIdade()) {
    msg.textContent = "Você deve ter pelo menos 18 anos.";
    msg.className = "mensagem erro";
  } else {
    msg.textContent = "Idade válida!";
    msg.className = "mensagem sucesso";
  }
});

form.addEventListener("submit", function (e) {
  const validador = new ValidadorIdade(input.value);
  if (!validador.maiorDeIdade()) {
    msg.textContent = "Você deve ter pelo menos 18 anos.";
    msg.className = "mensagem erro";
    e.preventDefault();
  }
});
