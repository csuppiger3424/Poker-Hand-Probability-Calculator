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

  const handleSubmit = (e) => {
    e.preventDefault();

    if (playerCards.length !== 2) {
      alert('Please select exactly 2 cards for the player.');
      return;
    }

    if (![0, 3, 4, 5].includes(tableCards.length)) {
      alert('Please select 0, 3, 4, or 5 cards for the table.');
      return;
    }

    const formData = {
      num_games: numGames,
      num_players: numPlayers,
      player_cards: playerCards,
      table_cards: tableCards,
    };

    onSubmit(formData); // Pass the form data to the parent component
  };

  return (
    <form onSubmit={handleSubmit} className="simulation-form">
      <div className="form-container">
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
        <div>
          <label>Player 1 Cards:</label>
          <div className="selected-cards">
            {playerCards.map((card, index) => (
              <span key={index}>
                {card.suit} {card.rank}
              </span>
            ))}
          </div>
        </div>
        <div>
          <label>Table Cards:</label>
          <div className="selected-cards">
            {tableCards.map((card, index) => (
              <span key={index}>
                {card.suit} {card.rank}
              </span>
            ))}
          </div>
        </div>
        <div>
          <label>Select Cards:</label>
          <div className="card-grid">
            {allCards.map((card, index) => (
              <button
                type="button"
                key={index}
                className={`card ${
                  isCardSelected(card) ? 'selected' : ''
                }`}
                onClick={() =>
                  handleCardClick(
                    card,
                    playerCards.length < 2 ? 'player' : 'table'
                  )
                }
                disabled={isCardSelected(card)}
              >
                {card.suit} {card.rank}
              </button>
            ))}
          </div>
        </div>
        {error && <p style={{ color: 'red' }}>{error}</p>}
        <button type="submit">Run Simulation</button>
      </div>
    </form>
  );
}

export default SimulationForm;