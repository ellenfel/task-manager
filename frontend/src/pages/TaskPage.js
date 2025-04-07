import React, { useEffect, useState } from 'react';
import { getTasks, createTask } from '../services/api';

const TaskPage = () => {
  const [tasks, setTasks] = useState([]);
  const [newTask, setNewTask] = useState({ title: '', description: '' });

  useEffect(() => {
    const fetchTasks = async () => {
      const tasks = await getTasks();
      setTasks(tasks);
    };

    fetchTasks();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const task = await createTask(newTask);
    setTasks([...tasks, task]);
    setNewTask({ title: '', description: '' });
  };

  return (
    <div className="container mx-auto p-8">
      <h1 className="text-3xl font-semibold mb-6">Tasks</h1>
      <form onSubmit={handleSubmit} className="mb-6">
        <input
          type="text"
          value={newTask.title}
          onChange={(e) => setNewTask({ ...newTask, title: e.target.value })}
          placeholder="Task Title"
          className="w-full p-2 border rounded mb-2"
          required
        />
        <textarea
          value={newTask.description}
          onChange={(e) => setNewTask({ ...newTask, description: e.target.value })}
          placeholder="Task Description"
          className="w-full p-2 border rounded mb-2"
          required
        />
        <button type="submit" className="bg-blue-500 text-white p-2 rounded hover:bg-blue-600">
          Add Task
        </button>
      </form>
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

