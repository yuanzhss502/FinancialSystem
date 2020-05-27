

function init_chart(chartlist) {

    chartlist.forEach(function (value, index, array) {

        var elem = value['elemid'];
        console.log(elem);

        echarts.init(document.getElementById(elem));

    })

}

function flushchart(sdata,edata,elem,dims) {

    var url = "/data/get_data";
    var params = {

        "sdata": sdata,
        "edata": edata,
        "dims": dims

    };

    console.log(params);

    $.get(url, params, function(json_data) {
        if (json_data.code == 0){
            setChartData(elem, json_data.data);
        }

    });

}

function init_data(chartlist) {
    $("#sdata").jeDate({
            format:"YYYY-MM-DD",
            isTime:false,
            isinitVal: true,
            minDate:"2014-09-19 00:00:00",
            okfun: function(obj) {
                console.log(obj.elem);
                var sdata = $("#sdata").val();
                var edata = $("#edata").val();
                chartlist.forEach(function (value,index,array) {
                    var elemid = value['elemid'];
                    var dims = value['dims'];
                    flushchart(sdata,edata,elemid,dims)
                });
            }

    });

    $("#edata").jeDate({
            format:"YYYY-MM-DD",
            isTime:false,
            isinitVal: true,
            minDate:"2014-09-19 00:00:00",
            okfun: function(obj){
                console.log(obj.elem);
                var sdata = $("#sdata").val();
                var edata = $("#edata").val();
                chartlist.forEach(function (value,index,array) {
                    var elemid = value['elemid'];
                    var dims = value['dims'];
                    flushchart(sdata,edata,elemid,dims)
                });
            }
})}


function setChartData(elem,data) {

    var title = data['title'];
    var xAxis = data['xAxis'];
    var series = data['series'];

    var names = [];

    series.forEach(function (value,index,array) {

        names.push(value['name']);

    });


    var option = {
        title: {
            text: title
        },
        tooltip: {},
        legend: {
            data: names
        },
        xAxis: {
            data: xAxis
        },
        yAxis: {},
        series: series

        };
    var char = echarts.getInstanceByDom(document.getElementById(elem));
    char.setOption(option);
}

function login() {

    $("#btn").click(function () {

        var elem = $(this);

        if (elem.text() == '登录') {

            var url = '/user/login';
            var param = {

                "fwork_id": $('#account').val(),
                "fpassword": $('#password').val()
            };
            $.post(url, param, function (json_data) {
                console.log(json_data)
                if (json_data.code == 0) {

                    elem.text("注销");

                } else {

                    alert(json_data.msg);
                }

            });
        } else {

            var url = "/user/logout";
            $.post(url, {}, function (json_data) {

                if (json_data == 0) {

                    elem.text("登录");
                } else {

                    alert(json_data.msg)
                }

            })

        }

    });
}

