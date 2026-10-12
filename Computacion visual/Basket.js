/**
 * ====================================================================
 * SPORTS HEADS: BASKETBALL 1v1 - CURRY VS LEBRON
 * ====================================================================
 * Stack: p5.js + Matter.js
 * 
 * - Fondo: Background.png (1024 x 696) con estadio, público, marcador y cancha.
 * - Línea de la cancha: y = 606 (los jugadores se desplazan sobre esta línea,
 *   justo encima de la zona azul inferior).
 * - Personajes:
 *   - Jugador 1 (Izquierda): Stephen Curry (Curry.png)
 *   - Jugador 2 (Derecha): LeBron James (Lebron.png) - Volteado horizontalmente
 * - Aros y postes: Anclados a las paredes laterales con barreras invisibles
 *   que impiden el paso bajo la canasta.
 */

// Desestructuración de módulos de Matter.js
const {
  Engine,
  World,
  Bodies,
  Body,
  Events,
  Composite
} = Matter;

// ====================================================================
// CONSTANTES GLOBALES Y DIMENSIONES
// ====================================================================
// Dimensiones exactas según Background.png
const CANVAS_WIDTH  = 1024;
const CANVAS_HEIGHT = 696;

// En Background.png, la línea inferior de la cancha de madera está en y = 606.
// Por debajo (y = 606 a 696) se encuentra la zona azul del suelo.
const FLOOR_Y       = 606;

// Altura del aro (media-alta sobre la cancha)
const HOOP_Y        = 340;

// Dimensiones de las físicas
const PLAYER_RADIUS = 44;   // Radio físico de la cabeza/cuerpo
const BALL_RADIUS   = 18;   // Balón de baloncesto
const MOVE_SPEED    = 5.2;  // Velocidad de desplazamiento horizontal
const JUMP_FORCE    = -12.8;// Impulso de salto (flotante y controlado)

// Bounding box del contenido no transparente en los sprites originales (2400x1792)
const SPRITE_DATA = {
  curry:  { sx: 644, sy: 20, sw: 1072, sh: 1752 },
  lebron: { sx: 644, sy: 24, sw: 1080, sh: 1748 }
};

// Altura y anchura calculadas de renderizado para los personajes
const CHAR_RENDER_H = 108;
const CHAR_RENDER_W = 66;

// Categorías de colisión para Matter.js (bitmasks)
const CAT_DEFAULT = 0x0001; // Límites (suelo, techo, paredes)
const CAT_PLAYER  = 0x0002; // Jugadores
const CAT_BALL    = 0x0004; // Balón
const CAT_HOOP    = 0x0008; // Bordes físicos del aro
const CAT_BARRIER = 0x0010; // Barreras bloqueadas bajo el aro

// ====================================================================
// RECURSOS GRÁFICOS Y VARIABLES DE ESTADO
// ====================================================================
let bgImg;
let curryImg;
let lebronImg;

let engine;
let world;

// Entidades físicas
let player1, player2;
let ball;
let hoopLeft, hoopRight;
let barrierLeft, barrierRight;
let floorBody, ceilBody, wallLeftBody, wallRightBody;

// Estado del partido y marcador
let scoreP1 = 0;
let scoreP2 = 0;
let isScoring = false;
let scoreMessage = '';

// ====================================================================
// CARGA ROBUSTA DE IMÁGENES (Compatible con file:/// y servidores locales)
// ====================================================================
let bgReady = false;
let curryReady = false;
let lebronReady = false;

const nativeBg = new Image();
const nativeCurry = new Image();
const nativeLebron = new Image();

function initImages() {
  nativeBg.onload = () => { bgReady = true; };
  nativeBg.src = 'Background.png';

  nativeCurry.onload = () => { curryReady = true; };
  nativeCurry.src = 'Curry.png';

  nativeLebron.onload = () => { lebronReady = true; };
  nativeLebron.src = 'Lebron.png';
}

