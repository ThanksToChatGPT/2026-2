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
    this.lastTouchX = null; // Stores directly the X position of the last player who touched the ball
    this.goalTimeout = null; // Tracks pending goal reset timer to prevent orphaned timeouts
  }

  // Register X position of the last player who touched the ball
  registerBallTouch(player) {
    if (!player || !player.body) {
      return;
    }
    this.lastTouchX = player.body.position.x;
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
    } else {
      // Press Spacebar to restart game
      if (keyIsDown(32)) {
        this.restart();
      }
    }
  }

  // Trigger goal scored (long distance = 3 points, close range = 2 points)
  handleGoal(isRightHoop) {
    if (this.isScoring || this.isGameOver) {
      return;
    }

    this.isScoring = true;

    // Long distance: last touch behind midcourt A and basket in B, or vice versa
    let midX = width / 2;
    let isLong = false;

    if (this.lastTouchX !== null) {
      if (isRightHoop && this.lastTouchX < midX) {
        // Cesta en B (derecha), último toque en A (izquierda)
        isLong = true;
      } else if (!isRightHoop && this.lastTouchX > midX) {
        // Cesta en A (izquierda), último toque en B (derecha)
        isLong = true;
      }
    }

    let points = isLong ? 3 : 2;

    // Add points and set message
    if (isRightHoop) {
      this.scoreP1 += points;
      this.scoreMessage = isLong ? 'P1 SCORED! (+3)' : 'P1 SCORED! (+2)';
    } else {
      this.scoreP2 += points;
      this.scoreMessage = isLong ? 'P2 SCORED! (+3)' : 'P2 SCORED! (+2)';
    }

    // Cancel any previous pending goal timeout
    if (this.goalTimeout) {
      clearTimeout(this.goalTimeout);
    }

    // Reset players and ball after 1 second
    let self = this;
    this.goalTimeout = setTimeout(function() {
      player1.reset(280);
      player2.reset(width - 280);
      ball.reset();
      self.lastTouchX = null;
      self.scoreMessage = '';
      self.isScoring = false;
      self.goalTimeout = null;
    }, 1000);
  }

  // Restart match from beginning
  restart() {
    // Clear any orphaned timeout from goal reset
    if (this.goalTimeout) {
      clearTimeout(this.goalTimeout);
      this.goalTimeout = null;
    }

    this.scoreP1 = 0;
    this.scoreP2 = 0;
    this.timeRemaining = 67;
    this.isGameOver = false;
    this.isScoring = false;
    this.scoreMessage = '';
    this.lastTouchX = null;
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
    text('P1: A, D (Mover), W (Saltar), S (Tiro)   |   P2: Flechas (← → Mover, ↑ Saltar, ↓ Tiro)', width / 2, 675);

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
