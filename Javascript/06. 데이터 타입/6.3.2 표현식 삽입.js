// < 예제 06-12 > //
var first = 'Ung-mo'
var last = 'Lee'

// ES5: 문자열 연결
console.log('My name is ' + first + ' ' + last + '.')


// < 예제 06-13 > //
var first = 'Ung-mo'
var last = 'Lee'
const name = `${first} ${last}`

// ES6: 표현식 삽입
console.log(`My name is ${name}.`); // 반드시 템플릿 리터럴 내에서 사용해야 한다.
// console.log(`My name is ${first} ${last}.`);