// ====================================================================
// SETUP: INICIALIZACIÓN
// ====================================================================
function setup() {
  const canvas = createCanvas(CANVAS_WIDTH, CANVAS_HEIGHT);
  canvas.parent('game-container');

  // Inicializar carga de recursos (imágenes de fondo y jugadores)
  initImages();

  // 1. Motor de físicas con ritmo pausado y flotante
  engine = Engine.create();
  world = engine.world;
  engine.gravity.y = 0.65;
  engine.gravity.scale = 0.001;

  // 2. Límites sólidos (Piso en la línea de la cancha y = 606)
  createBoundaries();

  // 3. Aros anclados a las paredes y barreras bajo los aros
  createHoops();

  // 4. Jugadores (Curry y LeBron)
  createPlayers();

  // 5. Balón
  createBall();

  // 6. Detector de canastas
  setupScoreListener();

  // Prevenir scroll de la página con flechas o barra espaciadora
  window.addEventListener('keydown', (e) => {
    if (['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight', ' '].includes(e.key)) {
      e.preventDefault();
    }
  });
}

// ====================================================================
// DRAW: BUCLE PRINCIPAL DE JUEGO
// ====================================================================
function draw() {
  // 1. Controles de jugadores
  handlePlayerInputs();

  // 2. Paso de físicas de Matter.js
  Engine.update(engine, 1000 / 60);

  // 3. Forzar bloqueo estricto de rotación para mantener erguidos a los personajes
  Body.setAngle(player1, 0);
  Body.setAngularVelocity(player1, 0);
  Body.setAngle(player2, 0);
  Body.setAngularVelocity(player2, 0);

  // 4. Renderizado en capas
  drawBackground();
  drawHoop(hoopLeft, true);
  drawHoop(hoopRight, false);
  drawPlayer(player1, 'CURRY', true);
  drawPlayer(player2, 'LEBRON', false);
  drawBall(ball);
  drawScoreboard();
}

// ====================================================================
// CREACIÓN DE ENTIDADES FÍSICAS (MATTER.JS)
// ====================================================================

/**
 * Crea las paredes, el techo y el suelo sólido ubicado en la línea de la cancha (y = 606).
 */
function createBoundaries() {
  const wallThickness = 60;

  // Suelo: Su cara superior queda exactamente en FLOOR_Y (606)
  floorBody = Bodies.rectangle(width / 2, FLOOR_Y + wallThickness / 2, width * 2, wallThickness, {
    isStatic: true,
    restitution: 0.6,
    friction: 0.1,
    collisionFilter: {
      category: CAT_DEFAULT,
      mask: CAT_PLAYER | CAT_BALL
    }
  });

  // Techo
  ceilBody = Bodies.rectangle(width / 2, -wallThickness / 2, width * 2, wallThickness, {
    isStatic: true,
    restitution: 0.5,
    collisionFilter: {
      category: CAT_DEFAULT,
      mask: CAT_PLAYER | CAT_BALL
    }
  });

  // Pared izquierda
  wallLeftBody = Bodies.rectangle(-wallThickness / 2, height / 2, wallThickness, height * 2, {
    isStatic: true,
    restitution: 0.7,
    friction: 0.05,
    collisionFilter: {
      category: CAT_DEFAULT,
      mask: CAT_PLAYER | CAT_BALL
    }
  });

  // Pared derecha
  wallRightBody = Bodies.rectangle(width + wallThickness / 2, height / 2, wallThickness, height * 2, {
    isStatic: true,
    restitution: 0.7,
    friction: 0.05,
    collisionFilter: {
      category: CAT_DEFAULT,
      mask: CAT_PLAYER | CAT_BALL
    }
  });

  Composite.add(world, [floorBody, ceilBody, wallLeftBody, wallRightBody]);
}

/**
 * Crea los aros izquierdo y derecho pegados a las paredes y sus barreras bloqueadas inferiores.
 */
