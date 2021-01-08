function convertToRoman(num) {


  let myNum = num.toString();
  //var count = 1;
  var result = "";
  var guide = [["I","V","X"], ["X","L","C"],["C","D","M"]];


  var digit = num.toString.length;

  for(var i = '0'; i < digit ; i++){
    if ( myNum.charAt(i) == '1') {result.concat(guide[i][1]);}
    else if ( myNum.charAt(i) == '2') {result.concat(guide[i][0] + guide[i][0]);}
    else if ( myNum.charAt(i) == '3') {result.concat(guide[i][0] + guide[i][0] + guide[i][0]);}
    else if ( myNum.charAt(i) == '4') {result.concat(guide[i][0] + guide[i][1]);}
    else if ( myNum.charAt(i) == '5') {result.concat(guide[i][1]);}
    else if ( myNum.charAt(i) == '6') {result.concat(guide[i][1] + guide[i][0]);}
    else if ( myNum.charAt(i) == '7') {result.concat(guide[i][1] + guide[i][0] + guide[i][0]);}
    else if ( myNum.charAt(i) == '8') {result.concat(guide[i][1] + guide[i][0] + guide[i][0] + guide[i][0]);}
    else if ( myNum.charAt(i) == '9') {result.concat(guide[i][0] + guide[i][2]);}

    console.log(result);
  }


 return result;
}

convertToRoman(36);
