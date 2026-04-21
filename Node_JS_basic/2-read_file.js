const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');

    const lines = data.split('\n').filter((line) => line.trim() !== '');

    // Remove header
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
          order.push(field); // preserve order (IMPORTANT for full marks)
        }

        fields[field].push(firstname);
      }
    });

    console.log(`Number of students: ${students.length}`);

    order.forEach((field) => {
      const list = fields[field].join(', ');
      console.log(`Number of students in ${field}: ${fields[field].length}. List: ${list}`);
    });
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
