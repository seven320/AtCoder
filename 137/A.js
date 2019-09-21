function main(input) {
    var num = input.split(" ");
    let ans = -1;
    let a = num[0]
    let b = num[1]
    ans = a+b
    if (ans < a-b){
        ans = a-b
    }
    if (ans < a*b){
        ans = a*b
    }
    console.log(ans);
  }


main(require('fs').readFileSync('/dev/stdin', 'utf8'))
