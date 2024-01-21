var url = "http://localhost/logger";

async function log(msg) {

    console.log(msg);

}

async function err(msg) {

    console.log("this is the second function exproted " + msg);

}

module.exports = {log, err};