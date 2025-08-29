// ProfilePage.js
import React, { useEffect, useState } from 'react';

const ProfilePage = () => {
  const [profile, setProfile] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const token = localStorage.getItem('token');
        const response = await fetch('/api/me/', {
          headers: {
            'Authorization': `Bearer ${token}`,
          },
        });
        const responseText = await response.text();
        if (!response.ok) {
          throw new Error(`Failed to fetch profile: ${response.status} ${response.statusText}. Response: ${responseText}`);
        }
        let data;
        try {
          data = JSON.parse(responseText);
        } catch (jsonErr) {
          throw new Error(`Invalid JSON response: ${responseText}`);
        }
        setProfile(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };
    fetchProfile();
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;
  if (!profile) return <div>No profile data.</div>;

  return (
    <div>
      <h2>Profile</h2>
      <p><strong>Username:</strong> {profile.username}</p>
      <p><strong>Email:</strong> {profile.email}</p>
    </div>
  );
};

export default ProfilePage;
