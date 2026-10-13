// Module aliases
const { Engine, Bodies, Body, Events, Composite } = Matter;

const CANVAS_WIDTH = 1024;
const CANVAS_HEIGHT = 696;
const FLOOR_Y = 606; // Court baseline in Background.png

const bgImg = new Image();
bgImg.src = 'Background.png';

const p1Img = new Image();
p1Img.src = 'Curry.png';

const p2Img = new Image();
p2Img.src = 'Lebron.png';

const hoopImg = new Image();
hoopImg.src = 'Hoop.png';

let player1, player2, ball;
let leftHoop, rightHoop;
let game;

function setup() {
  const canvas = createCanvas(CANVAS_WIDTH, CANVAS_HEIGHT);
  canvas.parent('game-container');

  engine = Engine.create();
  engine.gravity.y = 0.65;

  createBoundaries();

  leftHoop = new Hoop(true);
  rightHoop = new Hoop(false);
  player1 = new Player(280, FLOOR_Y - 44, true);
  player2 = new Player(width - 280, FLOOR_Y - 44, false);
  ball = new Ball(width / 2, 230);
  game = new Game();

  setupCollisions();

  window.addEventListener('keydown', (e) => {
    if (['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight', ' '].includes(e.key)) {
      e.preventDefault();
    }
  });
}

function draw() {
  game.update();

  if (!game.isGameOver) {
    player1.update();
    player2.update();
  }

  Engine.update(engine, 1000 / 60);

  // Clear previous frame and render court background
  background(20);
  if (bgImg.complete) {
    drawingContext.drawImage(bgImg, 0, 0, width, height);
  }

  leftHoop.show();
  rightHoop.show();
  player1.show();
  player2.show();
  ball.show();
  game.drawScoreboard();
}

function createBoundaries() {
  const thickness = 60;
  const floor = Bodies.rectangle(width / 2, FLOOR_Y + thickness / 2, width * 2, thickness, { isStatic: true, restitution: 0.6 });
  const ceiling = Bodies.rectangle(width / 2, -thickness / 2, width * 2, thickness, { isStatic: true });
  const leftWall = Bodies.rectangle(-thickness / 2, height / 2, thickness, height * 2, { isStatic: true, restitution: 0.7 });
  const rightWall = Bodies.rectangle(width + thickness / 2, height / 2, thickness, height * 2, { isStatic: true, restitution: 0.7 });
  Composite.add(engine.world, [floor, ceiling, leftWall, rightWall]);
}

function setupCollisions() {
  const checkGoal = (event) => {
    for (const pair of event.pairs) {
      const { bodyA, bodyB } = pair;
      const isBall = bodyA === ball.body || bodyB === ball.body;
      if (!isBall) continue;

      if ((bodyA === leftHoop.sensor || bodyB === leftHoop.sensor) && ball.body.velocity.y > 0.05) {
        game.handleGoal(false);
      } else if ((bodyA === rightHoop.sensor || bodyB === rightHoop.sensor) && ball.body.velocity.y > 0.05) {
        game.handleGoal(true);
      }
    }
  };

  Events.on(engine, 'collisionStart', checkGoal);
  Events.on(engine, 'collisionActive', checkGoal);
}

// ====================================================================
// CLASSES (OOP)
// ====================================================================

class Player {
  constructor(x, y, isP1) {
    this.isP1 = isP1;
    this.radius = 44;
    this.img = isP1 ? p1Img : p2Img;
    this.crop = isP1 ? { sx: 644, sy: 20, sw: 1072, sh: 1752 } : { sx: 644, sy: 24, sw: 1080, sh: 1748 };
    this.renderW = 66;
    this.renderH = 108;

    this.body = Bodies.circle(x, y, this.radius, {
      restitution: 0.05,
      friction: 0.1,
      frictionAir: 0.04,
      density: 0.015,
      inertia: Infinity
    });
    Composite.add(engine.world, this.body);
  }

  isGrounded() {
    return this.body.position.y >= FLOOR_Y - this.radius - 4 && this.body.velocity.y >= -1.0;
  }

