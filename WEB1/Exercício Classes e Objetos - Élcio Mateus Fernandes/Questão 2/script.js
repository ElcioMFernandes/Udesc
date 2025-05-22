class Nascimento {
  constructor(ano, mes, dia) {
    this.data = new Date(ano, mes - 1, dia);
    this.diasSemana = [
      "Domingo",
      "Segunda-feira",
      "Terça-feira",
      "Quarta-feira",
      "Quinta-feira",
      "Sexta-feira",
      "Sábado",
    ];
  }

  diaSemana() {
    return this.diasSemana[this.data.getDay()];
  }
}

document.getElementById("verificar").addEventListener("click", function () {
  const dataStr = document.getElementById("dataNasc").value;
  if (!dataStr) {
    document.getElementById("resultado").innerHTML =
      "Por favor, selecione uma data.";
    return;
  }
  const [ano, mes, dia] = dataStr.split("-").map(Number);

  const nascimento = new Nascimento(ano, mes, dia);

  document.getElementById(
    "resultado"
  ).innerHTML = `<p>Você nasceu em uma <strong>${nascimento.diaSemana()}</strong>.</p>`;
});
