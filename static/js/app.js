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

selectionTaskApp.run(function ($rootScope, $window, $document, localize) {
    // root scope functions
    $rootScope.getLanguages = function () {
        return ['en', 'jp'];
    };
    $rootScope.$watch('language', function (newLang) {
        localize.setLanguage(newLang);
        $rootScope.$broadcast('langChange', newLang);
    });
    // initialization
    if (!$rootScope.language) {
        $rootScope.language = $window.navigator.userLanguage ||
                              $window.navigator.language ||
                              $document.getElementsByTagName('html')[0].lang;
        if ($rootScope.language && ($rootScope.language.length > 2)) {
            $rootScope.language = $rootScope.language.substr(0, 2);
        }
    }
});