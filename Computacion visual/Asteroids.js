function setup() {
  createCanvas(500, 500);
  player = new Player();
}

function draw() {
  background(0, 0, 0);
  player.update();
  player.draw();
}



class Player{
  constructor(){
    this.pos = createVector(width/2, height/2);
    this.vel = createVector(0, 0);
    this.acc = createVector(0, 0);
    this.color = color(255, 255, 255);
    this.angle = 0;
  }
  draw(){
    push();
    translate(this.pos.x, this.pos.y);
    rotate(this.angle);
    stroke(this.color);
    noFill();
    triangle(0, -10, -5, 10, 5, 10);
    pop();
  }
  update(){
    if (keyIsDown(LEFT_ARROW)) {
      this.angle -= 0.1;
    }else if (keyIsDown(RIGHT_ARROW)) {
      this.angle += 0.1;
    }
    if (keyIsDown(UP_ARROW)) {

  }
}