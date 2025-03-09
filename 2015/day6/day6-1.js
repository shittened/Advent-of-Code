import input from './input.txt'

const data = input.split('\n')
var map = []

for(let i = 0; i < 1000; i++) {
    for(let j = 0; j < 1000; j++) {
        map.push([i, j, 0])
    }
}

data.forEach(line => {
    if(line == '') {
        return
    }

    line = line.split(' ')

    const turn = line.indexOf('turn')
    if(turn > -1) {
        line.splice(turn, 1)    
    }

    const start = line[1].split(',')
    const end = line[3].split(',')
    const start_x = Math.floor(start[0])
    const start_y = Math.floor(start[1])
    const end_x = Math.floor(end[0])
    const end_y = Math.floor(end[1])

    map.forEach(coord => {
        if(start_x > coord[0]) {
            return
        }
        if(end_x < coord[0]) {
            return        
        }
        if(start_y > coord[1]) {
            return
        }
        if(end_y < coord[1]) {
            return
        }

        switch(line[0]) {
            case 'on':
                coord[2] = 1       
            case 'off':
                coord[2] = 0
            case 'toggle':
                if(coord[2] == 0) {
                    coord[2] = 1
                }
                else {
                    coord[2] = 0
                }
        }
    })
})

var total_on = 0
map.forEach(coord => {
    if(coord[2] == 1){
        total_on += 1
    }
})

console.log(total_on)
