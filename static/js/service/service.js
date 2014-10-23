'use strict';

angular.module('BackendService', [])
    .factory('Backend', function ($http) {
        return {
            assign: function () { $http.get("/task/assign") },
            submit: function () { $http.get("/task/submit") }
        }
    });