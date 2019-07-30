// TEMP:
package main

import (
  "fmt"
  // "os"
)

var S string

func main(){
  // var S string
  fmt.Scan(&S)
  var ans = true
  for i := 0; i < 3; i++ {
    if S[i] == S[i+1] {
      ans = false
      break
    }
  }

  if ans {
    fmt.Println("Good")
  }else{
    fmt.Println("Bad")
  }
}
