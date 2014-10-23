'use strict';

selectionTaskApp.controller("taskCtrl", function ($scope, $routeParams, Backend) {
    console.log($routeParams['id']);
    Backend.assign($routeParams['id']);

    $scope.clickNext = function () {

    };

});
