const express = require('express');
const cors = require('cors');
const app = express();
const port = 5000;

app.use((req, res, next) => {
  console.log(`Received a ${req.method} request to ${req.url}`);
  next();
});


app.use(cors());
app.use(express.json());

app.get('/', (req, res) => {
  res.send('Hello from the back-end!');
});

app.post('/api/login', (req, res) => {
  const { username, password } = req.body;
  // Perform login logic here (e.g., check username and password against a database)
  if (username === 'Admin' && password === '123456') {
    res.json({ success: true, message: 'Login successful!' });
  } else {
    res.status(401).json({ success: false, message: 'Invalid credentials' });
  }
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});