const http = require('http');
const fs = require('fs');

const app = http.createServer((req, res) => {
  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!');
    return;
  }

  if (req.url === '/students') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });

    res.write('This is the list of our students\n');

    const database = process.argv[2];

    fs.readFile(database, 'utf8', (err, data) => {
      if (err) {
        res.end('Cannot load the database');
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

      res.write(`Number of students: ${students.length}\n`);

      order.forEach((field) => {
        res.write(
          `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}\n`
        );
      });

      res.end();
    });

    return;
  }

  res.writeHead(404, { 'Content-Type': 'text/plain' });
  res.end('Not found');
});

app.listen(1245);

module.exports = app;
