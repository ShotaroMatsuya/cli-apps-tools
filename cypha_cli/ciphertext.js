function rot13(c) {
    return c.replace(/([a-m])|([n-z])/ig, function($0,$1,$2) {
        return String.fromCharCode($1 ? $1.charCodeAt(0) + 13 : $2 ? $2.charCodeAt(0) - 13 : 0) || $0;
    });
}

function rot(text, shift) {
  return text.toUpperCase().replace(/[^A-Z]/g,'').replace(/./g, function(a) {
    return String.fromCharCode(65+(a.charCodeAt(0)-65+shift)%26).toLowerCase();
  });
}


function caesar(text, shift) {
  return text.toUpperCase().replace(/[^A-Z]/g,'').replace(/./g, function(a) {
    return String.fromCharCode(65+(a.charCodeAt(0)-65+shift)%26).toLowerCase();
  });
}

function reverseString(str) {
    return str.split("").reverse().join("");
}

function speakLeet(str) {
	var leetCode = {A: "@",B: '8',C: '(',D: '|)',E: '3',F: 'ph',G: 'g',H: '#',I: 'l',J: '_|',K: '|<',L: '1', M: '|\'|\'|',N: '/|/',O: '0', P: '|D',Q: '(,)',R: '|2',S: '5',T: '+',U: '|_|',V: '|/',W: '|/|/',X: '><',Y: 'j',Z: '2'
	}
	var translatedStr = "";

	for (i = 0; i < str.length; i++) {
		translatedStr += leetCode[str.charAt(i).toUpperCase()];
		}
	return translatedStr;
}

// Package
class CipherText{
    constructor(text){
        this.text = text;
    }
    rot13() {
        return this.text.replace(/([a-m])|([n-z])/ig, function($0,$1,$2) {
            return String.fromCharCode($1 ? $1.charCodeAt(0) + 13 : $2 ? $2.charCodeAt(0) - 13 : 0) || $0;
        });
    }

    reverseString() {
        return this.text.split("").reverse().join("");
    }

    caesar (shift=13) {
      return this.text.toUpperCase().replace(/[^A-Z]/g,'').replace(/./g, function(a) {
        return String.fromCharCode(65+(a.charCodeAt(0)-65+shift)%26).toLowerCase();
      });
    }

    speakLeet() {
        var leetCode = {A: "@",B: '8',C: '(',D: '|)',E: '3',F: 'ph',G: 'g',H: '#',I: 'l',J: '_|',K: '|<',L: '1', M: '|\'|\'|',N: '/|/',O: '0', P: '|D',Q: '(,)',R: '|2',S: '5',T: '+',U: '|_|',V: '|/',W: '|/|/',X: '><',Y: 'j',Z: '2'
        }
        var translatedStr = "";

        for (var i = 0; i < this.text.length; i++) {
            translatedStr += leetCode[this.text.charAt(i).toUpperCase()];
            }
        return translatedStr;
    }
}
module.exports = {
   rot13,
   rot,
   caesar,
   reverseString,
   speakLeet,
   CipherText
}