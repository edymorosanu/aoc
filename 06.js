const fs = require('fs')
const readline = require('readline')
const events = require('events')
const input_file = "06input.txt"
const data = fs.readFileSync(input_file, {encoding:'utf8', flag:'r'});

function main(pck_len, file) {
    const str = data.split("\n")[0]
    const result = str
        .split("")
        .reduce((a, b, i, arr) => {
            if (a.length === pck_len) {
                if (new Set(a).size === pck_len) {
                    arr.splice(0)
                    return a
                }
                else {
                    a.shift()
                }
            }
            a.push(b)
            return a
        }, [])
        .join("")
    console.log(str.indexOf(result)+pck_len)

}

async function doit() {
    await main(4, input_file)
    await main(14, input_file)
}

doit()
