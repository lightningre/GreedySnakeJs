var c = document.getElementById("myCanvas");
var ctx = c.getContext("2d");
ctx.fillStyle = "#FF0000";
var snakes = new Array();
var snakeNodeNew;

ctx.fillRect(20 + 10 * 20, 20, 19, 20);
ctx.fillRect(20 + 20 * 20, 200, 19, 20);
ctx.fillRect(20 + 10 * 20, 300, 19, 20);


for (let i = 0; i < 10; i++) {
  if (i == 9) { ctx.fillStyle = "#00FF00" };
  ctx.fillRect(20 + i * 20, 0, 19, 20);
  snakes.push({
    x: 10 + i * 20,
    y: 0,
    w: 19,
    h: 19
  })
}
document.getElementById("codes").innerText = "Hello Snake Man !";

var myVar;

function myStartFunction() {
  myVar = setInterval(mainFunc, 500);
  console.log("Start...")
}

function mainFunc() {
  if (snakes.slice(-2, -1)[0].y != snakes.slice(-1)[0].y) {
    if (snakes.slice(-2, -1)[0].y < snakes.slice(-1)[0].y) {
      snakeNodeNew = {
        x: snakes.slice(-1)[0].x,
        y: snakes.slice(-1)[0].y + snakes.slice(-1)[0].h,
        w: 19,
        h: 19
      }
    } else {
      snakeNodeNew = {
        x: snakes.slice(-1)[0].x,
        y: snakes.slice(-1)[0].y - snakes.slice(-1)[0].h,
        w: 19,
        h: 19
      }
    }
  } else {
    if (snakes.slice(-2, -1)[0].x < snakes.slice(-1)[0].x) {
      snakeNodeNew = {
        x: snakes.slice(-1)[0].x + snakes.slice(-1)[0].w,
        y: snakes.slice(-1)[0].y,
        w: 19,
        h: 19
      }
    } else {
      snakeNodeNew = {
        x: snakes.slice(-1)[0].x - snakes.slice(-1)[0].w,
        y: snakes.slice(-1)[0].y,
        w: 19,
        h: 19
      }
    }
  }
  if (!snakes.map((item) => {
    return JSON.stringify(item)
  }).includes(JSON.stringify(snakeNodeNew))) {
    var imgData = ctx.getImageData(snakeNodeNew.x, snakeNodeNew.y, snakeNodeNew.w, snakeNodeNew.h);
    if (imgData.data[0] === 255) snakes.push(snakeNodeNew);
    else {
      snakes.shift();
      snakes.push(snakeNodeNew);
    }
  }
  ctx.clearRect(0, 0, 500, 500);
  for (let snake of snakes) {
    if (snake === snakes.slice(-1)[0]) {
      ctx.fillStyle = "#FF0000";
      ctx.fillRect(snake.x, snake.y, 18, 18);
    } else {
      ctx.fillStyle = "#00FF00";
      ctx.fillRect(snake.x, snake.y, 18, 18);
    }
  }
}

function myStopFunction() {
  clearInterval(myVar);
  console.log("Stop...")
}

document.addEventListener("keydown", (e) => {
  switch (e.which) {
    case 38:
      snakeNodeNew = {
        x: snakes.slice(-1)[0].x,
        y: snakes.slice(-1)[0].y - snakes.slice(-1)[0].h,
        w: 19,
        h: 19
      }
      break;
    case 39:
      snakeNodeNew = {
        x: snakes.slice(-1)[0].x + snakes.slice(-1)[0].w,
        y: snakes.slice(-1)[0].y,
        w: 19,
        h: 19
      }
      break;
    case 37:
      snakeNodeNew = {
        x: snakes.slice(-1)[0].x - snakes.slice(-1)[0].w,
        y: snakes.slice(-1)[0].y,
        w: 19,
        h: 19
      }
      break;
    case 40:
      snakeNodeNew = {
        x: snakes.slice(-1)[0].x,
        y: snakes.slice(-1)[0].y + snakes.slice(-1)[0].h,
        w: 19,
        h: 19
      }
      break;
    case 32:
      myStopFunction()
      break;
  }
  if (!snakes.map((item) => {
    return JSON.stringify(item)
  }).includes(JSON.stringify(snakeNodeNew))) {
    snakes.shift();
    snakes.push(snakeNodeNew);
  }
  document.getElementById("codes").innerText = "Hello Snake Man ! keycode:" + e.which.toString();
  ctx.clearRect(0, 0, 500, 500);
  for (let snake of snakes) {
    if (snake === snakes.slice(-1)[0]) {
      ctx.fillStyle = "#FF0000";
      ctx.fillRect(snake.x, snake.y, 18, 18);
    } else {
      ctx.fillStyle = "#00FF00";
      ctx.fillRect(snake.x, snake.y, 18, 18);
    }
  }

})
