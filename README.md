# Poker Calculator

The Poker Calculator is a web-based tool designed to simulate poker games and calculate the win percentage for Player 1 based on selected cards and table cards. This project is built using React and Vite for a fast and efficient development experience.

## How It Works

1. **Input Parameters**:

   - Enter the number of games to simulate.
   - Specify the number of players in the game.

2. **Select Cards**:

   - Choose exactly 2 cards for Player 1.
   - Optionally, select 0, 3, 4, or 5 cards for the table.

3. **Run Simulation**:

   - Click the "Run Simulation" button to calculate the results.
   - The backend processes the simulation and returns the win percentage for Player 1.

4. **View Results**:

   - The results are displayed in the "Results" panel, showing Player 1's win percentage.

5. **Reset**:
   - Use the "Reset" button to clear all selections and start over.

## Features

- **Dynamic Card Selection**: Interactive card grid to select Player 1 and table cards.
- **Simulation Results**: Displays Player 1's win percentage based on the simulation.
- **Responsive Design**: Fits well on different screen sizes.
- **Dark Mode**: Toggle between light and dark themes for better usability.

## Technologies Used

- **Frontend**:

  - React: For building the user interface.
  - Vite: For fast development and build tooling.
  - CSS: For styling the components.

- **Backend**:
  - A Python-based backend (e.g., Flask) processes the simulation logic.

## Getting Started

### Prerequisites

- Node.js and npm installed on your machine.
- Python installed on your machine.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/PokerCalculator.git
   cd PokerCalculator
   ```

2. Start the backend:

   ```bash
   cd backend
   python api.py
   ```

3. Start the frontend:

   ```bash
   cd frontend
   npm install
   npm run dev
   ```

4. Open the app in your browser at `http://localhost:5173`.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
