//Inspired on https://www.miniplay.com/game/sports-heads-basketball
// Matter.js objects
let Engine = Matter.Engine;
let Bodies = Matter.Bodies;
let Body = Matter.Body;
let Events = Matter.Events;
let Composite = Matter.Composite;

// Dimensions
let CANVAS_WIDTH = 1024;
let CANVAS_HEIGHT = 696;
let FLOOR_Y = 606; // Height where players walk

// Image assets made with Gemini 
let bgImg = new Image();
bgImg.src = 'Background.png';

let p1Img = new Image();
p1Img.src = 'Curry.png';

let p2Img = new Image();
p2Img.src = 'Lebron.png';

let hoopImg = new Image();
hoopImg.src = 'Hoop.png';

// Global variables for game
let engine;
let player1;
let player2;
let ball;
let leftHoop;
let rightHoop;
let game;


function setup() {
  let canvas = createCanvas(CANVAS_WIDTH, CANVAS_HEIGHT);

  // Attach to container if present, otherwise p5 attaches it to body
  let container = document.getElementById('game-container');
  if (container) {
    canvas.parent(container);
  }

  engine = Engine.create();
  engine.gravity.y = 0.65;

  createBoundaries();

  // Create hoops (true = left, false = right)
  leftHoop = new Hoop(true);
  rightHoop = new Hoop(false);

  player1 = new Player(280, FLOOR_Y - 44, true);
  player2 = new Player(width - 280, FLOOR_Y - 44, false);
  ball = new Ball(width / 2, 230);

  // score, timer, game over
  game = new Game();

  setupCollisions();

}

function draw() {
  // Update game timer and scoring
  game.update();

  // Only move players if the game is running
  if (game.isGameOver === false) {
    player1.update();
    player2.update();
  }

  // Advance the physics engine by one step (60 FPS)
  Engine.update(engine, 1000 / 60);

  // Draw background
  background(20);
  if (bgImg.complete) {
    drawingContext.drawImage(bgImg, 0, 0, width, height);
  }

  // Draw hoops, players, and ball
  leftHoop.draw();
  rightHoop.draw();
  player1.draw();
  player2.draw();
  ball.draw();

  // Draw scoreboard and UI
  game.drawScoreboard();
}


function createBoundaries() {
  let thickness = 60;

  // Floor with bounce
  let floor = Bodies.rectangle(width / 2, FLOOR_Y + thickness / 2, width * 2, thickness, {
    isStatic: true,
    restitution: 0.67
  });

  let ceiling = Bodies.rectangle(width / 2, -thickness / 2, width * 2, thickness, {
    isStatic: true
  });

  let leftWall = Bodies.rectangle(-thickness / 2, height / 2, thickness, height * 2, {
    isStatic: true,
    restitution: 0.5
  });

  let rightWall = Bodies.rectangle(width + thickness / 2, height / 2, thickness, height * 2, {
    isStatic: true,
    restitution: 0.5
  });

  // Add to the world
  Composite.add(engine.world, [floor, ceiling, leftWall, rightWall]);
}


function setupCollisions() {
  Events.on(engine, 'collisionStart', handlePhysicsCollisions);
  Events.on(engine, 'collisionActive', handlePhysicsCollisions);
}

function handlePhysicsCollisions(event) {
  for (let i = 0; i < event.pairs.length; i++) {
    let pair = event.pairs[i];
    let bodyA = pair.bodyA;
    let bodyB = pair.bodyB;

    // Check trampoline collision
    checkTrampolineHit(bodyA, bodyB);

    // Check goal sensor collision
    checkGoalSensorHit(bodyA, bodyB);
  }
}

// Bounce objects when they touch a trampoline
function checkTrampolineHit(bodyA, bodyB) {
  let hitLeft = (leftHoop && (bodyA === leftHoop.trampoline || bodyB === leftHoop.trampoline));
  let hitRight = (rightHoop && (bodyA === rightHoop.trampoline || bodyB === rightHoop.trampoline));

  if (!hitLeft && !hitRight) {
    return;
  }

  // Find the other body that touched the trampoline
  let otherBody = bodyA;
  if (bodyA === leftHoop.trampoline || bodyA === rightHoop.trampoline) {
    otherBody = bodyB;
  }

  // If Player 1 touches the trampoline
  if (otherBody === player1.body) {
    if (player1.body.velocity.y >= -2) {
      Body.setVelocity(player1.body, { x: player1.body.velocity.x, y: -15 });
    }
  }

  // If Player 2 touches the trampoline
  if (otherBody === player2.body) {
    if (player2.body.velocity.y >= -2) {
      Body.setVelocity(player2.body, { x: player2.body.velocity.x, y: -15 });
    }
  }

  // If the ball touches the trampoline
  if (otherBody === ball.body) {
    let currentYVelocity = ball.body.velocity.y;
    let bouncePower = 16.5;
    if (Math.abs(currentYVelocity) * 1.35 > bouncePower) {
      bouncePower = Math.abs(currentYVelocity) * 1.35;
    }
    Body.setVelocity(ball.body, {
      x: ball.body.velocity.x * 0.95,
      y: -bouncePower
    });
  }
}

