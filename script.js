fetch("news.json")
  .then(response => response.json())
  .then(news => {
    const homeNews = document.getElementById("home-news");
    if (!homeNews) return;

    homeNews.innerHTML = "";

    news.slice(0, 3).forEach(item => {
      homeNews.innerHTML += `
        <div class="news-card">
          <img src="${item.image}" alt="IL VOLO News">
          <h3>${item.title}</h3>
          <small>${item.date}</small>
          <p>${item.summary}</p>
          <a href="${item.link}" target="_blank">Read Full Story →</a>
        </div>
      `;
    });
  })
  .catch(error => {
    console.error(error);
    const homeNews = document.getElementById("home-news");
    if (homeNews) {
      homeNews.innerHTML = "<p>Unable to load the latest news.</p>";
    }
  });