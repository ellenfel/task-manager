import React from 'react';
import { Link } from 'react-router-dom';
import { useUser } from '../context/UserContext';

const Navbar = () => {
  const { user } = useUser();

  return (
    <nav className="bg-gray-800 text-white p-4">
      <div className="container mx-auto flex justify-between items-center">
        <Link to="/" className="text-xl font-bold">Task Manager</Link>
        <div>
          {user ? (
            <span>Welcome, {user.username}</span>
          ) : (
            <Link to="/login" className="bg-blue-500 text-white p-2 rounded hover:bg-blue-600">Login</Link>
          )}
        </div>
      </div>
    </nav>
  );
};

export default Navbar; 