import React, { useState } from 'react';
import '../styles/SimulationForm.css'; // Ensure the correct CSS file is imported

function SimulationForm({ onSubmit }) {
  const [numGames, setNumGames] = useState(10000);
  const [numPlayers, setNumPlayers] = useState(4);
  const [playerCards, setPlayerCards] = useState([
    { suit: 'Heart', rank: 14 },
    { suit: 'Diamond', rank: 14 },
  ]);
  const [tableCardsInput, setTableCardsInput] = useState('');
  const [error, setError] = useState(null);

  const handleTableCardsChange = (e) => {
    const input = e.target.value;
    setTableCardsInput(input);

    try {
      const parsed = JSON.parse(input);
      if (Array.isArray(parsed)) {
        setError(null); // Clear any previous errors
      } else {
        setError('Table cards must be an array of objects.');
      }
    } catch {
      setError('Invalid JSON format for table cards.');
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (error) {
      alert('Please fix the errors before submitting.');
      return;
    }

    try {
      const tableCards = JSON.parse(tableCardsInput || '[]');
      onSubmit({
        num_games: numGames,
        num_players: numPlayers,
        player_cards: playerCards,
        table_cards: tableCards,
      });
    } catch {
      alert('Invalid JSON format for table cards.');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="simulation-form">
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
        <input
          type="text"
          placeholder="Suit"
          value={playerCards[0].suit}
          onChange={(e) =>
            setPlayerCards([{ ...playerCards[0], suit: e.target.value }, playerCards[1]])
          }
        />
        <input
          type="number"
          placeholder="Rank"
          value={playerCards[0].rank}
          onChange={(e) =>
            setPlayerCards([{ ...playerCards[0], rank: Number(e.target.value) }, playerCards[1]])
          }
        />
        <input
          type="text"
          placeholder="Suit"
          value={playerCards[1].suit}
          onChange={(e) =>
            setPlayerCards([playerCards[0], { ...playerCards[1], suit: e.target.value }])
          }
        />
        <input
          type="number"
          placeholder="Rank"
          value={playerCards[1].rank}
          onChange={(e) =>
            setPlayerCards([playerCards[0], { ...playerCards[1], rank: Number(e.target.value) }])
          }
        />
      </div>
      <div>
        <label>Table Cards (JSON):</label>
        <textarea
          placeholder='[{"suit": "Heart", "rank": 13}]'
          value={tableCardsInput}
          onChange={handleTableCardsChange}
        />
        {error && <p style={{ color: 'red' }}>{error}</p>}
      </div>
      <button type="submit">Run Simulation</button>
    </form>
  );
}

export default SimulationForm;