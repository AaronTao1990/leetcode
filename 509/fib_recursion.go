package main

import "fmt"

func fib(N int) int {
    if N == 0 || N== 1 {
        return N
    }

    return fib(N-1) + fib(N-2)
}

func main() {
    fmt.Println(fib(3))
}
