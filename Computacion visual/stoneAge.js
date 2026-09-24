const N = 20;
function setup() {
  createCanvas(680, 480, WEBGL);

}

function draw() {
  background(0);
  orbitControl();

  for(let i = 0; i < N; i++){
    rotateY(TWO_PI/N)
    push()
    translate(0, 0, 400)
    box(40, 100, 40)
    pop()


    push()
    rotateY(PI/N)
    translate(0,-70,400)
    box(130, 40, 40)
    pop()
  }
}


// const N = 20;

// function setup() {
//   createCanvas(680, 480, WEBGL);
// }

// function draw() {
//   background(0);
//   orbitControl();
  
//   for(let i=0; i<N; i++){
//     rotateY(TWO_PI/N);
    
//     push();
//     translate(0, 0, 400);
//     box(40, 100, 40);
//     pop();
    
//     push();
//     rotateY(PI/N);
//     translate(0, -70, 400);
//     box(130, 40, 40);
//     pop();
//   }
// }