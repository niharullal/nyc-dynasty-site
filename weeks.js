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
      { home: "Advaith", homeTeam: "First Indians", away: "Nihar", awayTeam: "Spider-Jan: Brand New Day" },
      { home: "Dev", homeTeam: "Team Develeper", away: "Alan", awayTeam: "Best Not Miss" },
      { home: "Varun", homeTeam: "Every Kiss Begins With Zay", away: "Manas", awayTeam: "Concepts of a Team" },
      { home: "Achal", homeTeam: "Team Handcuffs", away: "Vaibhav", awayTeam: "The Padawans" },
      { home: "Taylor", homeTeam: "Fannin the Flames", away: "Dhiraj", awayTeam: "Love Thy Nabers" },
      { home: "Soham", homeTeam: "The RB Shelter", away: "Shiamak", awayTeam: "Super Lamario Bros" }
    ]
  }
];
