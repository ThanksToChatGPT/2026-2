let gravedad = createVector(0, 0.2);

function setup() {
  createCanvas(400, 400);
  myRocket = new Rocket();
}

function draw() {
  background(0, 0, 0);
  myRocket.update();
  myRocket.draw();
}


class Rocket{
  constructor( ){
    this.pos = createVector(random(width), 380)
    this.vel = createVector(0, -random(1, 5));

    this.acc = createVector(0, 0);
    this.color = color(random(255), random(255), random(255));
    this.exploded = false;  
  }

  update(){
    this.acc.add(gravedad);
    this.vel.add(this.acc);
    this.pos.add(this.vel);
    this.acc.mult(0);
  }

  draw(){
    fill(this.color);
    ellipse(this.pos.x, this.pos.y, 10, 10);

    }

  
}
