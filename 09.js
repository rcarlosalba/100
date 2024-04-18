let dias = Number(prompt('Ingrese la cantidad de días: '));
let horas = Number(prompt('Ingrese la cantidad de horas: '));
let minutos = Number(prompt('Ingrese la cantidad de minutos: '));
let segundos = Number(prompt('Ingrese la cantidad de segundos: '));

function convertirMilisegundo(d, h, m, s) {
  let ms = 0;
  ms += s * 1000;
  ms += m * 60000;
  ms += h * 3600000;
  ms += d * 86400000;
  console.log(`La cantidad de milisegundos es: ${ms}`);
}

convertirMilisegundo(dias, horas, minutos, segundos);