function createHoops() {
  const rimPinRadius = 6;
  const rimSpan = 75;            // Apertura amplia y limpia para el balón (diámetro 36)
  const hoopDepthFromWall = 25;  // Distancia del pin posterior anclado a la pared

  // ----------------------------------------------------
  // ARO IZQUIERDO (Canasta defendida por Curry)
  // ----------------------------------------------------
  const leftBackX  = hoopDepthFromWall;
  const leftFrontX = hoopDepthFromWall + rimSpan; // x = 100

  // Pin soporte de pared
  const leftPinBack = Bodies.circle(leftBackX, HOOP_Y, rimPinRadius, {
    isStatic: true,
    restitution: 0.75,
    friction: 0.05,
    collisionFilter: { category: CAT_HOOP, mask: CAT_PLAYER | CAT_BALL }
  });

  // Pin frontal del aro
  const leftPinFront = Bodies.circle(leftFrontX, HOOP_Y, rimPinRadius, {
    isStatic: true,
    restitution: 0.75,
    friction: 0.05,
    collisionFilter: { category: CAT_HOOP, mask: CAT_PLAYER | CAT_BALL }
  });

  // Sensor de anotación
  const leftSensor = Bodies.rectangle((leftBackX + leftFrontX) / 2, HOOP_Y + 14, rimSpan - 14, 10, {
    isStatic: true,
    isSensor: true,
    collisionFilter: { category: CAT_HOOP, mask: CAT_BALL }
  });

  hoopLeft = {
    pinBack: leftPinBack,
    pinFront: leftPinFront,
    sensor: leftSensor,
    side: 'left'
  };

  // Barrera estática invisible desde la base del aro hasta el suelo
  // Bloquea x de 0 a 100, impidiendo que jugadores o balón entren bajo la canasta
  const leftBarrierWidth  = leftFrontX;
  const leftBarrierHeight = FLOOR_Y - (HOOP_Y + 28);
  const leftBarrierY      = (HOOP_Y + 28) + leftBarrierHeight / 2;

  barrierLeft = Bodies.rectangle(leftBarrierWidth / 2, leftBarrierY, leftBarrierWidth, leftBarrierHeight, {
    isStatic: true,
    restitution: 0.5,
    friction: 0.1,
    collisionFilter: {
      category: CAT_BARRIER,
      mask: CAT_PLAYER | CAT_BALL
    }
  });

  // ----------------------------------------------------
  // ARO DERECHO (Canasta defendida por LeBron)
  // ----------------------------------------------------
  const rightBackX  = width - hoopDepthFromWall;
  const rightFrontX = width - (hoopDepthFromWall + rimSpan); // x = 924

  // Pin soporte de pared
  const rightPinBack = Bodies.circle(rightBackX, HOOP_Y, rimPinRadius, {
    isStatic: true,
    restitution: 0.75,
    friction: 0.05,
    collisionFilter: { category: CAT_HOOP, mask: CAT_PLAYER | CAT_BALL }
  });

  // Pin frontal del aro
  const rightPinFront = Bodies.circle(rightFrontX, HOOP_Y, rimPinRadius, {
    isStatic: true,
    restitution: 0.75,
    friction: 0.05,
    collisionFilter: { category: CAT_HOOP, mask: CAT_PLAYER | CAT_BALL }
  });

  // Sensor de anotación
  const rightSensor = Bodies.rectangle((rightBackX + rightFrontX) / 2, HOOP_Y + 14, rimSpan - 14, 10, {
    isStatic: true,
    isSensor: true,
    collisionFilter: { category: CAT_HOOP, mask: CAT_BALL }
  });

  hoopRight = {
    pinBack: rightPinBack,
    pinFront: rightPinFront,
    sensor: rightSensor,
    side: 'right'
  };

  // Barrera estática invisible derecha
  const rightBarrierWidth  = width - rightFrontX;
  const rightBarrierHeight = FLOOR_Y - (HOOP_Y + 28);
  const rightBarrierY      = (HOOP_Y + 28) + rightBarrierHeight / 2;

  barrierRight = Bodies.rectangle(width - rightBarrierWidth / 2, rightBarrierY, rightBarrierWidth, rightBarrierHeight, {
    isStatic: true,
    restitution: 0.5,
    friction: 0.1,
    collisionFilter: {
      category: CAT_BARRIER,
      mask: CAT_PLAYER | CAT_BALL
    }
  });

  Composite.add(world, [
    leftPinBack, leftPinFront, leftSensor, barrierLeft,
    rightPinBack, rightPinFront, rightSensor, barrierRight
  ]);
}

