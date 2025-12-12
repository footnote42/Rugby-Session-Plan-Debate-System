const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');

const app = express();
app.use(cors());
app.use(bodyParser.json());

let plans = [
  { id: 1, title: 'Passing & Support', author: 'Coach A', points: 'Quick ruck, 2 v 1 finishing' },
  { id: 2, title: 'Tackling Basics', author: 'Coach B', points: 'Low body position, wrap up' }
];

let debates = [
  { id: 1, planId: 1, author: 'Coach C', comment: 'Consider adding conditioning running between reps to simulate fatigue.' }
];

app.get('/api/plans', (req, res) => res.json(plans));
app.post('/api/plans', (req, res) => {
  const newPlan = { id: plans.length + 1, ...req.body };
  plans.push(newPlan);
  res.status(201).json(newPlan);
});

app.get('/api/debates', (req, res) => res.json(debates));
app.post('/api/debates', (req, res) => {
  const newDebate = { id: debates.length + 1, ...req.body };
  debates.push(newDebate);
  res.status(201).json(newDebate);
});

app.listen(3000, () => console.log('Backend API listening on http://localhost:3000'));
