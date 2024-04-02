let oracion = prompt('Ingrese una oración: ');
oracion = oracion.split(' ');

function makeTitle(text) {
  let nt = '';
  for (let t of text) {
    t = t[0].toUpperCase() + t.slice(1) + ' ';
    nt += `${t}`;
  }
  console.log(nt);
}

makeTitle(oracion);