// Detect when the ball crosses the goal sensors
function checkGoalSensorHit(bodyA, bodyB) {
  let isBall = (bodyA === ball.body || bodyB === ball.body);
  if (!isBall) {
    return;
  }

  // Ball must be falling downward to count as a score
  if (ball.body.velocity.y <= 0.05) {
    return;
  }

  // Left hoop sensor (Player 2 scores)
  if (bodyA === leftHoop.sensor || bodyB === leftHoop.sensor) {
    game.handleGoal(false);
  }

  // Right hoop sensor (Player 1 scores)
  if (bodyA === rightHoop.sensor || bodyB === rightHoop.sensor) {
    game.handleGoal(true);
  }
}

class Player {
  constructor(x, y, isP1) {
    this.isP1 = isP1;
    this.radius = 44;
    this.renderWidth = 66;
    this.renderHeight = 108;

    // Sprite image and crop coordinates from the character files
    if (this.isP1) {
      this.img = p1Img;
      this.cropX = 644;
      this.cropY = 20;
      this.cropWidth = 1072;
      this.cropHeight = 1752;
    } else {
      this.img = p2Img;
      this.cropX = 644;
      this.cropY = 24;
      this.cropWidth = 1080;
      this.cropHeight = 1748;
    }

    // Physics circle for player body
    this.body = Bodies.circle(x, y, this.radius, {
      restitution: 0.05,
      friction: 0.1,
      frictionAir: 0.04,
      density: 0.015,
      inertia: Infinity // Keeps the player upright
    });

    Composite.add(engine.world, this.body);
  }

  // Check if player is on the ground
  isGrounded() {
    let nearFloor = this.body.position.y >= FLOOR_Y - this.radius - 4;
    let notMovingUp = this.body.velocity.y >= -1.0;
    return nearFloor && notMovingUp;
  }

  update() {
    // Keep player upright
    Body.setAngle(this.body, 0);
    Body.setAngularVelocity(this.body, 0);

    let moveSpeed = 5.2;
    let jumpSpeed = -12.8;
    let horizontalVelocity = 0;

    if (this.isP1) {
      // Player 1 controls: A, D, W 
      if (keyIsDown(65)) { // A
        horizontalVelocity -= moveSpeed;
      }
      if (keyIsDown(68)) { // D
        horizontalVelocity += moveSpeed;
      }
      if (keyIsDown(87) && this.isGrounded()) { // W
        Body.setVelocity(this.body, { x: this.body.velocity.x, y: jumpSpeed });
      }
    } else {
      // Player 2 controls: Arrow keys
      if (keyIsDown(LEFT_ARROW)) {
        horizontalVelocity -= moveSpeed;
      }
      if (keyIsDown(RIGHT_ARROW)) {
        horizontalVelocity += moveSpeed;
      }
      if (keyIsDown(UP_ARROW) && this.isGrounded()) {
        Body.setVelocity(this.body, { x: this.body.velocity.x, y: jumpSpeed });
      }
    }

    // Apply horizontal speed or slow down with friction
    if (horizontalVelocity !== 0) {
      Body.setVelocity(this.body, { x: horizontalVelocity, y: this.body.velocity.y });
    } else {
      Body.setVelocity(this.body, { x: this.body.velocity.x * 0.85, y: this.body.velocity.y });
    }
  }

  // Draw player on the screen
  draw() {
    push();
    translate(this.body.position.x, this.body.position.y);

    // Flip Player 2 to face left
    if (this.isP1 === false) {
      scale(-1, 1);
    }

    // Draw character image
    if (this.img.complete) {
      drawingContext.drawImage(
        this.img,
        this.cropX,
        this.cropY,
        this.cropWidth,
        this.cropHeight,
        -this.renderWidth / 2,
        this.radius - this.renderHeight,
        this.renderWidth,
        this.renderHeight
      );
    }
    pop();

    // Draw player label ('P1' or 'P2') above player's head
    textAlign(CENTER, CENTER);
    fill(255);
    stroke(0);
    strokeWeight(3);
    textSize(12);
    textStyle(BOLD);

    let labelText = 'P1';
    if (this.isP1 === false) {
      labelText = 'P2';
    }
    let labelY = this.body.position.y + this.radius - this.renderHeight - 10;
    text(labelText, this.body.position.x, labelY);
  }

  // Reset player to initial position
  reset(x) {
    Body.setPosition(this.body, { x: x, y: FLOOR_Y - this.radius });
    Body.setVelocity(this.body, { x: 0, y: 0 });
  }
}

