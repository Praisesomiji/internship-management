import React, { useEffect, useState } from 'react';
import api from './api';

function App() {
  const [profiles, setProfiles] = useState([]);

  useEffect(() => {
    api.get('members/profiles/')
      .then(response => {
        setProfiles(response.data);
      })
      .catch(error => {
        console.error('Error fetching profiles:', error);
      });
  }, []);

  return (
    <div className="App">
      <h1>Profiles</h1>
      <ul>
        {profiles.map(profile => (
          <li key={profile.id}>{profile.user.username} - {profile.bio}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;

