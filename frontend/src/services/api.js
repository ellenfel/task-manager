import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api', // Adjust the base URL as needed
});

// Add a request interceptor to include the token in the headers
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token'); // Adjust as needed
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export const getTasks = async () => {
  const response = await api.get('/tasks/');
  return response.data;
};

export const createTask = async (task) => {
  const response = await api.post('/tasks/', task);
  return response.data;
};

// Add other API methods as needed

export default api;