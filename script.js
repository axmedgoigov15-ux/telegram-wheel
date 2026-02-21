let angle = 0;

function spin() {
  angle += 720 + Math.random() * 360;
  document.getElementById("wheel").style.transform =
    `rotate(${angle}deg)`;

  setTimeout(() => {
    const prize = Math.floor(Math.random() * 100);
    document.getElementById("text").innerText =
      "Результат: " + prize;

    // отправка результата в Telegram
    if (window.Telegram) {
      Telegram.WebApp.sendData(JSON.stringify({
        prize: prize
      }));
    }
  }, 2000);
}

// автозапуск
window.onload = spin;
