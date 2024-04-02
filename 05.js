let str1 = prompt('Ingresa un texto: ');
let str2 = prompt('Ingresa otro texto: ');

const diff1 = new Set([...str1]).difference(new Set([...str2]));
const diff2 = new Set([...str2]).difference(new Set([...str1]));

rta1 = [...diff1].join(',');
rta2 = [...diff2].join(',');

console.log(
  `Caracteres en el primer texto que no están en el segundo: ${rta1}`
);
console.log(
  `Caracteres en el segundo texto que no están en el primero: ${rta2}`
);
