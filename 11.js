let lista1 = prompt('Ingresa una lista de números separados por coma');
let lista2 = prompt('Ingresa una lista de números separados por coma');
let verdadero = prompt(
  '¿True si quieres los elementos comunes o False si quieres los elementos no comunes? '
);
lista1 = lista1.split(',');
lista2 = lista2.split(',');

function trueOrNot() {
  if (verdadero === 'True') {
    console.log(lista1.filter((element) => lista2.includes(element)));
  } else {
    console.log(lista1.filter((element) => !lista2.includes(element)));
  }
}

trueOrNot();
