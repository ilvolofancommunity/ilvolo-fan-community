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

    const today = new Date();

    today.setHours(0,0,0,0);

    const upcomingConcerts = concerts

      .filter(concert => {

        const concertDate = new Date(concert.dateISO);

        return concertDate >= today;

      })

      .sort((a,b)=>new Date(a.dateISO)-new Date(b.dateISO));

    if(upcomingConcerts.length===0){

      concertList.innerHTML=`

      <div class="concert-card">

      <h3>🎤 No Upcoming Concerts</h3>

      <p>Please check back soon for the latest official IL VOLO tour announcements.</p>

      </div>

      `;

      return;

    }

    upcomingConcerts.forEach(concert=>{

      concertList.innerHTML+=`

      <div class="concert-card">

        <h3>🎤 ${concert.city}</h3>

        <p>📅 <strong>${concert.date}</strong></p>

        <p>📍 ${concert.venue}</p>

        <p>🌍 ${concert.country}</p>

        <div class="ticket-info">

          <h4>🎟 Tickets & Fan Information</h4>

          <div class="ticket-buttons">

            <a class="email-btn"
               href="mailto:ilvolomusic425@gmail.com">

               📧 Email Management

            </a>

            <a class="telegram-btn"
               href="https://t.me/ilvolo_fan_community"
               target="_blank">

               📲 Telegram

            </a>

            <a class="zangi-btn"
               href="https://zangi.com/dl/conversation/9402253010"
               target="_blank">

               📞 Zangi

            </a>

          </div>

        </div>

      </div>

      `;

    });

  })

  .catch(error=>{

    console.error(error);

    const concertList=document.getElementById("concert-list");

    if(concertList){

      concertList.innerHTML=`

      <div class="concert-card">

      <h3>Unable to Load Concerts</h3>

      <p>Please try again later.</p>

      </div>

      `;

    }

  });