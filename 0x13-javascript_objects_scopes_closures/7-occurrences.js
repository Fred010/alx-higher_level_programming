#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let numOccurrences = 0;
  for (let id = 0; id < list.length; id++) {
    if (searchElement === list[id]) {
      numOccurrences++;
    }
  }
  return numOccurrences;
};
