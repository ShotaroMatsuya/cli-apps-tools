// Arguments Vector[Array/list]
console.log(process.argv);

// Anatomy
// cli command/option value

const runtime = process.argv[0];
const cli = process.argv[1];
const command = process.argv[2];
const values = process.argv[3];

console.log('Runtime/Interpreter[0]::', runtime);
console.log('CLI program[1]::', cli);
console.log('Command/option[2]::', command);
console.log('Values[3]::', values);
