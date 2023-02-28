// Interactive CLI
const vorpal = require('vorpal')();

// command [option_args] <require_args/positional_args>

// Command
vorpal
  .command('login [username]')
  .description('Login To View')
  .alias('l')
  .action(function (args, callback) {
    this.log('Hello and welcome', args.username);
    callback();
  });

// Options
vorpal
  .command('convert <value>')
  .description('convert Value to Upper/Lowercase')
  .option('-u,--upper', 'Uppercase')
  .option('-l,--lower', 'Lowercase')
  .action(function (args, callback) {
    // this.log(args.options);
    if (args.options.upper) this.log(args.value.toUpperCase());
    if (args.options.lower) this.log(args.value.toLowerCase());
    callback();
  });

// Interactive
vorpal.delimiter('cli$').show();
