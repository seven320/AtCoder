package main

import (
  "fmt"
  "os"
  "bufio"
)



func main(){
  s := make([]string, 4)
  for i := 0; i < 4; i++ {
    s[i] = nextLine()
  }
  for i := 3; i >= 0; i--{
    for j := len(s[i])-1; j >= 0; j--{
      fmt.Printf("%c",s[i][j])
    }
    fmt.Printf("\n")
  }

 }

 var sc = bufio.NewScanner(os.Stdin)

 func nextLine() string {
     sc.Scan()
     return sc.Text()
 }
