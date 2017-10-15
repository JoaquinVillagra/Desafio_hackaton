app.controller("MainCtrl", function($scope) {
    vm = this;
    vm.equipos = [
        {nombre: '', puntaje: 0, tabla: [{Q1:0,Q2:0,Q3:0,total:0},{Q1:0,Q2:0,Q3:0,total:0},{Q1:0,Q2:0,Q3:0,total:0},{Q1:0,Q2:0,Q3:0,total:0},{Q1:0,Q2:0,Q3:0,total:0},{Q1:0,Q2:0,Q3:0,total:0}]},
        {nombre: '', puntaje: 0, tabla: [{Q1:0,Q2:0,Q3:0,total:0},{Q1:0,Q2:0,Q3:0,total:0},{Q1:0,Q2:0,Q3:0,total:0},{Q1:0,Q2:0,Q3:0,total:0},{Q1:0,Q2:0,Q3:0,total:0},{Q1:0,Q2:0,Q3:0,total:0}]},
        {nombre: '', puntaje: 0, tabla: [{Q1:0,Q2:0,Q3:0,total:0},{Q1:0,Q2:0,Q3:0,total:0},{Q1:0,Q2:0,Q3:0,total:0},{Q1:0,Q2:0,Q3:0,total:0},{Q1:0,Q2:0,Q3:0,total:0},{Q1:0,Q2:0,Q3:0,total:0}]},
        {nombre: '', puntaje: 0, tabla: [{Q1:0,Q2:0,Q3:0,total:0},{Q1:0,Q2:0,Q3:0,total:0},{Q1:0,Q2:0,Q3:0,total:0},{Q1:0,Q2:0,Q3:0,total:0},{Q1:0,Q2:0,Q3:0,total:0},{Q1:0,Q2:0,Q3:0,total:0}]}
    ];
    vm.equiposArreglados = [];
    vm.equiposArreglados2 = [];
    vm.estado = 0;

    vm.test = function(entrada){
        if(vm.estado == entrada) {
            return true;
        }
        return false;
    };

    vm.cambiar = function(numero){
        vm.estado+=numero;
        if(vm.estado==1){
            vm.sort();
        }
        if(vm.estado==2){
            vm.sort2();
        }
        if(vm.estado==3){
            vm.sort3();
        }
    };

    vm.sort = function(){
        vm.equiposArreglados = vm.equipos;
        vm.equiposArreglados.sort(function (a,b){
            return a.puntaje < b.puntaje;
        })
    };

    vm.sort2 = function(){
        console.log(vm.equiposArreglados);
        if(vm.equiposArreglados[0].tabla[5].total > vm.equiposArreglados[3].tabla[5].total){
            vm.equiposArreglados2[0] = vm.equiposArreglados[0];
            vm.equiposArreglados2[1] = vm.equiposArreglados[3];
        } else {
            vm.equiposArreglados2[0] = vm.equiposArreglados[3];
            vm.equiposArreglados2[1] = vm.equiposArreglados[0];
        }
        if(vm.equiposArreglados[1].tabla[5].total > vm.equiposArreglados[2].tabla[5].total){
            vm.equiposArreglados2[3] = vm.equiposArreglados[1];
            vm.equiposArreglados2[2] = vm.equiposArreglados[2];
        } else {
            vm.equiposArreglados2[3] = vm.equiposArreglados[2];
            vm.equiposArreglados2[2] = vm.equiposArreglados[1];
        }
        vm.equiposArreglados2[0].tabla = [{Q1:0,Q2:0,Q3:0,total:0},{Q1:0,Q2:0,Q3:0,total:0},{Q1:0,Q2:0,Q3:0,total:0},{Q1:0,Q2:0,Q3:0,total:0},{Q1:0,Q2:0,Q3:0,total:0},{Q1:0,Q2:0,Q3:0,total:0}];
        vm.equiposArreglados2[1].tabla = [{Q1:0,Q2:0,Q3:0,total:0},{Q1:0,Q2:0,Q3:0,total:0},{Q1:0,Q2:0,Q3:0,total:0},{Q1:0,Q2:0,Q3:0,total:0},{Q1:0,Q2:0,Q3:0,total:0},{Q1:0,Q2:0,Q3:0,total:0}];
        vm.equiposArreglados2[2].tabla = [{Q1:0,Q2:0,Q3:0,total:0},{Q1:0,Q2:0,Q3:0,total:0},{Q1:0,Q2:0,Q3:0,total:0},{Q1:0,Q2:0,Q3:0,total:0},{Q1:0,Q2:0,Q3:0,total:0},{Q1:0,Q2:0,Q3:0,total:0}];
        vm.equiposArreglados2[3].tabla = [{Q1:0,Q2:0,Q3:0,total:0},{Q1:0,Q2:0,Q3:0,total:0},{Q1:0,Q2:0,Q3:0,total:0},{Q1:0,Q2:0,Q3:0,total:0},{Q1:0,Q2:0,Q3:0,total:0},{Q1:0,Q2:0,Q3:0,total:0}];
    };
    vm.sort3 = function(){
        if(vm.equiposArreglados2[0].tabla[5].total > vm.equiposArreglados2[3].tabla[5].total){
            vm.equiposArreglados3[0] = vm.equiposArreglados2[0];
            vm.equiposArreglados3[1] = vm.equiposArreglados2[3];
        } else {
            vm.equiposArreglados3[0] = vm.equiposArreglados2[3];
            vm.equiposArreglados3[1] = vm.equiposArreglados2[0];
        }
        if(vm.equiposArreglados2[1].tabla[5].total > vm.equiposArreglados2[2].tabla[5].total){
            vm.equiposArreglados3[2] = vm.equiposArreglados2[1];
            vm.equiposArreglados3[3] = vm.equiposArreglados2[2];
        } else {
            vm.equiposArreglados3[2] = vm.equiposArreglados2[2];
            vm.equiposArreglados3[3] = vm.equiposArreglados2[1];
        }
    };

    vm.ajustar = function(equipo, tabla){
        vm.equiposArreglados[equipo].tabla[tabla].total = vm.equiposArreglados[equipo].tabla[tabla].Q1 + vm.equiposArreglados[equipo].tabla[tabla].Q2 + vm.equiposArreglados[equipo].tabla[tabla].Q3;
        vm.equiposArreglados[equipo].tabla[5].Q1 = 0;
        vm.equiposArreglados[equipo].tabla[5].Q2 = 0;
        vm.equiposArreglados[equipo].tabla[5].Q3 = 0;
        vm.equiposArreglados[equipo].tabla[5].total = 0;
        vm.equiposArreglados[equipo].tabla[5].Q1 = vm.equiposArreglados[equipo].tabla[0].Q1 + vm.equiposArreglados[equipo].tabla[1].Q1 + vm.equiposArreglados[equipo].tabla[2].Q1 + vm.equiposArreglados[equipo].tabla[3].Q1 + vm.equiposArreglados[equipo].tabla[4].Q1 + vm.equiposArreglados[equipo].tabla[5].Q1;
        vm.equiposArreglados[equipo].tabla[5].Q2 = vm.equiposArreglados[equipo].tabla[0].Q2 + vm.equiposArreglados[equipo].tabla[1].Q2 + vm.equiposArreglados[equipo].tabla[2].Q2 + vm.equiposArreglados[equipo].tabla[3].Q2 + vm.equiposArreglados[equipo].tabla[4].Q2 + vm.equiposArreglados[equipo].tabla[5].Q2;
        vm.equiposArreglados[equipo].tabla[5].Q3 = vm.equiposArreglados[equipo].tabla[0].Q3 + vm.equiposArreglados[equipo].tabla[1].Q3 + vm.equiposArreglados[equipo].tabla[2].Q3 + vm.equiposArreglados[equipo].tabla[3].Q3 + vm.equiposArreglados[equipo].tabla[4].Q3 + vm.equiposArreglados[equipo].tabla[5].Q3;
        vm.equiposArreglados[equipo].tabla[5].total = vm.equiposArreglados[equipo].tabla[0].total + vm.equiposArreglados[equipo].tabla[1].total + vm.equiposArreglados[equipo].tabla[2].total + vm.equiposArreglados[equipo].tabla[3].total + vm.equiposArreglados[equipo].tabla[4].total + vm.equiposArreglados[equipo].tabla[5].total;
    };

    vm.ajustar2 = function(equipo, tabla){
        vm.equiposArreglados2[equipo].tabla[tabla].total = vm.equiposArreglados2[equipo].tabla[tabla].Q1 + vm.equiposArreglados2[equipo].tabla[tabla].Q2 + vm.equiposArreglados2[equipo].tabla[tabla].Q3;
        vm.equiposArreglados2[equipo].tabla[5].Q1 = 0;
        vm.equiposArreglados2[equipo].tabla[5].Q2 = 0;
        vm.equiposArreglados2[equipo].tabla[5].Q3 = 0;
        vm.equiposArreglados2[equipo].tabla[5].total = 0;
        vm.equiposArreglados2[equipo].tabla[5].Q1 = vm.equiposArreglados2[equipo].tabla[0].Q1 + vm.equiposArreglados2[equipo].tabla[1].Q1 + vm.equiposArreglados2[equipo].tabla[2].Q1 + vm.equiposArreglados2[equipo].tabla[3].Q1 + vm.equiposArreglados2[equipo].tabla[4].Q1 + vm.equiposArreglados2[equipo].tabla[5].Q1;
        vm.equiposArreglados2[equipo].tabla[5].Q2 = vm.equiposArreglados2[equipo].tabla[0].Q2 + vm.equiposArreglados2[equipo].tabla[1].Q2 + vm.equiposArreglados2[equipo].tabla[2].Q2 + vm.equiposArreglados2[equipo].tabla[3].Q2 + vm.equiposArreglados2[equipo].tabla[4].Q2 + vm.equiposArreglados2[equipo].tabla[5].Q2;
        vm.equiposArreglados2[equipo].tabla[5].Q3 = vm.equiposArreglados2[equipo].tabla[0].Q3 + vm.equiposArreglados2[equipo].tabla[1].Q3 + vm.equiposArreglados2[equipo].tabla[2].Q3 + vm.equiposArreglados2[equipo].tabla[3].Q3 + vm.equiposArreglados2[equipo].tabla[4].Q3 + vm.equiposArreglados2[equipo].tabla[5].Q3;
        vm.equiposArreglados2[equipo].tabla[5].total = vm.equiposArreglados2[equipo].tabla[0].total + vm.equiposArreglados2[equipo].tabla[1].total + vm.equiposArreglados2[equipo].tabla[2].total + vm.equiposArreglados2[equipo].tabla[3].total + vm.equiposArreglados2[equipo].tabla[4].total + vm.equiposArreglados2[equipo].tabla[5].total;
    }; 
});