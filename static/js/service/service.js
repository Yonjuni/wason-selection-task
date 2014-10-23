'use strict';

angular.module('BackendService', [])
    .factory('Backend', function ($http) {
        return {
            assign: function (id) {
                return $http({
                    method: "POST",
                    url: '/task/assign',
                    data: 'id=' + id,
                    headers: {'Content-Type': 'application/x-www-form-urlencoded'}
                });
            },
            submit: function () {
                return $http.get("/task/submit")
            }
        }
    });