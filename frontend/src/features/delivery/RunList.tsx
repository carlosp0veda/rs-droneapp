import { FC, useEffect, useState } from 'react';
import api from '../../services/api';

interface DeliveryRun {
  id: string;
  status: string;
  started_at: string;
  total_locations: number;
}

interface RunListProps {
  onSelectRun: (id: string) => void;
}

const RunList: FC<RunListProps> = ({ onSelectRun }) => {
  const [runs, setRuns] = useState<DeliveryRun[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api.get('/delivery-runs/')
      .then(res => setRuns(res.data))
      .catch(err => console.error(err))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <div>Loading runs...</div>;

  return (
    <div className="run-list">
      <h2>Active Delivery Runs</h2>
      <div className="run-grid">
        {runs.map(run => (
          <div 
            key={run.id} 
            className="run-card"
            onClick={() => onSelectRun(run.id)}
          >
            <div className="run-id">#{run.id.slice(0, 8)}</div>
            <div className={`status-badge status-${run.status.toLowerCase()}`}>
              {run.status}
            </div>
            <div className="run-stats">
              {run.total_locations} Locations
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default RunList;
