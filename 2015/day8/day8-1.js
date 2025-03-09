import input from './input.txt'

const data = input.split('\n')
var chars_len = 0
var mem_len = 0

data.forEach(line => {
    if(line == '') {
        return
    }

    chars_len += line.length

    var mem_line = line.substring(1, line.length -1)
    var mem_line = mem_line.replace('\\\\', 'a')
    var mem_line = mem_line.replace('\\\"', 'a')
    var hex = mem_line.indexOf('\\x')
    if(hex != -1) {
        mem_line = mem_line.substring(0, hex)
        mem_line += 'a'
    }
    mem_len += mem_line.length
})

console.log(chars_len - mem_len)
