/* global process */

var gulp = require('gulp');
var browserify = require('browserify');
var source = require('vinyl-source-stream');
var stringify = require('stringify');

var entry = './fec/static/js/fec.js';
var debug = !!process.env.FEC_CMS_DEBUG;

gulp.task('build-js', function () {
  return browserify(entry, {debug: debug})
    .transform({global: true}, stringify(['.html']))
    .bundle()
    .pipe(source(entry))
    .pipe(gulp.dest('dist'));
});
