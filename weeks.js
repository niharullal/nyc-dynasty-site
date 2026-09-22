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
        series: "Vaibhav leads 1–0 (Reg. 1–0; Post. 0–0)",
        blurb: "Somehow just one meeting since 2022 — and it was a 113.30-point Vaibhav blowout in 2025, the widest margin either manager has been part of. Achal gets the chance to rewrite the only page in this book."
      },
      {
        home: "Taylor", homeTeam: "Fannin the Flames", away: "Dhiraj", awayTeam: "Love Thy Nabers",
        series: "Taylor leads 4–0 (Reg. 3–0; Post. 1–0)",
        blurb: "Taylor is a perfect 4–0 against Dhiraj, postseason included, at an average margin near 54 points. Dhiraj's closest call was 7.44 in their first meeting — the gap has only widened since. Someone's story changes this week, or it really is a pattern."
      },
      {
        home: "Soham", homeTeam: "The RB Shelter", away: "Shiamak", awayTeam: "Super Lamario Bros",
        series: "Shiamak leads 5–1 (Reg. 5–1; Post. 0–1)",
        blurb: "Shiamak has taken four straight meetings and owns the regular-season series 5–1. But Soham holds the one that stung most — a 51-point knockout in the 2022 postseason. He has been chasing that high ever since."
      }
    ]
  }
];
