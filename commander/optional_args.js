const program = require('commander');

program
  .version('0.0.2')
  .description('Working with Optional arguments')
  .name('cli');

// register short form of command alias
program.command('say').description('Say Something').alias('s');

// optional argument
// non mandatory
// --

program
  .option('-f,--firstname <value>', 'Specify Firstname', 'Matthew')
  .option('-l,--lastname <value>', 'Specify Lastname', 'Surname')
  .requiredOption('--status', 'Specify Status')
  .action(function (value) {
    console.log('Hello ', value.firstname);
    console.log('Your lastname is ', value.lastname);
    console.log('Required');
  });

program.parse(process.argv);
