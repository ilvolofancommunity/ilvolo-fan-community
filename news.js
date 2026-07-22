fetch("news.json")
  .then(response => response.json())
  .then(news => {
    const container = document.getElementById("news-container");
    container.innerHTML = "";

    news.forEach(article => {
      const item = document.createElement("div");

      item.innerHTML = `
        <h2>${article.title}</h2>
        <p>${article.published}</p>
        <a href="${article.link}" target="_blank">Read Full Article</a>
        <hr>
      `;

      container.appendChild(item);
    });
  })
  .catch(error => {
    document.getElementById("news-container").innerHTML =
      "<p>Unable to load the latest news.</p>";
    console.error(error);
  });
