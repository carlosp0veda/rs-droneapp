import { FC, useState, useEffect } from 'react';
import MapView from '../../components/MapView/MapView';
import RunList from './RunList';
import RunDetails from './RunDetails';
import api from '../../services/api';

const DeliveryOverview: FC = () => {
  const [selectedRunId, setSelectedRunId] = useState<string | null>(null);
  const [runLocations, setRunLocations] = useState<any[]>([]);

  useEffect(() => {
    if (selectedRunId) {
      api.get(`/delivery-runs/${selectedRunId}/`)
        .then(res => setRunLocations(res.data.locations))
        .catch(err => console.error(err));
    }
  }, [selectedRunId]);

  return (
    <div className="overview-container">
      <aside className="sidebar">
        {!selectedRunId ? (
          <RunList onSelectRun={setSelectedRunId} />
        ) : (
          <>
            <button className="back-btn" onClick={() => setSelectedRunId(null)}>
              ← Back to List
            </button>
            <RunDetails runId={selectedRunId} />
          </>
        )}
      </aside>
      <main className="map-area">
        <MapView locations={runLocations} />
      </main>
    </div>
  );
};

export default DeliveryOverview;
