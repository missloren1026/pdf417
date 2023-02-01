const pdf417 = require('pdf417')
const fs = require("fs")


function logArr(arr) {
    let l = ''
    for (let x of arr)
        l += x + ','
    console.log(l)
}

function aamvaToCodeWords(code) {
    let body = code.split('\rZOZOA')[0].slice(4)
    let optional = 'ZOZOA' + code.split('\rZOZOA')[1]
    let cw_body = pdf417.PDF417.getCompaction(900, body, true)
    cw_body.splice(1, 0, 881)
    cw_body.push(358)
    let cw_optional = pdf417.PDF417.getCompaction(900, optional, true)
    cw_optional = cw_optional.slice(1)
    if (cw_optional[cw_optional.length - 1] == 359) {
        cw_optional[cw_optional.length - 2] = cw_optional[cw_optional.length - 2] + 1
    } else if (cw_optional[cw_optional.length - 1] == 851) {
        cw_optional[cw_optional.length - 1] = 881
    }
    let cw = []
    cw = cw.concat([901, 64, 10, 30])
    cw = cw.concat(cw_body)
    // cw = cw.concat(cw_optional)
    return cw
}

// I/O: Read from stdin
let aamva = fs.readFileSync(0, "utf-8")
while (aamva[aamva.length - 1] == '\n') {
    aamva = aamva.slice(0, aamva.length - 1)
}
let cw = aamvaToCodeWords(aamva)

// I/O: Write to stdout
logArr(cw)
