class Calc {
  constructor(valor1, valor2) {
    this.valor1 = valor1;
    this.valor2 = valor2;
  }

  menor() {
    return Math.min(this.valor1, this.valor2);
  }

  maior() {
    return Math.max(this.valor1, this.valor2);
  }

  quadradoDoMenor() {
    return Math.pow(this.menor(), 2);
  }

  raizDoMaior() {
    return Math.sqrt(this.maior());
  }
}

document.getElementById("calcular").addEventListener("click", function () {
  const v1 = parseFloat(document.getElementById("valor1").value);
  const v2 = parseFloat(document.getElementById("valor2").value);

  if (isNaN(v1) || isNaN(v2)) {
    document.getElementById("resultado").innerHTML =
      "Por favor, preencha ambos os valores.";
    return;
  }

  const calc = new Calc(v1, v2);

  document.getElementById("resultado").innerHTML =
    `<p>Quadrado do menor (${calc.menor()}): ${calc.quadradoDoMenor()}</p>` +
    `<p>Raiz quadrada do maior (${calc.maior()}): ${calc.raizDoMaior()}</p>`;
});
