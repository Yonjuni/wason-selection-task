'use strict';

selectionTaskApp.controller("introductionCtrl", function ($scope, $routeParams, $location) {
    $scope.continueButton = function () {
        $location.path('/task/' + $routeParams['id']);
    };
});