  update() {
    Body.setAngle(this.body, 0);
    Body.setAngularVelocity(this.body, 0);

    let vx = 0;
    if (this.isP1) {
      if (keyIsDown(65)) vx -= 5.2; // A
      if (keyIsDown(68)) vx += 5.2; // D
      if (keyIsDown(87) && this.isGrounded()) { // W
        Body.setVelocity(this.body, { x: this.body.velocity.x, y: -12.8 });
      }
    } else {
      if (keyIsDown(LEFT_ARROW)) vx -= 5.2;
      if (keyIsDown(RIGHT_ARROW)) vx += 5.2;
      if (keyIsDown(UP_ARROW) && this.isGrounded()) {
        Body.setVelocity(this.body, { x: this.body.velocity.x, y: -12.8 });
      }
    }

    if (vx !== 0) {
      Body.setVelocity(this.body, { x: vx, y: this.body.velocity.y });
    } else {
      Body.setVelocity(this.body, { x: this.body.velocity.x * 0.85, y: this.body.velocity.y });
    }
  }

  show() {
    push();
    translate(this.body.position.x, this.body.position.y);
    if (!this.isP1) scale(-1, 1);

    if (this.img.complete) {
      drawingContext.drawImage(
        this.img,
        this.crop.sx,
        this.crop.sy,
        this.crop.sw,
        this.crop.sh,
        -this.renderW / 2,
        this.radius - this.renderH,
        this.renderW,
        this.renderH
      );
    } else {
      fill(255);
      stroke(30);
      strokeWeight(3);
      ellipse(0, 0, this.radius * 2);
    }
    pop();

    textAlign(CENTER, CENTER);
    fill(255);
    stroke(0);
    strokeWeight(3);
    textSize(12);
    textStyle(BOLD);
    text(this.isP1 ? 'P1' : 'P2', this.body.position.x, this.body.position.y + this.radius - this.renderH - 10);
  }

  reset(x) {
    Body.setPosition(this.body, { x: x, y: FLOOR_Y - this.radius });
    Body.setVelocity(this.body, { x: 0, y: 0 });
  }
}

class Ball {
  constructor(x, y) {
    this.radius = 18;
    this.body = Bodies.circle(x, y, this.radius, {
      restitution: 0.82,
      friction: 0.03,
      frictionAir: 0.007,
      density: 0.0008
    });
    Composite.add(engine.world, this.body);
  }

  reset() {
    Body.setPosition(this.body, { x: width / 2, y: 230 });
    Body.setVelocity(this.body, { x: 0, y: 0 });
    Body.setAngularVelocity(this.body, 0);
    Body.setAngle(this.body, 0);
  }

  show() {
    push();
    translate(this.body.position.x, this.body.position.y);
    rotate(this.body.angle);

    fill(245, 110, 30);
    stroke(30);
    strokeWeight(2.5);
    ellipse(0, 0, this.radius * 2);

    noFill();
    stroke(30);
    strokeWeight(1.8);
    line(-this.radius, 0, this.radius, 0);
    line(0, -this.radius, 0, this.radius);
    arc(-this.radius * 0.45, 0, this.radius, this.radius * 1.8, -HALF_PI, HALF_PI);
    arc(this.radius * 0.45, 0, this.radius, this.radius * 1.8, HALF_PI, -HALF_PI);
    pop();
  }
}

class Hoop {
  constructor(isLeft) {
    this.isLeft = isLeft;
    this.span = 88;
    this.backX = isLeft ? 22 : width - 22;
    this.frontX = isLeft ? this.backX + this.span : this.backX - this.span;
    this.y = 340;

    // Permissive rim pins: friendly bounce (restitution 0.35) and slight friction so shots roll in
    this.pinBack = Bodies.circle(this.backX, this.y, 5, {
      isStatic: true,
      restitution: 0.35,
      friction: 0.15
    });
    this.pinFront = Bodies.circle(this.frontX, this.y, 5, {
      isStatic: true,
      restitution: 0.35,
      friction: 0.15
    });

    // Permissive scoring sensor across rim throat
    const sensorW = this.span - 8;
    const sensorH = 26;
    const sensorX = (this.backX + this.frontX) / 2;
    const sensorY = this.y + 16;
    this.sensor = Bodies.rectangle(sensorX, sensorY, sensorW, sensorH, {
      isStatic: true,
      isSensor: true
    });

    // Backboard physics collider for bank shots
    const bbWidth = 18;
    const bbHeight = 105;
    const bbX = isLeft ? bbWidth / 2 : width - bbWidth / 2;
    const bbY = 275 + bbHeight / 2;
    this.backboard = Bodies.rectangle(bbX, bbY, bbWidth, bbHeight, {
      isStatic: true,
      restitution: 0.55,
      friction: 0.1
    });

    // Invisible vertical barrier: thin vertical line from hoop to floor.
    // Blocks horizontal traversal past the hoop, but allows vertical movement.
    const bWidth = 6;
    const bHeight = FLOOR_Y - this.y;
    const bX = this.backX;
    const bY = this.y + bHeight / 2;
    this.barrier = Bodies.rectangle(bX, bY, bWidth, bHeight, {
      isStatic: true,
      restitution: 0.3,
      friction: 0.1
    });

    Composite.add(engine.world, [this.backboard, this.pinBack, this.pinFront, this.sensor, this.barrier]);
  }

