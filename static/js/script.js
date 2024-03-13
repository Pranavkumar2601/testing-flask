// Fetch player names from Flask route
fetch("/players/names")
  .then((response) => response.json())
  .then((playerNames) => {
    const playerNameInput = document.getElementById("playerName");
    const playerList = document.getElementById("playerList");
    playerNames.forEach((name) => {
      const option = document.createElement("option");
      option.value = name;
      playerList.appendChild(option);
    });
  })
  .catch((error) => console.error("Error fetching player names:", error));
