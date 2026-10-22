// Matter.js objects
let Engine = Matter.Engine;
let Bodies = Matter.Bodies;
let Body = Matter.Body;
let Events = Matter.Events;
let Composite = Matter.Composite;

// Canvas and court dimensions
let CANVAS_WIDTH = 1024;
let CANVAS_HEIGHT = 696;
let FLOOR_Y = 606; // Height where players walk

// Shot physics and cooldown constants (hard to tune)
let SHOT_COOLDOWN_MS = 5000;
let SHOT_FORCE_X = 0.020;
let SHOT_FORCE_Y = -0.040;

// Image assets
let bgImg = new Image();
bgImg.src = 'Background.png';

let p1Img = new Image();
p1Img.src = 'Curry.png';

let p2Img = new Image();
p2Img.src = 'Lebron.png';

let hoopImg = new Image();
hoopImg.src = 'Hoop.png';

// Global variables for game entities
let engine;
let player1;
let player2;
let ball;
let leftHoop;
let rightHoop;
let game;

