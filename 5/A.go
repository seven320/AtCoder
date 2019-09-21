package main

import (
  "fmt"
  "math"
  // "os"
)

func main(){
  var a,b float64
  fmt.Scan(&a,&b)
  fmt.Println(math.Trunc(b/a))
 }
