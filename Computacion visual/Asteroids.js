function setup() {
  createCanvas(500, 500);
  player = new Player();
}

function draw() {
  // Classic cartesian order
  translate(width/2, height/2);
  scale(1, -1);

  background(0, 0, 0);
  player.update();
  player.draw();
}

// Only a bullet per press, not every frame.
// (keyIsDown inside draw checks every frame) 
function keyPressed(){
  if (keyCode === 32) {
    player.bullets.push(new Bullet(player.pos, player.angle));
  }
}

function wrap(pos, r = 0) {
  let halfW = width / 2;
  let halfH = height / 2;

  if (pos.x > halfW + r)  pos.x = -halfW - r;
  else if (pos.x < -halfW - r) pos.x = halfW + r;

  if (pos.y > halfH + r)  pos.y = -halfH - r;
  else if (pos.y < -halfH - r) pos.y = halfH + r;
}

class Player{
  constructor(){
    this.pos = createVector(0, 0);
    this.vel = createVector(0, 0);

    this.color = color(255, 255, 255);
    // The angle is the x axis
    this.angle = PI/2;
    this.bullets = [];
  }

  draw(){
    push();
    translate(this.pos.x, this.pos.y);
    rotate(this.angle);
    stroke(this.color);
    noFill();
    // The ship points to the angle
    triangle(15, 0, -10, -5, -10, 5);
    pop();

    for (let i = 0; i < this.bullets.length; i++){
      this.bullets[i].update();
      this.bullets[i].draw();
      if (this.bullets[i].outOfBounds()){
        this.bullets.splice(i, 1);
        
      }

    }
  }

  update(){
    if (keyIsDown(LEFT_ARROW)) {
      this.angle += 0.05;
    }else if (keyIsDown(RIGHT_ARROW)) {
      this.angle -= 0.05;
    }else if (keyIsDown(UP_ARROW)) {
      this.vel.add(p5.Vector.fromAngle(this.angle).mult(0.1));
    }
    this.pos.add(this.vel);
    this.vel.mult(0.98); // Friction
    wrap(this.pos, 15);
  }
}

class Bullet{

  constructor(pos, angle){
    // Angle = x axis
    this.angle = angle;
    // The origin is the position of the player when the bullet is created
    this.origin = createVector(pos.x, pos.y);
    // The position is relative to the origin, so it starts at the origin
    this.pos = createVector(15, 0);
    this.vel = createVector(7, 0);
  }

  draw(){
    push();
    translate(this.origin.x, this.origin.y);
    rotate(this.angle);
    fill(255);
    ellipse(this.pos.x, this.pos.y, 5, 5);
    pop();
  }

  update(){
    this.pos.add(this.vel);
    this.vel.mult(0.99999);
    
  }

  outOfBounds(){
    if (this.pos.x > width || this.pos.x < -width || this.pos.y > height || this.pos.y < -height){
      return true;
    }else{
      return false;
    }
  }
}


