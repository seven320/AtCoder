package main

import (
  "fmt"
  "sort"
  "os"
  "bufio"
  "strconv" //str to int
)

func main(){
  var N int
  fmt.Scan(&N)
  T := make([]int, N)
  for i := 0; i < N; i++ {
    s := nextLine()
    T[i],_ = strconv.Atoi(s)
  }
  sort.Sort(sort.IntSlice(T))
  fmt.Println(T[0])
 }


 var sc = bufio.NewScanner(os.Stdin)

 func nextLine() string {
     sc.Scan()
     return sc.Text()
 }
xt() 
}
