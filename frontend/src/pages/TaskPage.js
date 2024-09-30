import React, { useEffect, useState } from 'react';
import { getTasks } from '../services/api';

const TaskPage = () => {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    const fetchTasks = async () => {
      const tasks = await getTasks();
      setTasks(tasks);
    };

    fetchTasks();
  }, []);

  return (
    <div className="container mx-auto p-8">
      <h1 className="text-3xl font-semibold mb-6">Tasks</h1>
      <ul className="bg-white shadow-md rounded-lg p-4">
        {tasks.map((task) => (
          <li key={task.id} className="border-b last:border-b-0 py-4">
            <div className="text-xl">{task.title}</div>
            <p className="text-gray-600">{task.description}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TaskPage;