class Ball {
  constructor(x, y) {
    this.radius = 18;

    // Physics body for the ball
    this.body = Bodies.circle(x, y, this.radius, {
      restitution: 0.82, // bounciness
      friction: 0.03,
      frictionAir: 0.007,
      density: 0.0008
    });

    Composite.add(engine.world, this.body);
  }

  // Reset ball to center of the court
  reset() {
    Body.setPosition(this.body, { x: width / 2, y: 230 });
    Body.setVelocity(this.body, { x: 0, y: 0 });
    Body.setAngularVelocity(this.body, 0);
    Body.setAngle(this.body, 0);
  }

  // Draw the basketball
  draw() {
    push();
    translate(this.body.position.x, this.body.position.y);
    rotate(this.body.angle);

    // Orange circle
    fill(245, 110, 30);
    stroke(30);
    strokeWeight(2.5);
    ellipse(0, 0, this.radius * 2);

    // Basketball seams
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
    this.span = 88; // Width of the rim opening
    this.y = 340;

    // Determine rim positions depending on left or right side
    if (this.isLeft) {
      this.backX = 22;
      this.frontX = 22 + this.span;
    } else {
      this.backX = width - 22;
      this.frontX = width - 22 - this.span;
    }

    // Back rim pin (bounce points so ball can bounce on rim)
    this.pinBack = Bodies.circle(this.backX, this.y, 5, {
      isStatic: true,
      restitution: 0.35,
      friction: 0.15
    });

    // Front rim pin
    this.pinFront = Bodies.circle(this.frontX, this.y, 5, {
      isStatic: true,
      restitution: 0.35,
      friction: 0.15
    });

    //S core sensor inside the rim
    let sensorWidth = this.span - 8;
    let sensorHeight = 26;
    let sensorX = (this.backX + this.frontX) / 2;
    let sensorY = this.y + 16;
    this.sensor = Bodies.rectangle(sensorX, sensorY, sensorWidth, sensorHeight, {
      isStatic: true,
      isSensor: true
    });

    // Backboard physics collider
    let backboardWidth = 18;
    let backboardHeight = 105;
    let backboardX = backboardWidth / 2;
    if (this.isLeft === false) {
      backboardX = width - backboardWidth / 2;
    }
    let backboardY = 275 + backboardHeight / 2;
    this.backboard = Bodies.rectangle(backboardX, backboardY, backboardWidth, backboardHeight, {
      isStatic: true,
      restitution: 0.55,
      friction: 0.1
    });

    // Trampoline at the base below the hoop
    this.trampolineW = 65;
    this.trampolineH = 12;
    if (this.isLeft) {
      this.trampolineX = this.frontX + this.trampolineW / 2;
    } else {
      this.trampolineX = this.frontX - this.trampolineW / 2;
    }
    this.trampolineY = FLOOR_Y - this.trampolineH / 2;
    this.trampoline = Bodies.rectangle(this.trampolineX, this.trampolineY, this.trampolineW, this.trampolineH, {
      isStatic: true,
      restitution: 0.85,
      friction: 0.1
    });

    // Vertical barrier to block walking into the back area
    let barrierWidth = 10;
    let barrierX = this.frontX;
    let barrierTop = this.y;
    let barrierHeight = (FLOOR_Y - this.trampolineH) - barrierTop;
    let barrierY = barrierTop + barrierHeight / 2;
    this.barrier = Bodies.rectangle(barrierX, barrierY, barrierWidth, barrierHeight, {
      isStatic: true,
      restitution: 0.3,
      friction: 0.1
    });

    // Add everything to physics engine
    Composite.add(engine.world, [
      this.backboard,
      this.pinBack,
      this.pinFront,
      this.sensor,
      this.barrier,
      this.trampoline
    ]);
  }

  // Draw the backboard, rim, net, and trampoline
  draw() {
    push();

    // Draw the backboard
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

    let pinDistanceInImage = 248; // Distance between pin centers in Hoop.png
    let scaleFactor = this.span / pinDistanceInImage;
    let imgWidth = 347 * scaleFactor;
    let imgHeight = 348 * scaleFactor;

    push();
    if (this.isLeft) {
      let drawX = this.pinBack.position.x - 54 * scaleFactor;
      let drawY = this.pinBack.position.y - 141 * scaleFactor;
      drawingContext.drawImage(hoopImg, drawX, drawY, imgWidth, imgHeight);
    } else {
      translate(this.pinBack.position.x, this.pinBack.position.y);
      scale(-1, 1);
      drawingContext.drawImage(hoopImg, -54 * scaleFactor, -141 * scaleFactor, imgWidth, imgHeight);
    }
    pop();
    

    // Draw the red trampoline platform
    rectMode(CENTER);
    fill(225, 35, 35);
    stroke(30);
    strokeWeight(2);
    rect(this.trampolineX, this.trampolineY, this.trampolineW, this.trampolineH, 3);

    pop();
  }
}