/**
 * Crea a Curry y LeBron como cuerpos circulares pesados con rotación bloqueada.
 */
function createPlayers() {
  const playerOptions = {
    restitution: 0.05,
    friction: 0.1,
    frictionAir: 0.04,   // Fricción de aire para saltos deportivos controlados
    density: 0.015,      // Masa significativamente mayor a la del balón
    inertia: Infinity,   // Bloqueo físico estricto de rotación
    inverseInertia: 0,
    collisionFilter: {
      category: CAT_PLAYER,
      mask: CAT_DEFAULT | CAT_BALL | CAT_HOOP | CAT_BARRIER | CAT_PLAYER
    }
  };

  // Jugador 1 (Curry): empieza en x = 280 sobre la línea de la cancha
  player1 = Bodies.circle(280, FLOOR_Y - PLAYER_RADIUS, PLAYER_RADIUS, playerOptions);

  // Jugador 2 (LeBron): empieza en x = 744 sobre la línea de la cancha
  player2 = Bodies.circle(width - 280, FLOOR_Y - PLAYER_RADIUS, PLAYER_RADIUS, playerOptions);

  Composite.add(world, [player1, player2]);
}

/**
 * Crea el balón elástico y ligero.
 */
function createBall() {
  const ballOptions = {
    restitution: 0.82,     // Rebote elástico marcado
    friction: 0.03,        // Fricción baja
    frictionAir: 0.007,    // Fricción suave para parábolas aerodinámicas
    density: 0.0008,       // Ligero para rebotar contra los jugadores
    collisionFilter: {
      category: CAT_BALL,
      mask: CAT_DEFAULT | CAT_PLAYER | CAT_HOOP | CAT_BARRIER
    }
  };

  // Se genera en el centro para el saque inicial
  ball = Bodies.circle(width / 2, 230, BALL_RADIUS, ballOptions);
  Composite.add(world, ball);
}

// ====================================================================
// CONTROLES DE LOS JUGADORES
// ====================================================================

/**
 * Verifica si un jugador está tocando el suelo o la cabeza del rival para autorizar el salto.
 */
function isPlayerGrounded(player) {
  // Comprobación sobre el suelo: cota del piso y no en plena aceleración ascendente
  const touchingFloor = (player.position.y >= FLOOR_Y - PLAYER_RADIUS - 4) && (player.velocity.y >= -1.0);
  if (touchingFloor) return true;

  // Comprobación sobre la cabeza del otro jugador
  const otherPlayer = (player === player1) ? player2 : player1;
  const dx = Math.abs(player.position.x - otherPlayer.position.x);
  const dy = player.position.y - otherPlayer.position.y;
  const onTopOfOpponent = (dx < PLAYER_RADIUS * 1.5) && (dy < -PLAYER_RADIUS * 1.4) && (dy > -PLAYER_RADIUS * 2.2) && (player.velocity.y >= -1.0);

  return onTopOfOpponent;
}

/**
 * Gestiona el movimiento y salto de Curry y LeBron.
 */
function handlePlayerInputs() {
  // ----------------------------------------------------
  // CURRY (P1 - Izquierda): A / D para mover, W para saltar
  // ----------------------------------------------------
  let p1SpeedX = 0;
  if (keyIsDown(65)) { // A: Izquierda
    p1SpeedX -= MOVE_SPEED;
  }
  if (keyIsDown(68)) { // D: Derecha
    p1SpeedX += MOVE_SPEED;
  }

  if (p1SpeedX !== 0) {
    Body.setVelocity(player1, { x: p1SpeedX, y: player1.velocity.y });
  } else {
    Body.setVelocity(player1, { x: player1.velocity.x * 0.85, y: player1.velocity.y });
  }

  if (keyIsDown(87) && isPlayerGrounded(player1)) { // W: Salto
    Body.setVelocity(player1, { x: player1.velocity.x, y: JUMP_FORCE });
  }

  // ----------------------------------------------------
  // LEBRON (P2 - Derecha): Flechas Izq / Der para mover, Flecha Arriba para saltar
  // ----------------------------------------------------
  let p2SpeedX = 0;
  if (keyIsDown(LEFT_ARROW)) { // Flecha Izquierda
    p2SpeedX -= MOVE_SPEED;
  }
  if (keyIsDown(RIGHT_ARROW)) { // Flecha Derecha
    p2SpeedX += MOVE_SPEED;
  }

  if (p2SpeedX !== 0) {
    Body.setVelocity(player2, { x: p2SpeedX, y: player2.velocity.y });
  } else {
    Body.setVelocity(player2, { x: player2.velocity.x * 0.85, y: player2.velocity.y });
  }

  if (keyIsDown(UP_ARROW) && isPlayerGrounded(player2)) { // Flecha Arriba: Salto
    Body.setVelocity(player2, { x: player2.velocity.x, y: JUMP_FORCE });
  }
}

