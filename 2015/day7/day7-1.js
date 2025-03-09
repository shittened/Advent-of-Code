import input from './input.txt'

var data = input.split('\n')
var wires = {}
var iteration = 0

while(data.length > 0) {
    data.forEach((line, index) => {
        if(line == '') {
            return
        }
    
        line = line.split(' ')
    
        if(line[0] == 'NOT') {
            if(line[1] in wires) {
                wires[line[3]] = ~wires[line[0]]
                data.splice(index, 1)
                console.log('a', line, index)
            }
        }
        if(!isNaN(line[0])) {
            if(line[1] == '->') {
                wires[line[2]] = Math.floor(line[0])
                data.splice(index, 1)
                console.log('b', line, index, data.length)
            }
        }
        if(line[0] in wires && line[2] in wires) {
            switch(line[1]) {
                case 'AND':
                    wires[line[4]] = line[0] & line[2]
                case 'OR':
                    wires[line[4]] = line[0] | line[2]
                case 'RSHIFT':
                    wires[line[4]] = line[0] >> Math.floor(line[2])
                case 'LSHIFT':
                    wires[line[4]] = line[0] << Math.floor(line[2])
            }
            data.splice(index, 1)
        }
    })
    iteration += 1
}

console.log(wires)
