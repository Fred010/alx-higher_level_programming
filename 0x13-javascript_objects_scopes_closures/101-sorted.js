#!/usr/bin/node
const dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const vals = Object.values(dict);
const valsUniq = [...new Set(vals)];
const newDict = {};
for (const id1 in valsUniq) {
  const list = [];
  for (const id2 in totalist) {
    if (totalist[id2][1] === valsUniq[id1]) {
      list.unshift(totalist[id2][0]);
    }
  }
  newDict[valsUniq[id1]] = list;
}
console.log(newDict);