// ====================================================================
// LÓGICA DE CANASTA Y PARTIDO
// ====================================================================

/**
 * Escucha las colisiones con el sensor interior del aro.
 */
function setupScoreListener() {
  Events.on(engine, 'collisionStart', (event) => {
    if (isScoring) return;

    const pairs = event.pairs;
    for (let i = 0; i < pairs.length; i++) {
      const { bodyA, bodyB } = pairs[i];

      let targetHoop = null;
      let targetBall = null;

      if (bodyA === hoopLeft.sensor && bodyB === ball) {
        targetHoop = 'left';
        targetBall = bodyB;
      } else if (bodyB === hoopLeft.sensor && bodyA === ball) {
        targetHoop = 'left';
        targetBall = bodyA;
      } else if (bodyA === hoopRight.sensor && bodyB === ball) {
        targetHoop = 'right';
        targetBall = bodyB;
      } else if (bodyB === hoopRight.sensor && bodyA === ball) {
        targetHoop = 'right';
        targetBall = bodyA;
      }

      // Validar que el balón atraviese el sensor de arriba hacia abajo (velocidad vertical > 0)
      if (targetHoop && targetBall && targetBall.velocity.y > 0.35) {
        handleGoal(targetHoop);
        break;
      }
    }
  });
}

/**
 * Procesa la anotación, actualiza el marcador y reinicia tras 1 segundo.
 */
function handleGoal(hoopSide) {
  isScoring = true;

  if (hoopSide === 'right') {
    // Balón entró en aro derecho -> Anota Curry (P1)
    scoreP1++;
    scoreMessage = '¡CANASTA DE CURRY! (+1)';
  } else if (hoopSide === 'left') {
    // Balón entró en aro izquierdo -> Anota LeBron (P2)
    scoreP2++;
    scoreMessage = '¡CANASTA DE LEBRON! (+1)';
  }

  // Pausa de 1 segundo antes de reiniciar el balón en el centro de la cancha
  setTimeout(() => {
    resetBall();
    scoreMessage = '';
    isScoring = false;
  }, 1000);
}

/**
 * Reposiciona el balón en el centro superior de la cancha.
 */
function resetBall() {
  Body.setPosition(ball, { x: width / 2, y: 230 });
  Body.setVelocity(ball, { x: 0, y: 0 });
  Body.setAngularVelocity(ball, 0);
  Body.setAngle(ball, 0);
}

// ====================================================================
// RENDERIZADO VISUAL (P5.JS)
// ====================================================================

/**
 * Dibuja Background.png a resolución nativa 1024 x 696.
 */
function drawBackground() {
  if (bgReady) {
    drawingContext.drawImage(nativeBg, 0, 0, width, height);
  } else if (bgImg && bgImg.width > 0) {
    image(bgImg, 0, 0, width, height);
  } else {
    // Fallback geométrico si la imagen aún no está disponible
    background(240);
    fill(255);
    stroke(30);
    strokeWeight(3);
    rect(0, FLOOR_Y, width, height - FLOOR_Y);
  }
}

/**
 * Dibuja a Curry o LeBron integrando su sprite con el calzado exactamente sobre FLOOR_Y (606).
 */
