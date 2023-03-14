#!/usr/bin/node
const list = require('./100-data').list;
const newList = list.map((current, index) => {
  return (current * index);
});
console.log(list);
console.log(newList);
