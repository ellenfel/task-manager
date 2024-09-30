import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import HomePage from './pages/HomePage';
import TaskPage from './pages/TaskPage';
import NotFoundPage from './pages/NotFoundPage';

function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={HomePage} />
        <Route path="/tasks" component={TaskPage} />
        <Route component={NotFoundPage} />
      </Switch>
    </Router>
  );
}

export default App;
