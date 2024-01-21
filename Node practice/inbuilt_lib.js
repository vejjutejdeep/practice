const path  = require('path');

const os = require('os');

const fs = require('fs');

const files = fs.readdir('./', function(err,files){
    if(err) console.log(`Error ${errr}`)
    else console.log(`Result ${files}`)
});

// console.log(files)


// var obje = path.parse(__filename);

// var freememory = os.freemem()

// var platform = os.platform()

// console.log(`Free memory: ${freememory}`)

// console.log(`Platform: ${platform}`)

// console.log(obje);