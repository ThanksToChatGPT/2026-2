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

