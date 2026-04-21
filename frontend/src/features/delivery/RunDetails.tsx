import { FC, useEffect, useState } from 'react';
import api from '../../services/api';

interface Location {
  id: string;
  name: string;
  category: string;
  status: string;
  sequence_order: number;
}

interface RunDetail {
  id: string;
  status: string;
  locations: Location[];
}

interface RunDetailsProps {
  runId: string;
}

const RunDetails: FC<RunDetailsProps> = ({ runId }) => {
  const [run, setRun] = useState<RunDetail | null>(null);

  useEffect(() => {
    api.get(`/delivery-runs/${runId}/`)
      .then(res => setRun(res.data))
      .catch(err => console.error(err));
  }, [runId]);

  if (!run) return <div>Loading run details...</div>;

  return (
    <div className="run-details">
      <div className="details-header">
        <h3>Run Details</h3>
        <span className="status-badge">{run.status}</span>
      </div>
      <div className="location-timeline">
        {run.locations.map(loc => (
          <div key={loc.id} className="location-item">
            <div className="seq">{loc.sequence_order}</div>
            <div className="loc-info">
              <div className="loc-name">{loc.name}</div>
              <div className="loc-cat">{loc.category}</div>
            </div>
            <div className={`loc-status ${loc.status.toLowerCase()}`}>
              {loc.status}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default RunDetails;
