package main

import "fmt"

// 继承

type Student struct {
	Name string
	Age int
	Score int
}

func (stu Student) ShowInfo()  {
	fmt.Println("学生名=", stu.Name, "年龄=", stu.Age, "成绩=", stu.Score)
}

func (stu *Student) SetScore(score int)  {
	stu.Score = score
}

func (stu *Student) getSum(n1 int, n2 int) int {
	return n1 + n2
}

type Pupil struct {
	Student
}

func (p *Pupil) testing() {
	fmt.Println("小学生正在考试中...")
}

type Graduate struct {
	Student
}

func (p *Graduate) testing() {
	fmt.Println("大学生正在考试中...")
}

func main() {
	pupil := &Pupil{}
	pupil.Student.Name = "tom"
	pupil.Student.Age = 8
	pupil.testing()
	pupil.Student.SetScore(70)
	pupil.Student.ShowInfo()
	fmt.Println(pupil.getSum(1, 2))

	graduate := &Graduate{}
	graduate.Student.Name = "tim"
	graduate.Student.Age = 18
	graduate.testing()
	graduate.Student.SetScore(80)
	graduate.Student.ShowInfo()
	fmt.Println(pupil.getSum(10, 20))
}
