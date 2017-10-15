var app = angular.module("angularSpa", [
	"ngRoute", "nvd3", "ui.select", "ui.bootstrap","uiGmapgoogle-maps"
	])
	.constant('MyConfig', {
		urlBase: 'http://localhost:8080/grupo-1-tbd/'
	})
	.config(function(uiGmapGoogleMapApiProvider) {
    	uiGmapGoogleMapApiProvider.configure({
        	key: 'AIzaSyBvBtEuADxujaO7rFXfOoZogodhoXN2KcU',
        	v: '3.20', //defaults to latest 3.X anyhow
        	libraries: 'weather,geometry,visualization'
    	});
	})
	.service('MapService', function($http, $q){
		this.getDatos = function(){
			return $http.get('src/RM_Position.csv');
		};
	})
	.config(function($routeProvider) {
		$routeProvider
		.when("/home", {
			templateUrl: "views/main.html",
			controllerAs: "vm",
			controller: "MainCtrl"
		})
		.when("/mapa", {
			templateUrl: "views/mapas/mapa.html",
			controllerAs: "vm",
			controller: "MapaCtrl"
		})
		.otherwise({
			redirectTo: "/home"
		});
	});