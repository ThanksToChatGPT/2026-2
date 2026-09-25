let player;
let asteroids = [];
let score = 0;
let bullets = [];
let saucer;
let lives = 3;


function setup() {
  createCanvas(500, 500);
  player = new Player();

  // Initial wave of asteroids
  for (let i = 0; i < 5; i++) {
    asteroids.push(new Asteroid());
  }

}

function draw() {
  background(0, 0, 0);

  // HUD: Draw score in standard screen coordinates
  fill(255);
  noStroke();
  textSize(16);
  text("Score: " + floor(score), 15, 25);

  // HUD: Draw lives as hearts in the top-left corner
  for (let i = 0; i < lives; i++) {
    drawHeart(22 + i * 22, 45, 12);
  }

  // Classic cartesian order
  push();
  translate(width/2, height/2);
  scale(1, -1);

  player.update();
  player.draw();

  // Update, draw and handle collisions for asteroids
  for (let i = asteroids.length - 1; i >= 0; i--) {
    asteroids[i].update();
    asteroids[i].draw();

    // Check collision with player ship
    if (asteroids[i].hits(player.pos, 10)) {
      // Crash: reset player to origin
      player.pos = createVector(0, 0);
      player.angle = PI/2;
      player.vel = createVector(0, 0);
      if (lives > 0) lives--;
    }

    // Check collision with bullets
    for (let j = 0; j < bullets.length; j++) {
      if (asteroids[i].hits(bullets[j].pos, 2)) {
        // Large Asteroid (>13): 20 pts, Medium Asteroid (>7): 50 pts, Small Asteroid: 100 pts
        if (asteroids[i].r > 13) {
          score += 20;
        } else if (asteroids[i].r > 7) {
          score += 50;
        } else {
          score += 100;
        }

        // Asteroid splits into smaller pieces
        let newPieces = asteroids[i].break();
        if (newPieces.length > 0) {
          asteroids.push(newPieces[0]);
          asteroids.push(newPieces[1]);
        }

        // Remove bullet and destroyed asteroid
        asteroids.splice(i, 1);
        bullets.splice(j, 1);
        // Each original size asteroid generates 6 more asteroids
        // So generate a new asteroid each 6 destroyed ones
        if(random(1) <= 1/6){
          asteroids.push(new Asteroid());
        }
        break; // Stop checking bullets for this destroyed asteroid
      }
    }
  }
  // Update, draw and handle collisions for saucer
  if (saucer) {
    saucer.update();
    saucer.draw();

    // Check collision with player ship
    if (saucer.hits(player.pos, 10)) {
      player.pos = createVector(0, 0);
      player.angle = PI/2;
      player.vel = createVector(0, 0);
      if (lives > 0) lives--;
    }
    if (saucer.pos.x < -width/2 - 50 || saucer.pos.x > width/2 - 50) {
      saucer = null; // Remove saucer if it goes off screen
    }else {   
    // Check collision with bullets
      for (let j = bullets.length - 1; j >= 0; j--) {
        if (saucer.hits(bullets[j].pos, 2)) {
          // Large Saucer (r > 15): 200 pts, Small Saucer (r <= 15): 1000 pts
          score += (saucer.r <= 15) ? 1000 : 200;
          bullets.splice(j, 1);
          saucer = null;  
          break;
        }
      }
    }
  
  } else if (frameCount % (60 * 15) === 0) {
    // Under 10,000 points: Large Saucer
    // 10,000 points and above: Small Saucer
    let saucerRadius = (score >= 10000) ? 10 : 20;
    saucer = new Saucer(saucerRadius);
  } 
  
  pop();
}

