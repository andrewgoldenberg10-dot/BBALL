# NBA Draft vs. The League 🏀

A fun, interactive web game where you draft a random team of current NBA players and see how your squad stacks up against the season averages of real NBA franchises!

---

## 🎮 Core Gameplay Loop

1. **The Draft:** The game presents you with random pools of 10 NBA players. You pick one player per round until you have assembled a 5-man roster.
2. **Stat Aggregation:** The game combines the Points, Rebounds, and Assists (PTS, REB, AST) of your 5 drafted players to calculate your team's total power.
3. **The Simulation:** Your team's totals are compared directly against the real-world team statistics of all 30 NBA franchises.
4. **The Results:** Instantly view a breakdown of every team you successfully beat and which teams outperformed your squad.

---

## 🛠️ Built With

* **HTML5 & CSS3** - For the layout and responsive dashboard.
* **React (via CDN)** - For managing the draft state, randomized player pools, and win/loss calculations.
* **Tailwind CSS (Optional/via CDN)** - For rapid styling of the player cards and scoreboard.

---

## 🚀 How to Run Locally

Since this is a client-side prototype built in a single file, you don't need to install heavy dependencies to test it out!

1. Clone or download this repository.
2. Open the `index.html` file directly in any modern web browser (Chrome, Safari, Edge, Firefox).
3. Start drafting!

---

## 📈 Future Roadmap

* [ ] Replace mock data with live NBA player statistics using the `balldontlie` API.
* [ ] Add positional requirements (e.g., must draft at least one Center, Guard, etc.).
* [ ] Factor in defensive metrics or advanced efficiency ratings for deeper win/loss math.
