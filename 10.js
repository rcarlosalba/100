function oneToOnehundredFor() {
  for (let i = 1; i <= 100; i++) {
    console.log(i);
  }
}

function oneToOnehundredWhile() {
  let i = 1;
  while (i <= 100) {
    console.log(i);
    i++;
  }
}

function oneToOnehundredDoWhile() {
  let i = 1;
  do {
    console.log(i);
    i++;
  } while (i <= 100);
}

function oneToOnehundredForOf() {
  for (let i of Array.from({ length: 100 }, (_, i) => i + 1)) {
    console.log(i);
  }
}
