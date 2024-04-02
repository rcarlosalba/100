let numeral = prompt('Ingresa un número');

function isNar(num) {
  let nar = [];
  for (let n in num) {
    base = num[n];
    exponente = num.length;
    rta = Math.pow(base, exponente);
    nar.push(rta);
  }
  const total = nar.reduce((a, b) => a + b, 0);

  if (Number(total) === Number(num)) {
    console.log(`El ${numeral} es un número narcisista`);
  } else {
    console.log(`El ${numeral} No es un número narcisista`);
  }
}

isNar(numeral);
