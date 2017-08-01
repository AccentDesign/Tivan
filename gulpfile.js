// Include Gulp
var gulp = require('gulp');

// Include Plugins
var sass = require('gulp-sass');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var rename = require('gulp-rename');
var autoprefixer = require('autoprefixer');
var postcss = require('gulp-postcss');
var cssmin = require('gulp-cssmin');
var runSequence = require('run-sequence');

var sassSources = ['library/static/scss/*.scss'];
var jsSources = ['library/static/js/src/*.js'];

// Concatenate & compress JS
gulp.task('js-process', function() {
    return gulp.src(jsSources)
        .pipe(uglify())
        .pipe(concat('main.min.js'))
        .pipe(gulp.dest('library/static/js'));
});

// Compile Sass
gulp.task('sass-compile', function() {
    return gulp.src(sassSources)
        .pipe(sass())
        .pipe(concat('style.css'))
        .pipe(gulp.dest('library/static'));
});

// PostCSS processor
gulp.task('post-css', function () {
    var processors = [
        autoprefixer({
            browsers: ['last 1 version']
        }),
    ];
    return gulp.src('library/static/style.css')
        .pipe(postcss(processors))
        .pipe(cssmin())
        .pipe(concat('style.min.css'))
        .pipe(gulp.dest('library/static'))
});

// Process CSS
gulp.task('css-process', function(callback) {
    runSequence('sass-compile', 'post-css', callback);
});

// Watch files for changes
gulp.task('watch', function() {
	gulp.watch(jsSources, ['js-process']);
	gulp.watch(sassSources, ['css-process']);
});

// Default Task
gulp.task('default', ['js-process', 'css-process', 'watch']);