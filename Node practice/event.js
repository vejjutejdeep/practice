const EventEmitter = require('events')

const emitter = new EventEmitter()

emitter.addListener('print', (arg) => {

    console.log('print the statement', arg)

})

emitter.addListener('logging',(args) => {

    console.log(`the data sent in the message is: ${args.data}`)

})

emitter.emit('print', {id: 1, url: 'url'})

emitter.emit('logging', {data: 'We are leaning nodejs'})