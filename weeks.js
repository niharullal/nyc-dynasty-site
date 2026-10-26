// NYC Dynasty newsletter manifest.
// Weeks are listed in order, oldest first; the newest week opens by default.
// To add a new week:
//   1. Create newsletters/week-XX/ and drop the newsletter images in,
//      numbered in reading order (01-..., 02-..., etc.).
//   2. Add an entry to the END of this array (replace the week's light
//      preview entry if one exists).
const WEEKS = [
  {
    week: 1,
    title: "Week 1",
    dates: "September 9–14, 2026",
    tagline: "Four titles. Two names on the trophy. Year five — the hunt starts now.",
    pages: [
      { src: "newsletters/week-01/01-week-1-preview.jpeg", label: "Week 1 Preview" },
      { src: "newsletters/week-01/02-featured-rivalry-vaibhav-taylor.jpeg", label: "Featured Rivalry: Vaibhav vs Taylor" }
    ]
  },
  {
    week: 2,
    title: "Week 2",
    dates: "September 17–21, 2026",
    tagline: "Week 2 gets personal. Three marquee rivalries, six matchups.",
    pages: [
      { src: "newsletters/week-02/01-week-2-preview.jpeg", label: "Week 2 Preview" },
      { src: "newsletters/week-02/02-advaith-vs-alan.jpeg", label: "Advaith vs Alan" },
      { src: "newsletters/week-02/03-manas-vs-dhiraj.jpeg", label: "Manas vs Dhiraj" },
      { src: "newsletters/week-02/04-soham-vs-taylor.jpeg", label: "Soham vs Taylor" },
      { src: "newsletters/week-02/05-shiamak-vs-vaibhav.jpeg", label: "Shiamak vs Vaibhav" },
      { src: "newsletters/week-02/06-dev-vs-achal.jpeg", label: "Dev vs Achal" },
      { src: "newsletters/week-02/07-nihar-vs-varun.jpeg", label: "Nihar vs Varun" }
    ]
  },
  {
    week: 3,
    title: "Week 3",
    dates: "September 24–28, 2026",
    tagline: "Six matchups set. The full newsletter drops before kickoff.",
    banner: "Everyone meets again.",
    bannerSub: "All six matchups are second meetings of the season. Round one is on the books — the rematches start Thursday.",
    preview: true,
    matchups: [
      {
        home: "Advaith", homeTeam: "First Indians", away: "Nihar", awayTeam: "Spider-Jan: Brand New Day",
        series: "Nihar leads 5–0 (Reg. 5–0; Post. 0–0)",
        blurb: "Five meetings since 2022, five Nihar wins — and never by fewer than nine points. Advaith gets his first crack of the year at the one series he has never solved. Spider-Jan has answered every version of the First Indians so far."
      },
      {
        home: "Dev", homeTeam: "Team Develeper", away: "Alan", awayTeam: "Best Not Miss",
        series: "Alan leads 3–2 (Reg. 3–2; Post. 0–0)",
        blurb: "The series has swung back and forth since 2022, including a 3.12-point Dev escape in 2024. Alan answered last season with a 44-point statement. Dev needs the counterpunch, or Alan strings together wins in this series for the first time since 2023."
      },
      {
        home: "Varun", homeTeam: "Every Kiss Begins With Zay", away: "Manas", awayTeam: "Concepts of a Team",
        series: "Manas leads 4–0 (Reg. 4–0; Post. 0–0)",
        blurb: "Manas has won all four meetings, but last season's was decided by 1.36 points — the closest this series has ever been. Varun keeps inching closer. Manas keeps closing the door."
      },
      {
        home: "Achal", homeTeam: "Team Handcuffs", away: "Vaibhav", awayTeam: "The Padawans",
        series: "Achal leads 3–2 (Reg. 2–2; Post. 1–0)",
        blurb: "Deadlocked 2–2 in the regular season, but Achal took their 2024 postseason meeting for the overall series lead. Vaibhav has answered with the last two regular-season wins — including a 113.30-point demolition in 2025, the widest margin this series has seen. Achal holds the edge; Vaibhav holds the momentum."
      },
      {
        home: "Taylor", homeTeam: "Fannin the Flames", away: "Dhiraj", awayTeam: "Love Thy Nabers",
        series: "Taylor leads 6–1 (Reg. 5–1; Post. 1–0)",
        blurb: "Dhiraj took the very first meeting back in 2022 — and hasn't beaten Taylor since. Six straight Taylor wins, postseason included, though the 0.56-point escape in 2023 remains the closest game this series has seen. The streak is long; it hasn't always been safe."
      },
      {
        home: "Soham", homeTeam: "The RB Shelter", away: "Shiamak", awayTeam: "Super Lamario Bros",
        series: "Shiamak leads 5–1 (Reg. 5–1; Post. 0–1)",
        blurb: "Shiamak has taken four straight meetings and owns the regular-season series 5–1. But Soham holds the one that stung most — a 51-point knockout in the 2022 postseason. He has been chasing that high ever since."
      }
    ]
  },
  {
    week: 4,
    title: "Week 4",
    dates: "October 1–5, 2026",
    tagline: "Four teams are 3–0. Four are 0–3. Both lists shrink by Monday.",
    pages: [
      { src: "newsletters/week-04/01-week-4-preview.png", label: "Week 4 Preview" },
      { src: "newsletters/week-04/02-advaith-vs-dev.png", label: "Advaith vs Dev" },
      { src: "newsletters/week-04/03-nihar-vs-manas.png", label: "Nihar vs Manas" },
      { src: "newsletters/week-04/04-alan-vs-vaibhav.png", label: "Alan vs Vaibhav" },
      { src: "newsletters/week-04/05-nishant-vs-taylor.png", label: "Nishant vs Taylor" },
      { src: "newsletters/week-04/06-soham-vs-achal.png", label: "Soham vs Achal" },
      { src: "newsletters/week-04/07-shiamak-vs-dhiraj.png", label: "Shiamak vs Dhiraj" }
    ]
  },
  {
    week: 5,
    title: "Week 5",
    dates: "October 8–12, 2026",
    tagline: "Week 5 raises the stakes. Three teams are 4–0. Three are 0–4.",
    pages: [
      { src: "newsletters/week-05/01-week-5-preview.png", label: "Week 5 Preview" },
      { src: "newsletters/week-05/02-advaith-vs-manas.png", label: "Advaith vs Manas" },
      { src: "newsletters/week-05/03-dev-vs-vaibhav.png", label: "Dev vs Vaibhav" },
      { src: "newsletters/week-05/04-nihar-vs-taylor.png", label: "Nihar vs Taylor" },
      { src: "newsletters/week-05/05-soham-vs-alan.png", label: "Soham vs Alan" },
      { src: "newsletters/week-05/06-nishant-vs-shiamak.png", label: "Nishant vs Shiamak" },
      { src: "newsletters/week-05/07-achal-vs-dhiraj.png", label: "Achal vs Dhiraj" }
    ]
  },
  {
    week: 7,
    title: "Week 7",
    dates: "October 22–26, 2026",
    tagline: "One unbeaten team. Six new tests. Alan stands alone at 6–0.",
    pages: [
      { src: "newsletters/week-07/01-week-7-preview.png", label: "Week 7 Preview" },
      { src: "newsletters/week-07/02-advaith-vs-taylor.png", label: "Advaith vs Taylor" },
      { src: "newsletters/week-07/03-soham-vs-vaibhav.png", label: "Soham vs Vaibhav" },
      { src: "newsletters/week-07/04-manas-vs-shiamak.png", label: "Manas vs Shiamak" },
      { src: "newsletters/week-07/05-dev-vs-dhiraj.png", label: "Dev vs Dhiraj" },
      { src: "newsletters/week-07/06-nihar-vs-achal.png", label: "Nihar vs Achal" },
      { src: "newsletters/week-07/07-alan-vs-nishant.png", label: "Alan vs Nishant" },
      { src: "newsletters/week-07/08-extra-schedule-luck-report.png", label: "League Extra: The Schedule Luck Report" },
      { src: "newsletters/week-07/09-extra-behind-the-records.png", label: "League Extra: Behind the Records" }
    ]
  }
];
