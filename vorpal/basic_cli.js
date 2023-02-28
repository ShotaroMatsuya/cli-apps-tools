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
// Non Interactive
// vorpal.parse(process.argv);

// Interactive
vorpal.delimiter('cli$').show();
