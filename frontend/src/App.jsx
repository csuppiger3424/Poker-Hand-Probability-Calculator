import React, { useState } from 'react';
import SimulationForm from './components/SimulationForm';
import SimulationResults from './components/SimulationResults';
import './styles/App.css'; // Import the main App styles
import './styles/SimulationForm.css'; // Import the SimulationForm styles
import './styles/SimulationResults.css'; // Import the SimulationResults styles

function App() {
  const [results, setResults] = useState(null);

  const handleSimulation = async (formData) => {
    try {
      const response = await fetch('http://127.0.0.1:5000/simulate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        throw new Error('Failed to fetch simulation results');
      }

      const data = await response.json();
      setResults(data); // Update the results state with the backend response
    } catch (error) {
      console.error('Error running simulation:', error);
      alert('An error occurred while running the simulation. Please try again.');
    }
  };

  return (
    <div className="app-container">
      <header className="app-header">
        <h1>Poker Simulation</h1>
      </header>
      <main className="app-main">
        <SimulationForm onSubmit={handleSimulation} />
        {results && <SimulationResults results={results} />}
      </main>
    </div>
  );
}

export default App;
