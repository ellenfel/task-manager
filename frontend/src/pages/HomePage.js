import React from 'react';
import { useUser } from '../context/UserContext';

const HomePage = () => {
  const { user } = useUser();

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <h1 className="text-4xl font-bold text-gray-800">Welcome to the Task Manager</h1>
      {user ? (
        <p className="mt-4 text-lg text-gray-600">Welcome back, {user.username}!</p>
      ) : (
        <p className="mt-4 text-lg text-gray-600">Manage your tasks efficiently!</p>
      )}
    </div>
  );
};

export default HomePage;