// Score, Timer, and UI
class Game {
  constructor() {
    this.scoreP1 = 0;
    this.scoreP2 = 0;
    this.timeRemaining = 67; // 67 seconds match
    this.isGameOver = false;
    this.isScoring = false;
    this.scoreMessage = '';
    this.lastTime = millis();
  }

  // Update timer and gameplay checks
  update() {
    let now = millis();
    let deltaTime = (now - this.lastTime) / 1000;
    this.lastTime = now;

    if (this.isGameOver === false) {
      // Countdown timer
      this.timeRemaining -= deltaTime;
      if (this.timeRemaining <= 0) {
        this.timeRemaining = 0;
        this.isGameOver = true;
      }

      // Check ball position for scoring and net funneling

      // Launch players when they step on trampolines
      this.checkPlayerTrampoline(player1);
      this.checkPlayerTrampoline(player2);
    } else {
      // Press Spacebar to restart game
      if (keyIsDown(32)) {
        this.restart();
      }
    }
  }


  // Check if a player steps onto a trampoline
  checkPlayerTrampoline(player) {
    if (!player || !player.body) {
      return;
    }

    let px = player.body.position.x;
    let py = player.body.position.y;

    let onLeft = (px >= leftHoop.trampolineX - leftHoop.trampolineW / 2 - 2 &&
                  px <= leftHoop.trampolineX + leftHoop.trampolineW / 2 + 2 &&
                  py >= FLOOR_Y - player.radius - 18);

    let onRight = (px >= rightHoop.trampolineX - rightHoop.trampolineW / 2 - 2 &&
                   px <= rightHoop.trampolineX + rightHoop.trampolineW / 2 + 2 &&
                   py >= FLOOR_Y - player.radius - 18);

    // Launch upward if standing on trampoline
    if ((onLeft || onRight) && player.body.velocity.y >= -1.0) {
      Body.setVelocity(player.body, { x: player.body.velocity.x, y: -16.5 });
    }
  }

  // Trigger goal scored
  handleGoal(isRightHoop) {
    if (this.isScoring || this.isGameOver) {
      return;
    }

    this.isScoring = true;

    // Add point and set message
    if (isRightHoop) {
      this.scoreP1++;
      this.scoreMessage = 'P1 SCORED! (+1)';
    } else {
      this.scoreP2++;
      this.scoreMessage = 'P2 SCORED! (+1)';
    }

    // Reset ball after 1 second
    let self = this;
    setTimeout(function() {
      ball.reset();
      self.scoreMessage = '';
      self.isScoring = false;
    }, 1000);
  }

  // Restart match from beginning
  restart() {
    this.scoreP1 = 0;
    this.scoreP2 = 0;
    this.timeRemaining = 67;
    this.isGameOver = false;
    this.isScoring = false;
    this.scoreMessage = '';
    this.lastTime = millis();

    player1.reset(280);
    player2.reset(width - 280);
    ball.reset();
  }

  // Draw UI, scoreboard, and game over screen
  drawScoreboard() {
    push();
    textAlign(CENTER, CENTER);

    // Player 1 score display
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

    // Timer display
    fill(200);
    noStroke();
    textSize(10);
    text('TIME', 511, 88);

    // Format time into MM:SS
    let totalSeconds = Math.ceil(this.timeRemaining);
    let minutes = Math.floor(totalSeconds / 60);
    let seconds = totalSeconds % 60;

    let minuteString = minutes;
    if (minutes < 10) {
      minuteString = '0' + minutes;
    }

    let secondString = seconds;
    if (seconds < 10) {
      secondString = '0' + seconds;
    }

    let timeString = minuteString + ':' + secondString;

    // Red color when 10 seconds or less
    if (totalSeconds <= 10 && totalSeconds > 0) {
      fill(255, 60, 60);
    } else {
      fill(255);
    }
    stroke(20);
    strokeWeight(2);
    textSize(22);
    text(timeString, 511, 114);

    // Player 2 score display
    fill(255, 215, 0);
    noStroke();
    textSize(13);
    text('P2', 625, 88);

    fill(255);
    stroke(20);
    strokeWeight(2);
    textSize(30);
    text(this.scoreP2, 625, 116);

    // Goal scored banner
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

    // Bottom controls helper text
    fill(255);
    stroke(20);
    strokeWeight(2.5);
    textSize(13);
    text('P1: A, D, W   |   P2: Left, Right, Up arrows', width / 2, 675);

    // Game Over screen popup
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
      text('Press [Space] to restart', width / 2, height / 2 + 18);
    }

    pop();
  }
}

//TODO: Long distance shots = 3 points, close range shots = 2 points
