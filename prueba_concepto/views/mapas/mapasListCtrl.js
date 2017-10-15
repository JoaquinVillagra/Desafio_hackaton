$("#modal").modal();
app.controller("mapasListCtrl", function($scope, TweetService){

    var vm = this;
    vm.dataLoaded = false;
    vm.comunaClickeada = "Santiago";
    vm.mostrarTodos = false;
    vm.mostrarFestival = false;

    vm.geoDatosTodos = [];
    vm.geoDatosLolla = [];
    vm.geoDatosCream = [];
    vm.geoDatosFauna = [];
    vm.geoDatosCumbre = [];
    vm.geoDatosFrontera = [];
    vm.geoDatosFiis = [];
    vm.geoDatosDefqon = [];

    vm.mostrarParaTodos = [];

    vm.mostrarParaFestival = [];

    // más obscuro, menos valor
    vm.coloresTodos = [];
    vm.coloresLolla = ['#204644', '#2C6360', '#397F7B', '#469B97', '#59b5b1', '#72C0BC', '#8ECCC9'];
    vm.coloresCream = ['#B8003A' , '#E00047', '#FF0050', '#FF3374'];
    /*vm.coloresFauna = ['#0000FE'];*/
    /*vm.coloresCumbre = [];*/
    /*vm.coloresFrontera = [];*/
    /*vm.coloresFiis = [];*/
    /*vm.coloresDefqon = [];*/

    vm.filterSelected = "tweets";
    vm.festivalSelected = "todos";

    TweetService.getTweetsPorComuna()
    .then(function(data) {
        vm.geoDatosTodos = data;
        TweetService.getTweetsPorFestivalyComuna()
        .then(function(data) {
            vm.geoDatosLolla = data[0].comunas;
            vm.geoDatosCream = data[1].comunas;
            vm.geoDatosFauna = data[2].comunas;
            vm.geoDatosCumbre = data[3].comunas;
            vm.geoDatosFrontera = data[4].comunas;
            vm.geoDatosFiis = data[5].comunas;
            vm.geoDatosDefqon = data[6].comunas;
            heatMap();
            vm.dataLoaded = true;
        })
    })

    function heatMap() {
        var mapOptions = {
            zoom: 11,
            scrollwheel: false,
            center: new google.maps.LatLng(-33.47039910425852, -70.6475830078125),
            mapTypeId: google.maps.MapTypeId.SATELLITE,
            mapTypeControl: false,
        };

        vm.map = new google.maps.Map(document.getElementById('mapa-de-calor'), mapOptions);
        vm.map.data.loadGeoJson('js/geojson/all.geojson')
        
        vm.map.data.setStyle(function(feature) {
            var color = getColor(feature.getProperty('NOM_COM'), vm.filterSelected, vm.festivalSelected);
            return {
                fillColor: color,
                fillOpacity: 0.8,
                strokeColor: '#FFFFFF'
            };
        });

        vm.map.data.addListener('click', function(e) {
            vm.comunaClickeada = e.feature.getProperty('NOM_COM');
            if (vm.festivalSelected == "todos") {
                vm.mostrarFestival = false;
                getDatosComunaTodos(vm.comunaClickeada);
                vm.mostrarTodos = true;
            }
            else {
                vm.mostrarTodos = false;
                getDatosComunaTodos(vm.comunaClickeada);
                var i = getDatosFestival();
                vm.mostrarParaFestival = vm.mostrarParaTodos[i];
                vm.mostrarFestival = true;
            }

            $("#modal").modal('show');
            $scope.$apply(); // Actualiza el valor asignado anteriormente
        });
    }

    function getDatosFestival() {
        if (vm.festivalSelected == "Lollapalooza") return 1;
        else if (vm.festivalSelected == "Creamfields") return 2;
        else if (vm.festivalSelected == "Fauna Primavera") return 3;
        else if (vm.festivalSelected == "Cumbre del Rock Chileno") return 4;
        else if (vm.festivalSelected == "Frontera") return 5;
        else if (vm.festivalSelected == "FiiS") return 6;
        else if (vm.festivalSelected == "Defqon.1") return 7;
    }

    function getDatosComunaTodos(comuna) {
        for (var i = 0; i < vm.geoDatosTodos.length; i++) {
            if (comuna == vm.geoDatosTodos[i].nombre) {
                var todos = {
                    'tweets': vm.geoDatosTodos[i].tweets,
                    'emoteScoreAvg': vm.geoDatosTodos[i].emoteScoreAvg
                };
            }
            if (comuna == vm.geoDatosLolla[i].nombre) {
                var lolla = {
                    'tweets': vm.geoDatosLolla[i].tweets,
                    'emoteScoreAvg': vm.geoDatosLolla[i].emoteScoreAvg
                };
            }
            if (comuna == vm.geoDatosCream[i].nombre) {
                var cream = {
                    'tweets': vm.geoDatosCream[i].tweets,
                    'emoteScoreAvg': vm.geoDatosCream[i].emoteScoreAvg
                };
            }
            if (comuna == vm.geoDatosFauna[i].nombre) {
                var fauna = {
                    'tweets': vm.geoDatosFauna[i].tweets,
                    'emoteScoreAvg': vm.geoDatosFauna[i].emoteScoreAvg
                };
            }
            if (comuna == vm.geoDatosCumbre[i].nombre) {
                var cumbre = {
                    'tweets': vm.geoDatosCumbre[i].tweets,
                    'emoteScoreAvg': vm.geoDatosCumbre[i].emoteScoreAvg
                };
            }
            if (comuna == vm.geoDatosFrontera[i].nombre) {
                var frontera = {
                    'tweets': vm.geoDatosFrontera[i].tweets,
                    'emoteScoreAvg': vm.geoDatosFrontera[i].emoteScoreAvg
                };
            }
            if (comuna == vm.geoDatosFiis[i].nombre) {
                var fiis = {
                    'tweets': vm.geoDatosFiis[i].tweets,
                    'emoteScoreAvg': vm.geoDatosFiis[i].emoteScoreAvg
                };
            }
            if (comuna == vm.geoDatosDefqon[i].nombre) {
                var defqon = {
                    'tweets': vm.geoDatosDefqon[i].tweets,
                    'emoteScoreAvg': vm.geoDatosDefqon[i].emoteScoreAvg
                };
            }

        }
        var datos = [todos, lolla, cream, fauna, cumbre, frontera, fiis, defqon];
        console.log(datos);
        vm.mostrarParaTodos = datos;
    }

    function getMax(arreglo, parametro) {
        var maximo = arreglo[0][parametro];
        for (var i = 1; i < arreglo.length; i++) {
            if (arreglo[i][parametro] > maximo)
                maximo = arreglo[i][parametro];
        }
        return maximo;
    }

    function getColor(comuna, filtro, festival) {
        var color = '';
        var datos = [];
        if (festival == "todos") datos = vm.geoDatosTodos;
        else if (festival == "Lollapalooza") datos = vm.geoDatosLolla;
        else if (festival == "Creamfields") datos = vm.geoDatosCream;
        else if (festival == "Fauna Primavera") datos = vm.geoDatosFauna;
        else if (festival == "Cumbre del Rock Chileno") datos = vm.geoDatosCumbre;
        else if (festival == "Frontera") datos = vm.geoDatosFrontera;
        else if (festival == "FiiS") datos = vm.geoDatosFiis;
        else if (festival == "Defqon.1") datos = vm.geoDatosDefqon;
        var colores = vm.coloresLolla;
        var maximo = getMax(datos, filtro);
        var dif = maximo / 7;
        angular.forEach(datos, function(value, key) {
            if (comuna == value.nombre) {
                if (value[filtro] <= dif) color = colores[0];
                else if (value[filtro] > dif && value[filtro] <= dif * 2) color = colores[1];
                else if (value[filtro] > dif * 2 && value[filtro] <= dif * 3) color = colores[2];
                else if (value[filtro] > dif * 3 && value[filtro] <= dif * 4) color = colores[3];
                else if (value[filtro] > dif * 4 && value[filtro] <= dif * 5) color = colores[4];
                else if (value[filtro] > dif * 5 && value[filtro] <= dif * 6) color = colores[5];
                else if (value[filtro] > dif * 6 && value[filtro] <= dif * 7) color = colores[6];
            }
        });
        return color;
    }

    vm.updateMap = function() {
        vm.filterSelected = vm.filterSelected;
        vm.festivalSelected = vm.festivalSelected;
        vm.map.data.setStyle(function(feature) {
            var color = getColor(feature.getProperty('NOM_COM'), vm.filterSelected, vm.festivalSelected);
            return {
                fillColor: color,
                fillOpacity: 0.8,
                strokeColor: '#FFFFFF'
            };
        });
    }

});