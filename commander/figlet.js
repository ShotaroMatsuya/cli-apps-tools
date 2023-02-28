var figlet = require('figlet');

figlet('Building CLI!!', function (err, data) {
  if (err) {
    console.log('Something went wrong...');
    console.dir(err);
    return;
  }
  console.log(data);
});

figlet.text(
  'Building CLI',
  {
    font: 'Ghost',
    horizontalLayout: 'default',
    verticalLayout: 'default',
  },
  function (err, data) {
    if (err) {
      console.log('Something went wrong...');
      console.dir(err);
      return;
    }
    console.log(data);
  }
);

// Text Sync
console.log(
  figlet.textSync('Boo!', {
    font: 'Ghost',
    horizontalLayout: 'default',
    verticalLayout: 'default',
  })
);
