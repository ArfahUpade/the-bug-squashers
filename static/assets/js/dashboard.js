/* globals Chart:false, feather:false */

(function () {
  'use strict'

  feather.replace()

  // Graphs
  var ctx = document.getElementById('myChart')
  // eslint-disable-next-line no-unused-vars
  var myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: [
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '10',
        '11',
        '12',
        '13',
        '14',
        '15',
        '16',
        '17',
        '18',
        '19',
        '20',
        '21',
        '22',
        '23',
        '24',
        '25',
        '26',
        '27',
        '28',
        '29',
        '30',
        '31',
        '32',
        '33'
      ],
      datasets: [{
        data: [

          // 15,
          // 21,
          // 18,
          // 24,
          // 23,
          // 24,
          // 18,
          // 15,
          // 27,
          // 18,
          // 24,
          // 23,
          // 21,
          // 12,
          // 25,
          // 21,
          // 18,
          // 23,
          // 23,
          // 24,
          // 12,
          // 15,
          // 27,
          // 18,
          // 24,
          // 23,
          // 24,
          // 12,
          // 15,
          // 21,
          // 13,
          // 24,
          // 23
        ],
        lineTension: 0,
        backgroundColor: 'transparent',
        borderColor: '#007bff',
        borderWidth: 4,
        pointBackgroundColor: '#007bff'
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: false
          }
        }]
      },
      legend: {
        display: false
      }
    }
  })
})()

console.log("IN HERE!")
// var mylist = '{{ data| tojson}}';
// for (i = 0; i < mylist.length; i++) {
//   console.log(mylist[i])
// };

// var scatterChart = new Chart(ctx, {
//   type: 'scatter',
//   data: {
//     datasets: [{
//       label: 'Scatter Dataset',
//       data: [{
//         x: 1,
//         y: 0
//       }, {
//         x: 2,
//         y: 10
//       }, {
//         x: 3,
//         y: 5
//       }, {
//         x: 4,
//         y: 0
//       }, {
//         x: 5,
//         y: 10
//       }, {
//         x: 6,
//         y: 5
//       }, {
//         x: 7,
//         y: 0
//       }, {
//         x: 8,
//         y: 10
//       }, {
//         x: 9,
//         y: 5
//       }, {
//         x: 10,
//         y: 0
//       }, {
//         x: 11,
//         y: 10
//       }, {
//         x: 12,
//         y: 5
//       }, {
//         x: 13,
//         y: 0
//       }, {
//         x: 14,
//         y: 10
//       }, {
//         x: 15,
//         y: 5
//       }, {
//         x: 16,
//         y: 0
//       }, {
//         x: 17,
//         y: 10
//       }, {
//         x: 18,
//         y: 5
//       }, {
//         x: 19,
//         y: 0
//       }, {
//         x: 20,
//         y: 10
//       }, {
//         x: 21,
//         y: 5
//       }, {
//         x: 22,
//         y: 0
//       }, {
//         x: 23,
//         y: 10
//       }, {
//         x: 24,
//         y: 5
//       }, {
//         x: 25,
//         y: 0
//       }, {
//         x: 26,
//         y: 10
//       }, {
//         x: 27,
//         y: 5
//       }, {
//         x: 28,
//         y: 0
//       }, {
//         x: 29,
//         y: 10
//       }, {
//         x: 30,
//         y: 5
//       }, {
//         x: 31,
//         y: 0
//       }, {
//         x: 32,
//         y: 10
//       }, {
//         x: 33,
//         y: 5
//       }]
//     }]
//   },
//   options: {
//     scales: {
//       xAxes: [{
//         type: 'linear',
//         position: 'bottom'
//       }]
//     }
//   }
// });