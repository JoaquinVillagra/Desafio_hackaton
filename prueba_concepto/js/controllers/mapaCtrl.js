app.controller("MapaCtrl", function($scope, uiGmapGoogleMapApi, MapService) {
    vm = this;
    vm.data = [];
    $scope.markerList = [];
    vm.map = { 
        center: { latitude: -33.4376, longitude: -70.6505 }, 
        zoom: 12,
        heatLayerCallback: function (layer) {
                //set the heat layers backend data
                MapService.getDatos().then(function(data){
                    vm.data = CSVToArray(data.data);
                    //console.log(vm.data);
                    var mockHeatLayer = new MockHeatLayer(layer);
                });
                },
        showHeat: true
    };

    vm.markers = [
        {id: 1, position: {latitude:-33.4326367,longitude: -70.6305423}, title:'Clinica'},
        {id: 2, position: {latitude: -33.426693,longitude:  -70.648168}, title:'Clinica'},
        {id: 3, position: {latitude: -33.484312,longitude:  -70.645799}, title:'Clinica'},
        {id: 4, position: {latitude: -33.484312,longitude:  -70.645799}, title:'Clinica'},
        {id: 5, position: {latitude:-33.456873,longitude:  -70.702931}, title:'Clinica'}
    ];
    //console.log(vm.map);
    uiGmapGoogleMapApi.then(function(maps) {

    });
    function MockHeatLayer(heatLayer) {
        var map, pointarray, heatmap;
        var taxiData = [];
        for (var i = vm.data.length - 1; i >= 0; i--) {
            //console.log(vm.data[i]);  
            var dato = new google.maps.LatLng(parseFloat(vm.data[i][2]),parseFloat(vm.data[i][1]));
            //console.log(dato);
            taxiData.push(dato);
        }
        //console.log(taxiData);
        var pointArray = new google.maps.MVCArray(taxiData);
        heatLayer.setData(pointArray);
    };

    function MockArreglo(capa) {
        var map, pointarray;
        var pointArray = new google.maps.MVCArray(vm.dataClinica);
        capa.setData(pointArray);
    };
    function CSVToArray( strData, strDelimiter ){
        // Check to see if the delimiter is defined. If not,
        // then default to comma.
        strDelimiter = (strDelimiter || ",");

        // Create a regular expression to parse the CSV values.
        var objPattern = new RegExp(
            (
                // Delimiters.
                "(\\" + strDelimiter + "|\\r?\\n|\\r|^)" +

                // Quoted fields.
                "(?:\"([^\"]*(?:\"\"[^\"]*)*)\"|" +

                // Standard fields.
                "([^\"\\" + strDelimiter + "\\r\\n]*))"
            ),
            "gi"
            );


        // Create an array to hold our data. Give the array
        // a default empty first row.
        var arrData = [[]];

        // Create an array to hold our individual pattern
        // matching groups.
        var arrMatches = null;


        // Keep looping over the regular expression matches
        // until we can no longer find a match.
        while (arrMatches = objPattern.exec( strData )){

            // Get the delimiter that was found.
            var strMatchedDelimiter = arrMatches[ 1 ];

            // Check to see if the given delimiter has a length
            // (is not the start of string) and if it matches
            // field delimiter. If id does not, then we know
            // that this delimiter is a row delimiter.
            if (
                strMatchedDelimiter.length &&
                strMatchedDelimiter !== strDelimiter
                ){

                // Since we have reached a new row of data,
                // add an empty row to our data array.
                arrData.push( [] );

            }

            var strMatchedValue;

            // Now that we have our delimiter out of the way,
            // let's check to see which kind of value we
            // captured (quoted or unquoted).
            if (arrMatches[ 2 ]){

                // We found a quoted value. When we capture
                // this value, unescape any double quotes.
                strMatchedValue = arrMatches[ 2 ].replace(
                    new RegExp( "\"\"", "g" ),
                    "\""
                    );

            } else {

                // We found a non-quoted value.
                strMatchedValue = arrMatches[ 3 ];

            }


            // Now that we have our value string, let's add
            // it to the data array.
            arrData[ arrData.length - 1 ].push( strMatchedValue );
        }

        // Return the parsed data.
        return( arrData );
    }
});