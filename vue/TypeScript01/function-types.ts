function add(x:number, y: number, z?: number): number {
  if (typeof z == 'number') {
      return x + y + z
  }
  else {
      return x + y
  }
}

const add1 = (x:number, y: number, z?: number): number => {
    if (typeof z == 'number') {
        return x + y + z
    }
    else {
        return x + y
    }
}

add(1,2)
add(2,3, 4)

interface ISum{
    (x:number, y: number, z?: number): number
}

let add2: ISum = add1
