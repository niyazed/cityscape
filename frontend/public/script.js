$(function() {
    $('input[name="daterange"]').daterangepicker({
        
      opens: 'left'
    }, function(start, end, label) {
      // console.log("A new date selection was made: " + start.format('DD-MM-YYYY') + ' to ' + end.format('DD-MM-YYYY'));
      // document.getElementById('daterange').innerHTML = start.format('DD-MM-YYYY') + ' - ' + end.format('DD-MM-YYYY')
      
    });
  });