// Only a bullet per press, not every frame.
// (keyIsDown inside draw checks every frame) 
function keyPressed(){
  if (keyCode === 32) {
    bullets.push(new Bullet(player.pos, player.angle));
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

function drawHeart(x, y, size) {
  push();
  translate(x, y);
  fill(255, 40, 60);
  stroke(255);
  strokeWeight(1);
  beginShape();
  vertex(0, -size * 0.2);
  bezierVertex(-size * 0.5, -size * 0.8, -size, -size * 0.1, 0, size * 0.8);
  bezierVertex(size, -size * 0.1, size * 0.5, -size * 0.8, 0, -size * 0.2);
  endShape(CLOSE);
  pop();
}

class Player{
  constructor(){
    this.pos = createVector(0, 0);
    this.vel = createVector(0, 0);

    this.color = color(255, 255, 255);
    // The angle is the x axis or the front of the ship
    this.angle = PI/2;
    this.invulnerableTimer = 0; // Frames of invulnerability after respawn
  }

  respawn(){
    this.pos = createVector(0, 0);
    this.vel = createVector(0, 0);
    this.angle = PI/2;
    this.invulnerableTimer = 120; // 2 seconds of grace period at 60 fps
  }

  isInvulnerable(){
    return this.invulnerableTimer > 0;
  }

  draw(){
    // Invulnerability visual indicator (blinking effect)
    if (this.invulnerableTimer > 0 && floor(frameCount / 6) % 2 === 0) {
      // Blink: skip drawing ship body on alternating frames
    } else {
      push();
      translate(this.pos.x, this.pos.y);
      rotate(this.angle);
      stroke(this.color);
      noFill();
      triangle(15, 0, -10, -5, -10, 5);
      pop();
    }
    // All the bullets are updated, drawed and removed if dead
    for (let i = bullets.length - 1; i >= 0; i--){
      bullets[i].update();
      bullets[i].draw();
      if (bullets[i].isDead()){
        bullets.splice(i, 1);
        
      }

    }
  }

  update(){
    if (this.invulnerableTimer > 0) {
      this.invulnerableTimer--;
    }
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
    // angle = front of the ship
    this.angle = angle;
    // position = front of the ship
    this.pos = createVector(pos.x, pos.y);
    this.pos.add(p5.Vector.fromAngle(this.angle).mult(15));
    // inicial velocity
    this.vel = p5.Vector.fromAngle(this.angle).mult(8);
  }

  draw(){
    push();
    fill(255);
    ellipse(this.pos.x, this.pos.y, 5, 5);
    pop();
  }

  update(){
    // move and slow down the bullet
    this.pos.add(this.vel);
    this.vel.mult(0.99);
    wrap(this.pos, 5);
  }

  isDead(){
    //if the bullet is slow enough, it is dead
    if (this.vel.mag() < 4){
      return true;
    }
  }
}

class Asteroid{
  constructor(pos, r){
    // Default radius for large asteroid is around 20
    this.r = r || random(16, 24);

    // Spawn at a given position, or randomly away from origin (player)
    if (pos) {
      this.pos = pos.copy();
    } else {
      let angle = random(TWO_PI);
      let distFromCenter = random(120, width / 2);
      this.pos = createVector(cos(angle) * distFromCenter, sin(angle) * distFromCenter);
    }

    // Kinematics and rotation
    this.vel = p5.Vector.fromAngle(random(TWO_PI)).mult(random(0.5, 1.5));
    this.angle = random(TWO_PI);
    // Some rotate clockwise, some counterclockwise
    this.rotSpeed = random(-0.02, 0.02);
    this.color = color(255);

    // Irregular rocky shape (offsets per vertex)
    this.total = floor(random(10, 20));
    this.offsets = [];
    for (let i = 0; i < floor(random(10, 20)); i++) {
      this.offsets.push(random(-this.r * 0.4, this.r * 0.4));
    }
  }

  draw(){
    push();
    translate(this.pos.x, this.pos.y);
    rotate(this.angle);
    stroke(this.color);
    noFill();
    beginShape();
    for (let i = 0; i < this.offsets.length; i++) {
      let a = map(i, 0, this.offsets.length, 0, TWO_PI);
      let rad = this.r + this.offsets[i];
      let x = rad * cos(a);
      let y = rad * sin(a);
      vertex(x, y);
    }
    endShape(CLOSE);
    pop();
  }

  update(){
    // move
    this.pos.add(this.vel);
    // rotate
    this.angle += this.rotSpeed;
    wrap(this.pos, this.r);
  }

  // Splits into two smaller asteroids if large enough
  break(){
    let pieces = [];
    if (this.r > 7) {
      pieces.push(new Asteroid(this.pos, this.r / 2));
      pieces.push(new Asteroid(this.pos, this.r / 2));
    }
    return pieces;
  }

  // Distance check between centers against combined radii
  hits(targetPos, targetRadius = 0){
    let d = dist(this.pos.x, this.pos.y, targetPos.x, targetPos.y);
    return d < this.r + targetRadius;
  }
}

class Saucer{
  constructor(r){
    // Radius can be 20 for large or 10 for small)
    this.r = r;

    // Direction: enters from left (-1) or right (1)
    let side = random() < 0.5 ? -1 : 1;
    this.dir = -side; // Moves across to the opposite side

    let halfW = width / 2;
    let halfH = height / 2;


    this.pos = createVector(side * (halfW + this.r), random(-halfH * 0.7, halfH * 0.7));

    // Horizontal speed and velocity
    this.vel = createVector(this.dir * random(1, 2), 0);

    this.color = color(255);

    // Timers for classic zig-zag vertical movement
    this.timer = 0;
    this.changeInterval = floor(random(30, 60));

    // Shoot cooldown timer
    this.shootTimer = 0;
    this.shootInterval = floor(random(70, 150));
  }

  draw(){
    push();
    translate(this.pos.x, this.pos.y);
    stroke(this.color);
    noFill();

    // Classic vector saucer shape (Atari Asteroids style)
    // Outer perimeter
    beginShape();
    vertex(-this.r * 0.4, -this.r * 0.4); // bottom-left base
    vertex(this.r * 0.4, -this.r * 0.4);  // bottom-right base
    vertex(this.r, 0);                    // right middle point
    vertex(this.r * 0.5, this.r * 0.25);  // right dome base
    vertex(this.r * 0.25, this.r * 0.55); // right dome top
    vertex(-this.r * 0.25, this.r * 0.55);// left dome top
    vertex(-this.r * 0.5, this.r * 0.25); // left dome base
    vertex(-this.r, 0);                   // left middle point
    endShape(CLOSE);

    // Internal structural lines of the saucer
    line(-this.r, 0, this.r, 0);
    line(-this.r * 0.5, this.r * 0.25, this.r * 0.5, this.r * 0.25);
    pop();
  }

  update(){
    // Periodic vertical zig-zag change
    this.timer++;
    if (this.timer % this.changeInterval === 0) {
      this.vel.y = random([-1, 0, 1]) * random(0.5, 1.5);
      this.timer = 0;
    }

    // Move
    this.pos.add(this.vel);

  }

  // Check if it's ready to shoot
  canShoot(){
    this.shootTimer++;
    if (this.shootTimer % this.shootInterval === 0) {
      this.shootTimer = 0;
      return true;
    }
    return false;
  }

  // Spawns a bullet aimed at target (e.g. player.pos) or random direction
  shoot(targetPos){
    let angle;
    if (targetPos) {
      let desired = p5.Vector.sub(targetPos, this.pos);
      // Slight aim error for gameplay balance
      angle = desired.heading();
    } else { 
      angle = random(TWO_PI);
    }
    return new Bullet(this.pos, angle);
  }

  // Distance check between centers against combined radii
  hits(targetPos, targetRadius = 0){
    let d = dist(this.pos.x, this.pos.y, targetPos.x, targetPos.y);
    return d < this.r + targetRadius;
  }
}

