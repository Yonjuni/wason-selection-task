'use strict';

angular.module('BackendService', [])
    .factory('Backend', function ($http) {
        return {
            loadQuestions: function () { $http.get("/loadQuestions") }
        }
    });