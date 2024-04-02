numeral = Number(prompt('Ingresa un número: '));

const resultado = 1;

function factorial(num) {
  if (num === 0) {
    return 1;
  }
  return num * factorial(num - 1);
}

console.log(`El factorial de ${numeral} es ${factorial(numeral)}`);
