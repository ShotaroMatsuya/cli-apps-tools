const program = require('commander')
const chalk = require('chalk')
const figlet = require('figlet')
var ciphertext = require('./ciphertext.js')

// cypha rot13 text
// cypha rotate text --number 13
// cypha caesarshift text --shift 12
// cypha reverse text
// cypha leet text

program.version('0.0.1').description('Cypha - simple cipherig CLI').name('cypha')


program.command('rot13 <text>').description('Rotate 13 A Text').action(function(text){
  console.log("Original Text::", chalk.blue.bold(text))
  var result = ciphertext.rot13(text)
  console.log('Rotated Text::', chalk.blue.bold(result))
})

program.command('rotate <text>').description('Rotate Text By A number').alias('rt').option('-n,--number <value>', 'Number to Rotate By').action(function(text, value){
  console.log("Original Text::", chalk.blue.bold(text))
  console.log("Rotating Number", value.number)
  var result = ciphertext.rot(text, Number(value.number))
  console.log('Rotated Text::', chalk.blue.bold(result))
})

program.command('caesarshift <text>').description('Caesarshift Text By A number').alias('cs').option('-s,--shift <value>', 'Number to Shift By').action(function(text, value){
  console.log("Original Text::", chalk.blue.bold(text))
  console.log("Shift Number", value.shift)
  var result = ciphertext.caesar(text, Number(value.shift))
  console.log('Rotated Text::', chalk.blue.bold(result))
})

program.command('reverse <text>').alias('r').description('Reverse A Text or String').action(function(text){
  console.log("Original Text::", chalk.blue.bold(text))
  var result = ciphertext.reverseString(text)
  console.log("Reversed Text::", chalk.blue.bold(result))
})

program.command('leet <text>').alias('l').description('Leet Convert A Text or String').action(function(text){
  console.log("Original Text::", chalk.blue.bold(text))
  var result = ciphertext.speakLeet(text)
  console.log("Leet Text::", chalk.blue.bold(result))
})


program.command('info').description('Info About CLI').action(function (argument){
  console.log(figlet.textSync('Cypha', {
    font: 'Standard',
    horizontalLayout: 'default',
    verticalLayout: 'default',
  }))
  console.log(chalk.cyan.bold("Shotaro matsya@h923.itsceom.not"))
})

program.parse(process.argv)
