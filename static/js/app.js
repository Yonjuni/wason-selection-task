'use strict';

var selectionTaskApp = angular.module(
    "selectionTask",
    [
        "ngAnimate",
        "ngRoute"
    ]
).config(['$routeProvider', '$locationProvider', function ($routeProvider, $locationProvider) {
    $routeProvider.
        when('/', {templateUrl: '/static/partials/introduction.html', controller: 'introductionCtrl'}).
        when('/question/', {templateUrl: '/static/partials/question.html', controller: 'questionCtrl'}).
        otherwise({templateUrl: '/static/partials/introduction.html', controller: 'introductionCtrl'});
    // use the HTML5 History API
    $locationProvider.html5Mode(true).hashPrefix('!');
}]);