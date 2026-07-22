fetch("news.json")
  .then(response => response.json())
  .then(news => {
    const container = document.getElementById("home-news");

    if (!container) return;

    container.innerHTML = "";

    news.forEach(item => {
      container.innerHTML += `
        <div class="news-card">
          ${item.image ? `<img src="${item.image}" alt="${item.title}" class="news-image">` : ""}
          <h3>${item.title}</h3>
<small>${item.date}</small>
<p>${item.summary}</p>
<p><a href="${item.link}" target="_blank">Read Full Story →</a></p>
        </div>
      `;
    });
  });