function drawPlayer(player, label, isPlayer1) {
  const ready = isPlayer1 ? curryReady : lebronReady;
  const nImg  = isPlayer1 ? nativeCurry : nativeLebron;
  const pImg  = isPlayer1 ? curryImg : lebronImg;
  const crop  = isPlayer1 ? SPRITE_DATA.curry : SPRITE_DATA.lebron;

  push();
  translate(player.position.x, player.position.y);

  if (!isPlayer1) {
    // Voltear horizontalmente a LeBron para que mire hacia Curry y hacia la cancha
    scale(-1, 1);
  }

  if (ready) {
    // Dibujo nativo recortado de alta precisión: la suela del calzado queda exactamente en +PLAYER_RADIUS
    drawingContext.drawImage(
      nImg,
      crop.sx, crop.sy, crop.sw, crop.sh,
      -CHAR_RENDER_W / 2, PLAYER_RADIUS - CHAR_RENDER_H, CHAR_RENDER_W, CHAR_RENDER_H
    );
  } else if (pImg && pImg.width > 0) {
    image(
      pImg,
      -CHAR_RENDER_W / 2,
      PLAYER_RADIUS - CHAR_RENDER_H,
      CHAR_RENDER_W,
      CHAR_RENDER_H,
      crop.sx,
      crop.sy,
      crop.sw,
      crop.sh
    );
  } else {
    // Placeholder geométrico de respaldo
    fill(255);
    stroke(30);
    strokeWeight(3);
    ellipse(0, 0, PLAYER_RADIUS * 2, PLAYER_RADIUS * 2);
  }

  pop();

  // Nombre del jugador sobre la cabeza (renderizado sin voltear para que el texto sea legible)
  push();
  textAlign(CENTER, CENTER);
  fill(255);
  stroke(20);
  strokeWeight(3);
  textSize(12);
  textStyle(BOLD);
  const labelY = player.position.y + PLAYER_RADIUS - CHAR_RENDER_H - 10;
  text(label, player.position.x, labelY);
  pop();
}

/**
 * Dibuja el balón de baloncesto con sus costuras rotando con el ángulo de físicas.
 */
function drawBall(ballBody) {
  push();
  translate(ballBody.position.x, ballBody.position.y);
  rotate(ballBody.angle);

  // Balón naranja clásico
  fill(245, 110, 30);
  stroke(30);
  strokeWeight(2.5);
  ellipse(0, 0, BALL_RADIUS * 2, BALL_RADIUS * 2);

  // Costuras negras del balón
  noFill();
  stroke(30);
  strokeWeight(1.8);
  line(-BALL_RADIUS, 0, BALL_RADIUS, 0);
  line(0, -BALL_RADIUS, 0, BALL_RADIUS);
  arc(-BALL_RADIUS * 0.45, 0, BALL_RADIUS, BALL_RADIUS * 1.8, -HALF_PI, HALF_PI);
  arc(BALL_RADIUS * 0.45, 0, BALL_RADIUS, BALL_RADIUS * 1.8, HALF_PI, -HALF_PI);

  pop();
}

/**
 * Dibuja el aro pegado a la pared, el tablero y la red.
 */
