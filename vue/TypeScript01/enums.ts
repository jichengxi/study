enum Direction {
    Up,
    Down,
    Left,
    Right,
}

console.log(Direction.Up)
console.log(Direction[0])

// 常量枚举
const enum Direction2 {
    Up = 'UP',
    Down = 'DOWN',
    Left = 'LEFT',
    Right = 'RIGHT',
}
const value = 'UP'
if (value === Direction2.Up) {
    console.log('go up!')
}