  show() {
    push();
    // Backboard
    rectMode(CORNER);
    fill(255);
    stroke(30);
    strokeWeight(3);
    if (this.isLeft) {
      rect(0, 275, 18, 105);
      fill(220, 40, 40);
      stroke(30);
      strokeWeight(2);
      rect(3, 310, 12, 30);
    } else {
      rect(width - 18, 275, 18, 105);
      fill(220, 40, 40);
      stroke(30);
      strokeWeight(2);
      rect(width - 15, 310, 12, 30);
    }

    // Hoop.png integration
    if (hoopImg.complete && hoopImg.naturalWidth > 0) {
      const pinDistInImg = 248; // distance between pin centers in Hoop.png (x=54 to x=302)
      const scaleFactor = this.span / pinDistInImg;
      const imgW = 347 * scaleFactor;
      const imgH = 348 * scaleFactor;

      push();
      if (this.isLeft) {
        const drawX = this.pinBack.position.x - 54 * scaleFactor;
        const drawY = this.pinBack.position.y - 141 * scaleFactor;
        drawingContext.drawImage(hoopImg, drawX, drawY, imgW, imgH);
      } else {
        translate(this.pinBack.position.x, this.pinBack.position.y);
        scale(-1, 1);
        drawingContext.drawImage(hoopImg, -54 * scaleFactor, -141 * scaleFactor, imgW, imgH);
      }
      pop();
    } else {
      // Fallback procedural rim & net
      fill(255, 235);
      stroke(60);
      strokeWeight(1.5);
      beginShape();
      if (this.isLeft) {
        vertex(this.pinBack.position.x, this.pinBack.position.y);
        vertex(this.pinFront.position.x, this.pinFront.position.y);
        vertex(this.pinFront.position.x - 14, this.pinFront.position.y + 36);
        vertex(this.pinBack.position.x + 8, this.pinBack.position.y + 36);
      } else {
        vertex(this.pinBack.position.x, this.pinBack.position.y);
        vertex(this.pinFront.position.x, this.pinFront.position.y);
        vertex(this.pinFront.position.x + 14, this.pinFront.position.y + 36);
        vertex(this.pinBack.position.x - 8, this.pinBack.position.y + 36);
      }
      endShape(CLOSE);

      fill(255, 85, 0);
      stroke(30);
      strokeWeight(3);
      line(this.pinBack.position.x, this.pinBack.position.y, this.pinFront.position.x, this.pinFront.position.y);
      ellipse(this.pinBack.position.x, this.pinBack.position.y, 10);
      ellipse(this.pinFront.position.x, this.pinFront.position.y, 10);
    }
    pop();
  }
}

class Game {
  constructor() {
    this.scoreP1 = 0;
    this.scoreP2 = 0;
    this.timeRemaining = 60; // 1-minute match
    this.isGameOver = false;
    this.isScoring = false;
    this.scoreMessage = '';
    this.lastTime = millis();
  }

  update() {
    const now = millis();
    const dt = (now - this.lastTime) / 1000;
    this.lastTime = now;

    if (!this.isGameOver) {
      this.timeRemaining -= dt;
      if (this.timeRemaining <= 0) {
        this.timeRemaining = 0;
        this.isGameOver = true;
      }

      // Permissive scoring & net guide assists
      if (!this.isScoring && ball && ball.body) {
        const bx = ball.body.position.x;
        const by = ball.body.position.y;
        const vy = ball.body.velocity.y;

        // Downward ball traversing hoop throat
        if (vy > 0.05) {
          if (bx >= leftHoop.pinBack.position.x - 4 && bx <= leftHoop.pinFront.position.x + 4) {
            if (by >= leftHoop.y + 6 && by <= leftHoop.y + 36) {
              this.handleGoal(false);
            }
          } else if (bx >= rightHoop.pinFront.position.x - 4 && bx <= rightHoop.pinBack.position.x + 4) {
            if (by >= rightHoop.y + 6 && by <= rightHoop.y + 36) {
              this.handleGoal(true);
            }
          }
        }

        // Net funnel: guides ball down smoothly inside net
        const inLeftNet = bx >= leftHoop.pinBack.position.x && bx <= leftHoop.pinFront.position.x && by >= leftHoop.y && by <= leftHoop.y + 50;
        const inRightNet = bx >= rightHoop.pinFront.position.x && bx <= rightHoop.pinBack.position.x && by >= rightHoop.y && by <= rightHoop.y + 50;
        if (inLeftNet || inRightNet) {
          Body.setVelocity(ball.body, { x: ball.body.velocity.x * 0.92, y: ball.body.velocity.y });
        }
      }
    } else if (keyIsDown(82) || keyIsDown(32)) { // R or Space to restart
      this.restart();
    }
  }

