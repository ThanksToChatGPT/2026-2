let player;
let asteroids = [];
let score = 0;
let bullets = [];
let saucer;
let saucerBullets = [];
let lives = 3;
let wave = 1;
let gameOver = false;
let nextExtraLifeScore = 10000; // Extra life every 10,000 points

function setup() {
  createCanvas(500, 500);
  resetGame();
}

function resetGame() {
  score = 0;
  lives = 3;
  wave = 1;
  gameOver = false;
  nextExtraLifeScore = 10000;
  bullets = [];
  saucerBullets = [];
  saucer = null;
  player = new Player();
  player.respawn();
  startWave(wave);
}

// Starts a wave with progressive number of asteroids (4 in wave 1, +2 per wave)
function startWave(w) {
  asteroids = [];
  saucerBullets = [];
  let numAsteroids = 4 + min(w - 1, 4) * 2;
  for (let i = 0; i < numAsteroids; i++) {
    asteroids.push(new Asteroid());
  }
}

function playerHit() {
  if (player.isInvulnerable() || gameOver) return;
  lives--;
  if (lives <= 0) {
    gameOver = true;
  } else {
    player.respawn();
  }
}

function draw() {
  background(0);

  // HUD: Classic score and lives in standard screen coordinates
  fill(255);
  noStroke();
  textSize(18);
  textAlign(LEFT, TOP);
  text(nf(floor(score), 2), 20, 20);

  // Extra life bonus every 10,000 points
  if (score >= nextExtraLifeScore) {
    lives++;
    nextExtraLifeScore += 10000;
  }

  // HUD: Draw lives as miniature vector ships
  for (let i = 0; i < lives; i++) {
    drawShipIcon(440 + i * 18, 30);
  }

  // Game Over state
  if (gameOver) {
    textAlign(CENTER, CENTER);
    fill(255);
    textSize(28);
    text("GAME OVER", width / 2, height / 2 - 20);
    textSize(14);
    text("PRESIONA 'r' PARA REINICIAR", width / 2, height / 2 + 25);
    return;
  }

  // Next wave when all asteroids are destroyed
  if (asteroids.length === 0) {
    wave++;
    startWave(wave);
  }

  // Classic Asteroids centered Cartesian coordinates
  push();
  translate(width / 2, height / 2);
  scale(1, -1);

  player.update();
  player.draw();

  // Update, draw, and handle collisions for asteroids
  for (let i = asteroids.length - 1; i >= 0; i--) {
    asteroids[i].update();
    asteroids[i].draw();

    // Check collision with player ship
    if (asteroids[i].hits(player.pos, 10)) {
      playerHit();
    }

    // Check collision with player bullets
    for (let j = bullets.length - 1; j >= 0; j--) {
      if (asteroids[i].hits(bullets[j].pos, 2)) {
        // Atari scoring: Large: 20 pts, Medium: 50 pts, Small: 100 pts
        if (asteroids[i].r > 13) {
          score += 20;
        } else if (asteroids[i].r > 7) {
          score += 50;
        } else {
          score += 100;
        }

        // Asteroid splits into 2 smaller pieces
        let newPieces = asteroids[i].break();
        if (newPieces.length > 0) {
          asteroids.push(newPieces[0]);
          asteroids.push(newPieces[1]);
        }

        // Remove bullet and destroyed asteroid
        asteroids.splice(i, 1);
        bullets.splice(j, 1);
        break; // Stop checking bullets for this destroyed asteroid
      }
    }
  }

  // Update, draw, and handle collisions for saucer
  if (saucer) {
    saucer.update();
    saucer.draw();

    // Saucer shooting
    if (saucer.canShoot()) {
      // Small saucer (r <= 15) aims at player; large saucer shoots randomly
      let target = (saucer.r <= 15) ? player.pos : null;
      saucerBullets.push(saucer.shoot(target));
    }

    // Check collision with player ship
    if (saucer.hits(player.pos, 12)) {
      playerHit();
    }

    // Remove saucer if it goes off screen (width/2 + 50)
    if (saucer.pos.x < -width / 2 - 50 || saucer.pos.x > width / 2 + 50) {
      saucer = null;
    } else {
      // Check collision with bullets
      for (let j = bullets.length - 1; j >= 0; j--) {
        if (saucer.hits(bullets[j].pos, 2)) {
          // Scoring: Large saucer: 200 pts, Small saucer: 1000 pts
          score += (saucer.r <= 15) ? 1000 : 200;
          bullets.splice(j, 1);
          saucer = null;
          break;
        }
      }
    }
  } else if (frameCount > 0 && frameCount % (60 * 18) === 0) {
    // Under 10,000 points: Large Saucer (r=20). 10,000 points and above: Small Saucer (r=10)
    let saucerRadius = (score >= 10000) ? 10 : 20;
    saucer = new Saucer(saucerRadius);
  }

  // Update, draw, and check collisions for saucer bullets
  for (let k = saucerBullets.length - 1; k >= 0; k--) {
    saucerBullets[k].update();
    saucerBullets[k].draw();

    if (dist(saucerBullets[k].pos.x, saucerBullets[k].pos.y, player.pos.x, player.pos.y) < 10) {
      saucerBullets.splice(k, 1);
      playerHit();
      continue;
    }

    if (saucerBullets[k].isDead()) {
      saucerBullets.splice(k, 1);
    }
  }

  pop();
}

