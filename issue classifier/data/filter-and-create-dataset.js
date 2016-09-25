var max = 3000;
var allowedLabels = {
    'bug': true,
    'question': true,
    'enhancement': true,
    'help wanted': true,
    'wontfix': true,
    'invalid': true,
    'duplicate': true
};
var datasetFilename = './dataset.json';
var testsetFilename = './testset.json';

var data = require('./simple-issue-standard-label-json.json');
var categories = {};

var dataset = [], testset = [];
var _ds = {}, _ts = {};
data.forEach(function(d) {
    if (typeof allowedLabels[d.label.toLowerCase()] == 'undefined') return;

    if (typeof categories[d.label] == 'undefined') {
        categories[d.label] = 0;
    }
    categories[d.label]++;

    if (categories[d.label] > max) {
        testset.push(d);
        if (typeof _ts[d.label] == 'undefined') _ts[d.label] = 0;
        _ts[d.label]++;
    } else {
        dataset.push(d);
        if (typeof _ds[d.label] == 'undefined') _ds[d.label] = 0;
        _ds[d.label]++;
    }
});


console.log('categorisation done.');
console.log(_ds, _ts);


var fs = require('fs');
fs.writeFileSync(datasetFilename, JSON.stringify(dataset));
fs.writeFileSync(testsetFilename, JSON.stringify(testset));