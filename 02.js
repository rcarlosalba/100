const lados = Number(prompt('Cuántos lados tiene la figura? '));
const longitud = Number(prompt('Cuánto mide cada lado? '));
const apotema = Number(prompt('Cuánto mide el apotema? '));
let perimetro = lados * longitud;
let area = ((perimetro * apotema) / 2).toFixed(2);

if (lados == 3) {
  console.log(
    `Es un triángulo con un perímetro de ${perimetro} y un área de ${area}`
  );
} else if (lados == 4) {
  console.log(
    `Es un cuadrado con un perímetro de ${perimetro} y un área de ${area}`
  );
} else if (lados == 5) {
  console.log(
    `Es un pentágono con un perímetro de ${perimetro} y un área de ${area}`
  );
} else {
  console.log(
    `Es un polígono con ${lados} lados, un perímetro de ${perimetro} y un área de ${area}`
  );
}
