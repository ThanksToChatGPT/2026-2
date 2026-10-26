// Inspired on https://www.miniplay.com/game/sports-heads-basketball
// Summary of changes:
// - Modularized: split codebase into constants.js, Ball.js, Hoop.js, Player.js, and Game.js
// - Unified trampoline bounce: handled purely via Matter.js collisions (removed duplicate position checks)
// - Added ball-player touch tracking (checkBallPlayerCollision) for 2-pt vs 3-pt shot calculations
// - Resolved orphaned goal reset timeouts on match restart
// - Added player reset on goal

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
  drawingContext.drawImage(bgImg, 0, 0, width, height);
  

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

    // Track ball touches by players
    checkBallPlayerCollision(bodyA, bodyB);

    // Check trampoline collision
    checkTrampolineHit(bodyA, bodyB);

    // Check goal sensor collision
    checkGoalSensorHit(bodyA, bodyB);
  }
}

// Track player contact with the ball
function checkBallPlayerCollision(bodyA, bodyB) {
  if (!ball || !ball.body || !game) {
    return;
  }

  let isBallA = (bodyA === ball.body);
  let isBallB = (bodyB === ball.body);
  if (!isBallA && !isBallB) {
    return;
  }

  let otherBody = isBallA ? bodyB : bodyA;
  if (player1 && otherBody === player1.body) {
    game.registerBallTouch(player1);
  } else if (player2 && otherBody === player2.body) {
    game.registerBallTouch(player2);
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

  // If a player touches the trampoline
  if ((player1 && otherBody === player1.body) || (player2 && otherBody === player2.body)) {
    if (otherBody.velocity.y >= -2) {
      Body.setVelocity(otherBody, { x: otherBody.velocity.x, y: -15 });
    }
  }

  // If the ball touches the trampoline
  if (otherBody === ball.body) {
    let currentYVelocity = ball.body.velocity.y;
    let bouncePower = 15;
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
