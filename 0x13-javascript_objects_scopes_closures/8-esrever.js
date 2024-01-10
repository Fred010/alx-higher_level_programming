#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let id = 0;
  while ((len - id) > 0) {
    const backup = list[len];
    list[len] = list[id];
    list[id] = backup;
    id++;
    len--;
  }
  return list;
};
