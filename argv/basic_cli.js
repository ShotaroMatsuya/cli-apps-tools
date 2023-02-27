console.log(process.argv);

const command = process.argv[2];

if (command == 'greet') {
  console.log('Good Morning', process.argv[3]);
} else if (command == 'version') {
  console.log('CLI version 0.01');
}
