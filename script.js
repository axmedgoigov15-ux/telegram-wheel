const canvas = document.getElementById("wheel");
const ctx = canvas.getContext("2d");

const sections = ["100", "200", "300", "LOSE", "500", "TRY AGAIN"];
const colors = ["#f44336", "#ff9800", "#ffeb3b", "#4caf50", "#2196f3", "#9c27b0"];

let angle = 0;

function drawWheel() {
  const slice = 2 * Math.PI / sections.length;

  for (let i = 0; i < sections.length; i++) {
    ctx.beginPath();
    ctx.moveTo(150, 150);
    ctx.arc(150, 150, 140, angle + i * slice, angle + (i + 1) * slice);
    ctx.fillStyle = colors[i];
    ctx.fill();

    ctx.save();
    ctx.translate(150, 150);
    ctx.rotate(angle + (i + 0.5) * slice);
    ctx.fillStyle = "#000";
    ctx.font = "16px Arial";
    ctx.fillText(sections[i], 60, 5);
    ctx.restore();
  }
}

function spin() {
  let spinAngle = Math.random() * 2000 + 2000;
  let start = null;

  function animate(timestamp) {
    if (!start) start = timestamp;
    const progress = timestamp - start;
    angle += 0.05;
    ctx.clearRect(0, 0, 300, 300);
    drawWheel();

    if (progress < spinAngle) {
      requestAnimationFrame(animate);
    }
  }

  requestAnimationFrame(animate);
}

drawWheel();
