'use strict';

// Define the `phonecatApp` module
// console.log("i am in the app.module.js")
var HMPlotApp = angular.module('HMPlotApp', []);
HMPlotApp.controller('ListController', function ListController($scope) {
	$scope.files = [
		{
			name: 'Equal',
			concept_file: "../static/data/OverView.csv",
	 		mapping_file: "../static/graph_data/Mapping_OverView.csv",
	 		graph_file: "../static/graph_data/OverView.csv"		
	 	}

	];
	// console.log("i am in the app.module.js")

	$scope.orderProp = "Equal";

	

});

	console.log("i am in the app.module.js")
