let angle = 0;

function spin() {
  angle += 720 + Math.random() * 360;
  document.getElementById("wheel").style.transform =
    `rotate(${angle}deg)`;
}
