const fs = require('fs')
const readline = require('readline')
const events = require('events')
input_file = "02input.txt"
score1 = {
    "A X": 4,
    "B X": 1,
    "C X": 7,
    "A Y": 8,
    "B Y": 5,
    "C Y": 2,
    "A Z": 3,
    "B Z": 9,
    "C Z": 6
}
score2 = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7
}

async function processLineByLine(f, callback){
    try {
      const rl = readline.createInterface({
        input: fs.createReadStream(f),
        crlfDelay: Infinity
      })
      rl.on('line', callback)
      await events.once(rl, 'close')
    }
    catch (err) {
      console.error(err)
    }
}

function sum(arr){
    return arr.reduce((accumulator, value) => {
            return accumulator + value
            }, 0)
}

async function main(score, file){
    let total_score = 0
    await processLineByLine(file, line => {
        total_score += score[line]
    })
    console.log(total_score)
}

async function doit(){
    await main(score1, input_file)
    await main(score2, input_file)
}

doit()
