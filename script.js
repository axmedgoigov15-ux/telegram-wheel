const canvas = document.getElementById("wheel");
const ctx = canvas.getContext("2d");

const sections = ["LOSE", "LOSE", "LOSE", "LOSE", "LOSE", "JACKPOT"];
const colors = ["#444", "#555", "#666", "#777", "#888", "#ff0000"];

let angle = 0;

function drawWheel() {
  const slice = 2 * Math.PI / sections.length;
  ctx.clearRect(0, 0, 300, 300);

  for (let i = 0; i < sections.length; i++) {
    ctx.beginPath();
    ctx.moveTo(150, 150);
    ctx.arc(150, 150, 140, angle + i * slice, angle + (i + 1) * slice);
    ctx.fillStyle = colors[i];
    ctx.fill();

    ctx.save();
    ctx.translate(150, 150);
    ctx.rotate(angle + (i + 0.5) * slice);
    ctx.fillStyle = "#fff";
    ctx.font = "14px Arial";
    ctx.fillText(sections[i], 60, 5);
    ctx.restore();
  }
}

function spin() {
  let duration = 3000;
  let start = null;

  function animate(ts) {
    if (!start) start = ts;
    let progress = ts - start;

    angle += 0.08;
    drawWheel();

    if (progress < duration) {
      requestAnimationFrame(animate);
    } else {
      // 🎯 шанс 1 на 1 000 000 000
      const isWin = Math.random() < 0.000000001;
      const result = isWin ? "JACKPOT" : "LOSE";

      document.getElementById("text").innerText =
        result === "JACKPOT"
          ? "🎉 ДЖЕКПОТ! Заявка отправлена"
          : "❌ Не повезло";

      if (window.Telegram?.WebApp) {
        Telegram.WebApp.sendData(JSON.stringify({
          result: result
        }));
      }
    }
  }

  requestAnimationFrame(animate);
}

window.onload = spin;
