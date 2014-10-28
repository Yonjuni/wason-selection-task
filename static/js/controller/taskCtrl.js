'use strict';

selectionTaskApp.controller("taskCtrl", function ($scope, $routeParams, $location, Backend) {
    console.log($routeParams['id']);
    Backend.assign($routeParams['id']).success(function(data){
        var result = angular.fromJson(data);
        if (!("Error" in result)) {
            $scope.taskData = result;
        }
    });

    $scope.setSelection = function (number) {
        $scope.taskData[number].selected = !$scope.taskData[number].selected;
    };

    $scope.clickNext = function () {
        Backend.submit($routeParams['id'], {
            'task_id': $scope.taskData['task_id'],
            1: !!$scope.taskData[1].selected,
            2: !!$scope.taskData[2].selected,
            3: !!$scope.taskData[3].selected,
            4: !!$scope.taskData[4].selected
        }).success(function (data) {
            var result = angular.fromJson(data);
            if ("Finished" in result) {

                $location.path('/thanks/' + $routeParams['id']);
            }
            if (!("Error" in result)) {
                $scope.taskData = result;
            }
        });
    };

});
