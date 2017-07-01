// Include Gulp
var gulp = require('gulp');

// Include Plugins
var sass = require('gulp-sass');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var autoprefixer = require('autoprefixer');
var rename = require('gulp-rename');
var postcss = require('gulp-postcss');
var cssmin = require('gulp-cssmin');

// Compile Sass
gulp.task('sass', function() {
    return gulp.src('library/static/scss/*.scss')
        .pipe(sass())
        .pipe(concat('style.css'))
        .pipe(gulp.dest('library/static'));
});

// Concatenate
gulp.task('scripts', function() {
    return gulp.src('library/static/js/src/*.js')
        .pipe(uglify())
        .pipe(concat('main.min.js'))
        .pipe(gulp.dest('library/static/js'));
});

// PostCSS processor
gulp.task('post-css', function () {
    var processors = [
        autoprefixer({browsers: ['last 1 version']}),
    ];
    return gulp.src('library/static/style.css')
        .pipe(postcss(processors))
        .pipe(cssmin())
        .pipe(concat('style.min.css'))
        .pipe(gulp.dest('library/static'))
});

// Complete CSS processing
gulp.task('css-process', ['sass', 'post-css']);

// Watch Files For Changes
gulp.task('watch', function() {
    gulp.watch('library/static/scss/*.scss', ['css-process']);
    gulp.watch('library/static/js/*.js', ['scripts']);
});

// Default Task
gulp.task('default', ['sass', 'scripts', 'post-css', 'watch']);