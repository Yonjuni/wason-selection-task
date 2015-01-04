'use strict';

selectionTaskApp.controller("taskCtrl", function ($scope, $routeParams, $location, Backend) {


    Backend.assign($routeParams['id']).success(function(data){
        var result = angular.fromJson(data);
        if ("Error" in result) {
            $location.path('/error/' + $routeParams['id'] + '/' + result["Error"]);
        }
        $scope.taskData = result;
        $scope.startTime = Date.now();
    });

    $scope.setSelection = function (number) {
        $scope.taskData[number].selected = !$scope.taskData[number].selected;
    };

    $scope.getCardTypeClass = function (idStr) {
        if (idStr.length == 3) {
            return 'card-three';
        }
        if (idStr.length == 4) {
            return 'card-four';
        }
        return 'card';
    };

    $scope.clickNext = function () {
        var endTime = Date.now();
        Backend.submit($routeParams['id'], {
            'task_id': $scope.taskData['task_id'],
            1: !!$scope.taskData[1].selected,
            2: !!$scope.taskData[2].selected,
            3: !!$scope.taskData[3].selected,
            4: !!$scope.taskData[4].selected,
            'time': endTime - $scope.startTime
        }).success(function (data) {
            var result = angular.fromJson(data);
            if ("Finished" in result) {

                $location.path('/thanks/' + $routeParams['id']);
            }
            if (!("Error" in result)) {
                $scope.taskData = result;
                $scope.startTime = Date.now();
            }
        });
    };

});