  handleGoal(isRightHoop) {
    if (this.isScoring || this.isGameOver) return;
    this.isScoring = true;

    if (isRightHoop) {
      this.scoreP1++;
      this.scoreMessage = 'P1 SCORED! (+1)';
    } else {
      this.scoreP2++;
      this.scoreMessage = 'P2 SCORED! (+1)';
    }

    setTimeout(() => {
      ball.reset();
      this.scoreMessage = '';
      this.isScoring = false;
    }, 1000);
  }

  restart() {
    this.scoreP1 = 0;
    this.scoreP2 = 0;
    this.timeRemaining = 60;
    this.isGameOver = false;
    this.isScoring = false;
    this.scoreMessage = '';
    this.lastTime = millis();

    player1.reset(280);
    player2.reset(width - 280);
    ball.reset();
  }

  drawScoreboard() {
    push();
    textAlign(CENTER, CENTER);

    // P1 Panel
    fill(255, 215, 0);
    noStroke();
    textSize(13);
    textStyle(BOLD);
    text('P1', 398, 88);

    fill(255);
    stroke(20);
    strokeWeight(2);
    textSize(30);
    text(this.scoreP1, 398, 116);

    // Clock
    fill(200);
    noStroke();
    textSize(10);
    text('TIME', 511, 88);

    const secs = Math.ceil(this.timeRemaining);
    const m = Math.floor(secs / 60);
    const s = secs % 60;
    const timeStr = nf(m, 2) + ':' + nf(s, 2);

    fill(secs <= 10 && secs > 0 ? color(255, 60, 60) : color(255));
    stroke(20);
    strokeWeight(2);
    textSize(22);
    text(timeStr, 511, 114);

    // P2 Panel
    fill(255, 215, 0);
    noStroke();
    textSize(13);
    text('P2', 625, 88);

    fill(255);
    stroke(20);
    strokeWeight(2);
    textSize(30);
    text(this.scoreP2, 625, 116);

    // Goal banner
    if (this.isScoring && this.scoreMessage !== '' && !this.isGameOver) {
      rectMode(CENTER);
      fill(255);
      stroke(30);
      strokeWeight(3);
      rect(width / 2, 180, 320, 44, 8);

      fill(30);
      noStroke();
      textSize(20);
      text(this.scoreMessage, width / 2, 179);
    }

    // Controls at bottom
    fill(255);
    stroke(20);
    strokeWeight(2.5);
    textSize(13);
    text('P1: [A / D] Move  [W] Jump   |   P2: [Left / Right] Move  [Up] Jump', width / 2, 675);

    // Game over screen
    if (this.isGameOver) {
      rectMode(CENTER);
      fill(255);
      stroke(30);
      strokeWeight(4);
      rect(width / 2, height / 2 - 20, 420, 140, 12);

      fill(30);
      noStroke();
      textSize(24);
      text('GAME OVER', width / 2, height / 2 - 60);

      textSize(22);
      if (this.scoreP1 > this.scoreP2) {
        fill(20, 120, 220);
        text('P1 WINS!', width / 2, height / 2 - 24);
      } else if (this.scoreP2 > this.scoreP1) {
        fill(220, 80, 20);
        text('P2 WINS!', width / 2, height / 2 - 24);
      } else {
        fill(80);
        text('DRAW!', width / 2, height / 2 - 24);
      }

      fill(80);
      textSize(13);
      textStyle(NORMAL);
      text('Press [R] or [Space] to restart', width / 2, height / 2 + 18);
    }
    pop();
  }
}