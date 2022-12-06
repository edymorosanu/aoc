const fs = require('fs')
const readline = require('readline')
const events = require('events')
input_file = "01input.txt"
const data = fs.readFileSync(input_file, {encoding:'utf8', flag:'r'});

function main(ex, file){
    totals = data
        .split("\n\n")
        .map(v => v
            .split("\n")
            .filter(line => line !== "")
            .reduce((accum, value) => accum + parseInt(value), 0)
        )
        .sort((a,b) => a - b)
        .reverse()
    if (ex === 1){
        console.log(totals[0])
    }
    else{
        console.log(totals.slice(0,3).reduce((accum, value) => accum + parseInt(value), 0))
    }
}

async function doit(){
    await main(1, input_file)
    await main(2, input_file)
}

doit()