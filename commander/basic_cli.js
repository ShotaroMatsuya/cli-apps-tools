const program = require('commander');

program
  .version('0.0.1')
  .description('Simple CLI with Commander.js')
  .name('cli');

// Commands
program
  .command('register <name>')
  .description('Register User')
  .option('--upper,-u', 'Uppercase')
  .action(function (name) {
    console.log('Registering ', name.toUpperCase());
  });

program.parse(process.argv);
