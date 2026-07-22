fetch("news.json")
  .then(response => response.json())
  .then(news => {

    const newsContainer = document.getElementById("news-container");
    const homeContainer = document.getElementById("home-news");

    function render(container, articles, limit = articles.length) {
      if (!container) return;

      container.innerHTML = "";

      articles.slice(0, limit).forEach(article => {

        const item = document.createElement("div");

        item.className = "news-card";

        item.innerHTML = `
          <h3>${article.title}</h3>
          <p>${article.published}</p>
          <a href="${article.link}" target="_blank">
            Read Full Article
          </a>
        `;

        container.appendChild(item);

      });
    }

    render(newsContainer, news);
    render(homeContainer, news, 3);

  })
  .catch(() => {

    if (document.getElementById("news-container"))
      document.getElementById("news-container").innerHTML =
        "<p>Unable to load news.</p>";

    if (document.getElementById("home-news"))
      document.getElementById("home-news").innerHTML =
        "<p>Unable to load news.</p>";

  });