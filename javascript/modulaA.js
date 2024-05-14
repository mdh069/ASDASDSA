const fs = require("fs")

fs.readFile(`${__dirname}/moduloB.js`,"utf-8", (err, data) => {
    console.log(data)
})