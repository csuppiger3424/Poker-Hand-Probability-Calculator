import React, { useState } from 'react';
import '../styles/SimulationForm.css'; // Ensure the correct CSS file is imported

const suits = ['Heart', 'Diamond', 'Club', 'Spade'];
const ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]; // 11 = Jack, 12 = Queen, 13 = King, 14 = Ace

function SimulationForm({ onSubmit }) {
  const [numGames, setNumGames] = useState(10000);
  const [numPlayers, setNumPlayers] = useState(4);
  const [playerCards, setPlayerCards] = useState([]);
  const [tableCards, setTableCards] = useState([]);
  const [error, setError] = useState(null);
  const [results, setResults] = useState(null); // State to store simulation results

  const allCards = suits.flatMap((suit) =>
    ranks.map((rank) => ({ suit, rank }))
  );

  const isCardSelected = (card) => {
    return (
      playerCards.some(
        (selectedCard) =>
          selectedCard.suit === card.suit && selectedCard.rank === card.rank
      ) ||
      tableCards.some(
        (selectedCard) =>
          selectedCard.suit === card.suit && selectedCard.rank === card.rank
      )
    );
  };

  const handleCardClick = (card, target) => {
    if (isCardSelected(card)) {
      setError('This card is already selected.');
      return;
    }

    setError(null); // Clear any previous errors

    if (target === 'player' && playerCards.length < 2) {
      setPlayerCards([...playerCards, card]);
    } else if (target === 'table' && tableCards.length < 5) {
      setTableCards([...tableCards, card]);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!isFormValid()) {
      setError('Please ensure the form is valid before running the simulation.');
      return;
    }

    setError(null); // Clear any previous errors

    const formData = {
      num_games: numGames,
      num_players: numPlayers,
      player_cards: playerCards,
      table_cards: tableCards,
    };

    try {
      const response = await fetch('http://127.0.0.1:5000/simulate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        throw new Error(`Error: ${response.statusText}`);
      }

      const data = await response.json();
      setResults(data); // Store the results in state
    } catch (error) {
      setError('An error occurred while running the simulation.');
      console.error(error);
    }
  };

  const handleReset = () => {
    setPlayerCards([]); // Clear player cards
    setTableCards([]); // Clear table cards
    setError(null); // Clear any existing errors
    setResults(null); // Clear results
  };

  const getCardImage = (card) => {
    // Convert the suit to lowercase for the image filenames
    const suit = card.suit.toLowerCase();
    const rank = card.rank; // Use the rank as-is

    // Dynamically generate the image path based on suit and rank
    return `/assets/cards/${rank}_of_${suit}.png`;
  };

  const isFormValid = () => {
    return (
      playerCards.length === 2 && // Exactly 2 player cards
      [0, 3, 4, 5].includes(tableCards.length) // 0, 3, 4, or 5 table cards
    );
  };

  return (
    <div className="simulation-container">
      <div className="left-panel">
        <div className="description-panel">
          <h2>How to Use</h2>
          <p>
            Welcome to the Poker Calculator! Follow these steps to use the tool:
          </p>
          <ol>
            <li>Enter the number of games and players in the input fields.</li>
            <li>Select exactly 2 cards for Player 1.</li>
            <li>Select 0, 3, 4, or 5 cards for the table.</li>
            <li>Click "Run Simulation" to calculate the results.</li>
            <li>Use the "Reset" button to clear your selections.</li>
          </ol>
        </div>
        <div className="results-panel">
          <h2>Results</h2>
          {results ? (
            <div>
              <p>Player 1 Win Percentage: {results.player1_win_percentage}%</p>
            </div>
          ) : (
            <p>No results yet. Run a simulation to see the results here.</p>
          )}
        </div>
      </div>
      <form onSubmit={handleSubmit} className="simulation-form">
        <div className="form-container">
          <div className="input-group">
            <div>
              <label>Number of Games:</label>
              <input
                type="number"
                value={numGames}
                onChange={(e) => setNumGames(Number(e.target.value))}
                min="1"
              />
            </div>
            <div>
              <label>Number of Players:</label>
              <input
                type="number"
                value={numPlayers}
                onChange={(e) => setNumPlayers(Number(e.target.value))}
                min="2"
              />
            </div>
          </div>
          <div className="cards-section">
            <div>
              <label>Player 1 Cards:</label>
              <div className="selected-cards">
                {playerCards.map((card, index) => (
                  <img
                    key={index}
                    src={getCardImage(card)}
                    alt={`${card.rank} of ${card.suit}`}
                    className="selected-card"
                  />
                ))}
              </div>
            </div>
            <div>
              <label>Table Cards:</label>
              <div className="table-cards">
                {tableCards.map((card, index) => (
                  <img
                    key={index}
                    src={getCardImage(card)}
                    alt={`${card.rank} of ${card.suit}`}
                    className="selected-card"
                  />
                ))}
              </div>
            </div>
          </div>
          <div>
            <label>Select Cards:</label>
            <div className="card-grid">
              {allCards.map((card, index) => (
                <img
                  key={index}
                  src={getCardImage(card)}
                  alt={`${card.rank} of ${card.suit}`}
                  className={`card-image ${isCardSelected(card) ? 'selected' : ''}`}
                  onClick={() =>
                    handleCardClick(
                      card,
                      playerCards.length < 2 ? 'player' : 'table'
                    )
                  }
                  style={{
                    cursor: isCardSelected(card) ? 'not-allowed' : 'pointer',
                    opacity: isCardSelected(card) ? 0.5 : 1,
                  }}
                />
              ))}
            </div>
          </div>
          {error && <p style={{ color: 'red' }}>{error}</p>}
          <div className="button-group">
            <button type="submit" disabled={!isFormValid()}>
              Run Simulation
            </button>
            <button type="button" onClick={handleReset}>
              Reset
            </button>
          </div>
        </div>
      </form>
    </div>
  );
}

export default SimulationForm;