function drawHoop(hoop, isLeft) {
  push();

  // 1. Tablero de baloncesto anclado a la pared
  fill(255);
  stroke(30);
  strokeWeight(3);
  rectMode(CORNER);
  if (isLeft) {
    rect(0, HOOP_Y - 65, 18, 105);
    // Cuadro interior del tablero
    rect(3, HOOP_Y - 40, 12, 40);
  } else {
    rect(width - 18, HOOP_Y - 65, 18, 105);
    rect(width - 15, HOOP_Y - 40, 12, 40);
  }

  // 2. Red semitransparente de la canasta
  fill(255, 235);
  stroke(60);
  strokeWeight(1.5);
  beginShape();
  if (isLeft) {
    vertex(hoop.pinBack.position.x, hoop.pinBack.position.y);
    vertex(hoop.pinFront.position.x, hoop.pinFront.position.y);
    vertex(hoop.pinFront.position.x - 14, hoop.pinFront.position.y + 36);
    vertex(hoop.pinBack.position.x + 8, hoop.pinBack.position.y + 36);
  } else {
    vertex(hoop.pinBack.position.x, hoop.pinBack.position.y);
    vertex(hoop.pinFront.position.x, hoop.pinFront.position.y);
    vertex(hoop.pinFront.position.x + 14, hoop.pinFront.position.y + 36);
    vertex(hoop.pinBack.position.x - 8, hoop.pinBack.position.y + 36);
  }
  endShape(CLOSE);

  // Malla interior de la red
  stroke(130);
  strokeWeight(1);
  if (isLeft) {
    line(hoop.pinBack.position.x + 18, hoop.pinBack.position.y, hoop.pinFront.position.x - 24, hoop.pinFront.position.y + 36);
    line(hoop.pinFront.position.x - 18, hoop.pinFront.position.y, hoop.pinBack.position.x + 20, hoop.pinBack.position.y + 36);
  } else {
    line(hoop.pinBack.position.x - 18, hoop.pinBack.position.y, hoop.pinFront.position.x + 24, hoop.pinFront.position.y + 36);
    line(hoop.pinFront.position.x + 18, hoop.pinFront.position.y, hoop.pinBack.position.x - 20, hoop.pinBack.position.y + 36);
  }

  // 3. Aro metálico naranja
  fill(255, 85, 0);
  stroke(30);
  strokeWeight(3);
  line(hoop.pinBack.position.x, hoop.pinBack.position.y, hoop.pinFront.position.x, hoop.pinFront.position.y);
  ellipse(hoop.pinBack.position.x, hoop.pinBack.position.y, 11, 11);
  ellipse(hoop.pinFront.position.x, hoop.pinFront.position.y, 11, 11);

  pop();
}

/**
 * Renderiza el marcador digital integrado perfectamente en la estructura del marcador de Background.png,
 * el banner de canasta y los controles en la zona azul inferior.
 */
function drawScoreboard() {
  push();

  // ----------------------------------------------------
  // 1. MARCADOR EN EL TABLERO DEL ESTADIO (x: 323 a 705, y: 70 a 143)
  // ----------------------------------------------------
  textAlign(CENTER, CENTER);

  // Panel Izquierdo: CURRY (Panel en x = 398, y = 110)
  fill(255, 215, 0); // Amarillo Warriors
  noStroke();
  textSize(12);
  textStyle(BOLD);
  text('CURRY (P1)', 398, 88);

  fill(255);
  stroke(20);
  strokeWeight(2);
  textSize(30);
  textStyle(BOLD);
  text(scoreP1, 398, 116);

  // Panel Central: VS
  fill(200);
  noStroke();
  textSize(14);
  textStyle(BOLD);
  text('VS', 511, 110);

  // Panel Derecho: LEBRON (Panel en x = 625, y = 110)
  fill(255, 215, 0); // Oro Lakers
  noStroke();
  textSize(12);
  textStyle(BOLD);
  text('LEBRON (P2)', 625, 88);

  fill(255);
  stroke(20);
  strokeWeight(2);
  textSize(30);
  textStyle(BOLD);
  text(scoreP2, 625, 116);

  // ----------------------------------------------------
  // 2. BANNER DE CANASTA CUANDO SE ANOTA
  // ----------------------------------------------------
  if (isScoring && scoreMessage !== '') {
    rectMode(CENTER);
    fill(255);
    stroke(30);
    strokeWeight(3);
    rect(width / 2, 180, 360, 46, 8);

    fill(30);
    noStroke();
    textSize(20);
    textStyle(BOLD);
    text(scoreMessage, width / 2, 179);
  }

  // ----------------------------------------------------
  // 3. LEYENDA DE CONTROLES EN LA ZONA AZUL INFERIOR (y = 606 a 696)
  // ----------------------------------------------------
  fill(255);
  stroke(20);
  strokeWeight(2.5);
  textSize(13);
  textStyle(BOLD);
  text(
    'P1 (Curry): [A / D] Mover  [W] Salto   |   P2 (LeBron): [← / →] Mover  [↑] Salto',
    width / 2,
    675
  );

  pop();
}