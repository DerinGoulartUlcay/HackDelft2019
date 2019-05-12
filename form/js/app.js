$(document).foundation();
$(document).ready(function () {
  $('.specificForm').hide();
  $('#Hotelcosts').show();
  $('#reimSelect').change(function () {
      if ( this.value == 'Hotelcosts')
      {
        $("#Hotelcosts").show();
        $("#Parkingcosts").hide();
        totalFcn();
      }
      else if ( this.value == 'Parkingcosts' )
      {
        $("#Hotelcosts").hide();
        $("#Parkingcosts").show();
        totalFcn2();
      }
    });
    //$('.specificForm').hide();
    //$('#'+$(this).val()).show();
  //})
});

function totalFcn(){
    var arr = document.getElementsByName('hotel');
    var tot=0;
    for(var i=0;i<arr.length;i++){
        if(parseFloat(arr[i].value))
            tot += parseFloat(arr[i].value);
    }
    document.getElementById('total').value = tot;
}

function totalFcn2(){
    var arr = document.getElementsByName('parking');
    var tot=0;
    for(var i=0;i<arr.length;i++){
        if(parseFloat(arr[i].value))
            tot += parseFloat(arr[i].value);
    }
    document.getElementById('total').value = tot;
}


