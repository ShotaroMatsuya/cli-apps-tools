const program = require('commander');

program.version('0.0.3').description('Working with Arguments').name('cli');

program
  .arguments('<number1>')
  .arguments('<number2>')
  .action(function (number1, number2) {
    console.log('FirstNumber ', number1);
    console.log('SecondNumber ', number2);
    var results = parseInt(number1) + parseInt(number2);
    console.log(results);
  });

program.parse(process.argv);
