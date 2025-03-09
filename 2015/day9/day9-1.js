import input from './input.txt'

const data = input.split('\n')
var distances = []

data.forEach(line => {
    if(line == '') {
        return
    }

    line = line.split(' ')
    distances.push([line[0], line[2], Math.floor(line[4])])
})

console.log(distances)
