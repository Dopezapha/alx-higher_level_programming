#!/usr/bin/node
'use strict';

const fs = require('fs');

function readFile (filePath) {
  try {
    const content = fs.readFileSync(filePath, 'utf-8');
    console.log(content);
  } catch (error) {
    console.error(error);
  }
}

if (require.main === module) {
  if (process.argv.length !== 3) {
    console.error('Usage: ./script.js <file_path>');
  } else {
    const filePath = process.argv[2];
    readFile(filePath);
  }
}

module.exports = readFile;
