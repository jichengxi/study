package main

import "fmt"

type Person struct {
	Name string
}

func (p Person) speak() {
	fmt.Println(p.Name, "是一goodman")
}

func (a Person) test() {
	a.Name = "jack"
	fmt.Println("test() name=", a.Name)
}

func main() {
	var p Person
	p.Name = "Tom"
	p.test()
	fmt.Println("main() name=", p.Name)
	p.speak()

}
