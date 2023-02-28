const program = require('commander');
const chalk = require('chalk');

program
  .version('0.0.2')
  .description('Working with Optional arguments')
  .name('cli');

// optional argument
// non mandatory
// --

program
  .option('-f,--firstname <value>', 'Specify Firstname', 'Matthew')
  .option('-l,--lastname <value>', 'Specify Lastname', 'Surname')
  .action(function (value) {
    console.log('Hello ', chalk.red.bgWhite.bold(value.firstname));
    console.log('Your lastname is ', chalk.yellow(value.lastname));
    console.log(chalk.magenta('Required'));
  });

program.parse(process.argv);
