#!/usr/bin/node
exports.converter = function (base) {
    return nbre => nbre.toString(base);
};