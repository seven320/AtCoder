package main

import (
  "fmt"
  "math"
)

func main()  {
  var N,M int
  fmt.Scan(&N,&M)
  a := []int{}
  b := []int{}
  d := []int{}
  c := []int{}
  tmp,tmp2 := 0,0
  for i :=0; i < N ; i++ {
    fmt.Scan(&tmp,&tmp2)
    a = append(a,tmp)
    b = append(b,tmp2)
  }
  for i := 0; i < M; i++ {
    fmt.Scan(&tmp,&tmp2)
    c = append(c,tmp)
    d = append(d,tmp2)
  }
  var ans [N]int
  for i := 0; i < N; i++ {
    tmp := 10**9
    for j := 0; j < M; j++ {
      tmp = math.Min(tmp,math.Abs((a[i]-c[j]))+math.Abs(b[i]-d[j]))
    }
    a[i] = tmp
  }
  for i := 0; i < N; i++ {
    fmt.Println(a[i])
  }
}
