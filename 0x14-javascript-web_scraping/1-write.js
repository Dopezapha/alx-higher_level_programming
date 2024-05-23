#!/usr/bin/node
'use strict';

const fs = require('fs');

function writeFile (filePath, content) {
  try {
    fs.writeFileSync(filePath, content, 'utf-8');
    console.log('Content has been successfully written to the file.');
  } catch (error) {
    console.error(error);
  }
}

if (require.main === module) {
  if (process.argv.length !== 4) {
    console.error('Usage: ./script.js <file_path> <string_to_write>');
  } else {
    const filePath = process.argv[2];
    const content = process.argv[3];
    writeFile(filePath, content);
  }
}

module.exports = writeFile;
