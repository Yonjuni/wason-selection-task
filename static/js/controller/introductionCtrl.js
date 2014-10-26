'use strict';

selectionTaskApp.controller("introductionCtrl", function ($scope, $routeParams, $location) {
    console.log($routeParams['id']);


    $scope.continueButton = function () {
        $location.path('/task/12');
    };

});