const fs = require('fs')
const readline = require('readline')
const events = require('events')
input_file = "01input.txt"

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

async function main(ex, file){
    let max_sum, elf_sum, elf_sums
    max_sum = 0
    elf_sum = 0
    elf_sums = []
    await processLineByLine(file, line => {
        if (line != ""){
            elf_sum += parseInt(line)
        }
        else {
            elf_sums.push(elf_sum)
            elf_sum = 0
        }
    })
    if(ex === 1){
        console.log(Math.max(...elf_sums))
    }
    else{
        elf_sums.sort((a, b) => {
            return a - b
        })
        console.log(sum(elf_sums.slice(-3)))
    }
}

async function doit(){
    await main(1, input_file)
    await main(2, input_file)
}

doit()