// Game controls
function keyPressed() {
  if (gameOver) {
    if (key === 'r') {
      resetGame();
    }
    return;
  }

  // Spacebar: Shoot
  if (keyCode === 32) {
    bullets.push(new Bullet(player.pos, player.angle));
    return;
  }

  // Down arrow / KeyCode 40: Hyperspace
  if (keyCode === 40 || key === 's') {
    player.hyperspace();
    return;
  }
}

function wrap(pos, r = 0) {
  let halfW = width / 2;
  let halfH = height / 2;

  if (pos.x > halfW + r) pos.x = -halfW - r;
  else if (pos.x < -halfW - r) pos.x = halfW + r;

  if (pos.y > halfH + r) pos.y = -halfH - r;
  else if (pos.y < -halfH - r) pos.y = halfH + r;
}

// Vector ship drawing function for HUD and Player (scalable size)
function drawShipIcon(x, y, size = 10, angle = -PI / 2, thrusting = false) {
  push();
  translate(x, y);
  rotate(angle);
  stroke(255);
  strokeWeight(1.5);
  noFill();

  // Classic vector ship shape (triangle with rear notch)
  beginShape();
  vertex(size, 0);                  // Front nose
  vertex(-size * 0.7, -size * 0.5); // Back-left wing
  vertex(-size * 0.4, 0);           // Rear-center notch
  vertex(-size * 0.7, size * 0.5);  // Back-right wing
  endShape(CLOSE);

  // Flickering thrust flame when accelerating (Atari arcade style)
  if (thrusting) {
    beginShape();
    vertex(-size * 0.4, -size * 0.22);
    vertex(-size * (0.8 + random(0.25)), 0);
    vertex(-size * 0.4, size * 0.22);
    endShape();
  }

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
    this.isThrusting = false;
  }

  respawn(){
    this.pos = createVector(0, 0);
    this.vel = createVector(0, 0);
    this.angle = PI/2;
    this.invulnerableTimer = 120; // 2 seconds of grace period at 60 fps
    this.isThrusting = false;
  }

  isInvulnerable(){
    return this.invulnerableTimer > 0;
  }

  // Hyperspace jump to random coordinates
  hyperspace(){
    let halfW = width / 2 - 30;
    let halfH = height / 2 - 30;
    this.pos = createVector(random(-halfW, halfW), random(-halfH, halfH));
    this.vel = createVector(0, 0);
    this.invulnerableTimer = 30; // 0.5s of invulnerability after jump
  }

  draw(){
    // Invulnerability visual indicator (blinking effect)
    if (this.invulnerableTimer > 0 && floor(frameCount / 6) % 2 === 0) {
      // Blink: skip drawing ship body on alternating frames
    } else {
      // Draw player ship using drawShipIcon with size 15
      drawShipIcon(this.pos.x, this.pos.y, 15, this.angle, this.isThrusting);
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
    if (keyIsDown(LEFT_ARROW) || keyIsDown("a")) {
      this.angle += 0.05;
    } else if (keyIsDown(RIGHT_ARROW) || keyIsDown("d")) { 
      this.angle -= 0.05;
    }
    
    this.isThrusting = keyIsDown(UP_ARROW) || keyIsDown("w");
    if (this.isThrusting) {
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
    // initial velocity
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
    // if the bullet is slow enough, it is dead
    return this.vel.mag() < 4;
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
    for (let i = 0; i < this.total; i++) {
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
    // Radius can be 20 for large or 10 for small
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

  // Spawns a bullet 
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

