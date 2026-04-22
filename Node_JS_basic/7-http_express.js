const express = require('express');
const fs = require('fs');

const app = express();

app.get('/', (req, res) => {
  res.status(200).send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  const database = process.argv[2];

  fs.readFile(database, 'utf8', (err, data) => {
    if (err) {
      res.status(200).send('This is the list of our students\nCannot load the database');
      return;
    }

    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const students = lines.slice(1);

    const fields = {};
    const order = [];

    students.forEach((student) => {
      const parts = student.split(',');

      if (parts.length === 4) {
        const firstname = parts[0];
        const field = parts[3];

        if (!fields[field]) {
          fields[field] = [];
          order.push(field);
        }

        fields[field].push(firstname);
      }
    });

    let output = 'This is the list of our students\n';
    output += `Number of students: ${students.length}\n`;

    order.forEach((field) => {
      output += `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}\n`;
    });

    res.status(200).send(output.trim());
  });
});

app.listen(1245);

module.exports = app;
