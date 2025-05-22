class Circulo {
  constructor(raio) {
    this.raio = raio;
  }
  area() {
    return Math.PI * Math.pow(this.raio, 2);
  }
}

document.getElementById("calcular").addEventListener("click", function () {
  const raio = parseFloat(document.getElementById("raio").value);
  const resultado = document.getElementById("resultado");

  if (isNaN(raio) || raio <= 0) {
    resultado.textContent =
      "Por favor, informe um raio válido (maior que zero).";
    resultado.className = "erro";
    return;
  }

  const circulo = new Circulo(raio);
  resultado.textContent = `Área do círculo de raio ${raio}: ${circulo
    .area()
    .toFixed(2)}`;
  resultado.className = "sucesso";
});
