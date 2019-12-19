$(document).ready(function() {
  $.get(
    "sales-expectations",
    function(data) {
      var dateStrings = data.dates;
      var sales = data.sales;
      var prediction = data.prediction;

      var dateTimes = [];

      dateStrings.forEach(dateString => {
        var parts = dateString.split("-");
        var date = new Date(parts[0], parts[1] - 1, parts[2]);

        dateTimes.push(moment(date).format("DD/MM/YYYY"));
      });

      var ctx = document.getElementById('myChart').getContext('2d');
      var myChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: dateTimes,
          datasets: [
            {
              label: 'Sales Expectations',
              lineTension: 0,
              fill: false,
              data: prediction,
              borderWidth: 2,
              borderColor: "red",
            },
            {
              label: 'Sales Effective',
              data: sales,
              fill: false,
              lineTension: 0,
              borderWidth:2,
              borderColor: "blue",
            }
          ]
        },
        options: {
          elements: {
            point: {
              radius: 0
            }
          },
          scales: {
            yAxes: [{
              ticks: {
                beginAtZero: true
              }
            }],
            xAxes: [{
              ticks: {
                maxTicksLimit: 20
              }
            }]
          }
        }
      });
    }
  );
});
