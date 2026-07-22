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
  fetch("concerts.json")
  .then(response => response.json())
  .then(concerts => {
    const concertList = document.getElementById("concert-list");

    if (!concertList) return;

    concertList.innerHTML = "";

    concerts.forEach(concert => {
      concertList.innerHTML += `
        <div class="concert-card">
          <h3>${concert.city} ${concert.country}</h3>
          <p><strong>Date:</strong> ${concert.date}</p>
          <p><strong>Venue:</strong> ${concert.venue}</p>
        </div>
      `;
    });
  })
  .catch(error => console.error(error));