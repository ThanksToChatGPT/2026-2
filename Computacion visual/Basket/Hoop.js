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

    // Score sensor inside the rim
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

