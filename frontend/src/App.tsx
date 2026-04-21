import './App.css';
import DeliveryOverview from './features/delivery/DeliveryOverview';

function App() {
  return (
    <div className="app">
      <header className="app-header">
        <h1>DroneApp Operational Dashboard</h1>
        <div className="user-profile">Operator: DRN-OPERATOR-01</div>
      </header>
      <DeliveryOverview />
    </div>
  );
}

export default App;
