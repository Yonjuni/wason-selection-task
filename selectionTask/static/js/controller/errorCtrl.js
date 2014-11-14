'use strict';

selectionTaskApp.controller("errorCtrl", function ($scope, $routeParams) {
    $scope.id = $routeParams['id'];
    $scope.error = $routeParams['error'];
});
