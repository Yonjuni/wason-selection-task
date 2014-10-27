'use strict';

selectionTaskApp.controller("taskCtrl", function ($scope, $routeParams, Backend) {
    console.log($routeParams['id']);
    Backend.assign($routeParams['id']).success(function(data){

        $scope.taskData = angular.fromJson(data);
        
    });

    $scope.setSelection = function (number) {
        $scope.taskData[number].selected = !$scope.taskData[number].selected;
    };

    $scope.clickNext = function () {

    };

});
