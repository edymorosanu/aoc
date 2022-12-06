const fs = require('fs')
const readline = require('readline')
const events = require('events')
const input_file = "03input.txt"
const prio = {}
// Using for loop for (a-z):
for (let i = 1; i <= 26; i++) {
    prio[String.fromCharCode(i+96)] = i
    prio[String.fromCharCode(i+64)] = i+26
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

async function one(file){
    let sum = 0
    await processLineByLine(file, line => {
        let l = line.length
        let half = l / 2
        let str1 = line.substr(0, half)
        let str2 = line.substr(half, half)
        let intersect = new Set(str1.split("").filter(function(value){
            return str2.split("").includes(value)
        }))
        for (i of intersect){
            sum += prio[i]
        }
    })
    console.log(sum)
}

async function two(file){
    let sum = 0
    let group = []
    let line_nr = 0
    let intersect
    await processLineByLine(file, line => {
        group.push(line)
        if (line_nr % 3 === 2){
            intersect = new Set(group[0].split("").filter(function(value){
                return group[1].split("").includes(value) && group[2].split("").includes(value)
            }))
            for (let i of intersect){
                sum += prio[i]
            }
            group = []
        }
        line_nr++
    })
    console.log(sum)
}

async function doit(){
    await one(input_file)
    await two(input_file)
}

doit()