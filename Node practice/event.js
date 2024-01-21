const EventEmitter = require('events')

const emitter = new EventEmitter()

emitter.addListener('print', function(){

    console.log('print the statement')

})

emitter.emit('print')