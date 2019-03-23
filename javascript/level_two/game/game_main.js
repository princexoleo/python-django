//Restart game button
var restart = document.querySelector("#rbtn");

//Grabs all the square
var squares = document.querySelectorAll('td');
//clear all the square
function clearBoard(){
  for (var i = 0; i < squares.length; i++) {
    squares[i].textContent =" ";
  }
}

restart.addEventListener('click',clearBoard);
//Check the square
//
// var cellOne = document.querySelector('#one');
//
// cellOne.addEventListener('click', function(){
//   if (cellOne.textContent === '') {
//     cellOne.textContent = 'X';
//   }
//   else if (cellOne.textContent ==='X') {
//     cellOne.textContent='0';
//   } else {
//     cellOne.textContent='';
//   }
// })
function changeMarker(){
  if (this.textContent ==='') {
    this.textContent ='X';
  }else if (this.textContent === 'X') {
    this.textContent ='O';
  }else{
    this.textContent ='';
  }
}

for (var i = 0; i < squares.length; i++) {
  squares[i].addEventListener('click',changeMarker);
}

// For loops to add event listener to all the square
