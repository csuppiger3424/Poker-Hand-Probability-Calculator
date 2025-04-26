import React from 'react';
import '../styles/SimulationResults.css';

function SimulationResults({ results }) {
  return (
    <div className="results-container">
      <h2>Simulation Results</h2>
      <p><strong>Player 1 Win Percentage:</strong> {results.player1_win_percentage.toFixed(2)}%</p>
    </div>
  );
}

export default SimulationResults;