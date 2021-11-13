function echo<G>(arg: G): G {
    return arg
}

const result = echo('Jcx')

function swap<T, U>(tuple: [T, U]): [U ,T]{
    return [tuple[1], tuple[0]]
}

const result2 = swap(['jcx', 123])
console.log(result2)

function echoWithArr<T>(arg: T[]): T[] {
    console.log(arg.length)
    return arg
}
const arrs = echoWithArr([1, 2, 3])

// 约束泛型
interface IWithLength {
    length: number
}

function echoWithLength<T extends IWithLength>(arg: T): T {
    console.log(arg.length)
    return arg
}
const str = echoWithLength('jcx')
const obj = echoWithLength({length: 10, name: 'Jcx'})
const arr2 = echoWithLength([1, 2, 3])

// 泛型在类中的使用
class Queue<T> {
    private data: any[] = [];
    push(item: T) {
        return this.data.push(item)
    }
    pop(){
        return this.data.shift()
    }
}

const queue = new Queue<number>()
queue.push(1)
console.log(queue.pop().toFixed())

interface KeyPair<T, U> {
    key: T
    value: U
}
let kp1: KeyPair<number, string> = {
    key: 1,
    value: 'jcx'
}

let kp2: KeyPair<string, number> = {
    key: 'jcx',
    value: 1
}

let arr: number[] = [1, 2, 3]
let arrTwo: Array<number> = [1 ,2 ,3]










