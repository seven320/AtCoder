package main

import "fmt"

func main()  {
  var A int
  var B int
  fmt.Scan(&A,&B)
  ans := A+B
  if(ans >= 24){
    ans -= 24
  }
  fmt.Println(ans)
}
