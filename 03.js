const palabra = prompt('Introduce la palabra: ');

function volteando(palabra) {
  let resultado = [];
  for (let i = palabra.length - 1; i >= 0; i--) {
    resultado += palabra[i];
  }
  return resultado;
}

console.log(volteando(palabra));
