let decimal = Number(prompt('Introduce un número decimal: '));

function binario(decimal) {
  let resultado = [];
  while (decimal > 0) {
    resultado.unshift(decimal % 2);
    decimal = Math.floor(decimal / 2);
  }
  return resultado.join('');
}

console.log(binario(decimal));
