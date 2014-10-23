'use strict';

angular.module('BackendService', [])
    .factory('Backend', function ($http) {
        return {
            loadTask: function () { $http.get("/loadTask") }
        }
    });