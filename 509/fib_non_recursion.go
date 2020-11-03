package main

import "fmt"



func fib(N int) int {
    if N == 0 || N== 1 {
        return N
    }

    pre := 0
    cur := 1

    for i:=2; i<N; i++ {
        sum := pre + cur
        pre = cur
        cur = sum
    }

    return pre + cur
}

func main() {
    fmt.Println(fib(3))
}
