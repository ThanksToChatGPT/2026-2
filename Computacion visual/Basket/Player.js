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

    // Shot cooldown tracking (ready to shoot at start)
    this.lastShotTime = -SHOT_COOLDOWN_MS;
    this.prevShootDown = false;
  }

  // Check if player is on the ground
  isGrounded() {
    let nearFloor = this.body.position.y >= FLOOR_Y - this.radius - 4;
    let notMovingUp = this.body.velocity.y >= -1.0;
    return nearFloor && notMovingUp;
  }

  // Check if player is touching the ball
  isTouchingBall() {
    if (!ball || !ball.body) {
      return false;
    }
    let dx = this.body.position.x - ball.body.position.x;
    let dy = this.body.position.y - ball.body.position.y;
    let distSq = dx * dx + dy * dy;
    let maxTouchDistance = this.radius + ball.radius + 10;
    return distSq <= maxTouchDistance * maxTouchDistance;
  }

  // Shoot the ball towards the rival hoop (Body.applyForce)
  shoot() {
    if (!this.isGrounded() || !this.isTouchingBall()) {
      return;
    }

    let now = millis();
    if (now - this.lastShotTime < SHOT_COOLDOWN_MS) {
      return;
    }

    if (!ball || !ball.body || (game && (game.isScoring || game.isGameOver))) {
      return;
    }

    // Direction towards rival hoop (P1 targets right hoop, P2 targets left hoop)
    let rivalHoop = this.isP1 ? rightHoop : leftHoop;
    let targetX = (rivalHoop.backX + rivalHoop.frontX) / 2;
    let dirX = targetX >= ball.body.position.x ? 1 : -1;

    Body.applyForce(ball.body, ball.body.position, {
      x: dirX * SHOT_FORCE_X,
      y: SHOT_FORCE_Y
    });

    Body.setAngularVelocity(ball.body, 0);
    this.lastShotTime = now;

    // Register shot touch position for long distance calculation
    if (game) {
      game.registerBallTouch(this);
    }
  }

  update() {
    // Keep player upright
    Body.setAngle(this.body, 0);
    Body.setAngularVelocity(this.body, 0);

    let moveSpeed = 5.2;
    let jumpSpeed = -12.8;
    let horizontalVelocity = 0;

    if (this.isP1) {
      // Player 1 controls: A, D, W (Jump), S (Shot)
      if (keyIsDown(65)) { // A
        horizontalVelocity -= moveSpeed;
      }
      if (keyIsDown(68)) { // D
        horizontalVelocity += moveSpeed;
      }
      if (keyIsDown(87) && this.isGrounded()) { // W
        Body.setVelocity(this.body, { x: this.body.velocity.x, y: jumpSpeed });
      }

      let shootDown = keyIsDown(83); // S (Shot)
      if (shootDown && !this.prevShootDown) {
        this.shoot();
      }
      this.prevShootDown = shootDown;
    } else {
      // Player 2 controls: Arrow keys (Down arrow = Shot)
      if (keyIsDown(LEFT_ARROW)) {
        horizontalVelocity -= moveSpeed;
      }
      if (keyIsDown(RIGHT_ARROW)) {
        horizontalVelocity += moveSpeed;
      }
      if (keyIsDown(UP_ARROW) && this.isGrounded()) {
        Body.setVelocity(this.body, { x: this.body.velocity.x, y: jumpSpeed });
      }

      let shootDown = keyIsDown(DOWN_ARROW); // Down arrow = Shot
      if (shootDown && !this.prevShootDown) {
        this.shoot();
      }
      this.prevShootDown = shootDown;
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
    this.lastShotTime = -SHOT_COOLDOWN_MS;
    this.prevShootDown = false;
  }
}

