
const historicalDaily = 'http://localhost:5000/historical/daily'
const historicalWeekly = 'http://localhost:5000/historical/weekly'
const historicalMonthly = 'http://localhost:5000/historical/monthly'


const predictSESSS = 'http://localhost:5000/predict/SES/SS'
const predictARIMASS = 'http://localhost:5000/predict/ARIMA/SS'
const predictCNNSS = 'http://localhost:5000/predict/CNN/SS'
const predictLSTMSS = 'http://localhost:5000/predict/LSTM/SS'
const predictHybridSS = 'http://localhost:5000/predict/CNN-LSTM/SS'


var price__ses = document.getElementById('price--ses')
var price__arima = document.getElementById('price--arima')
var price__cnn = document.getElementById('price--cnn')
var price__lstm = document.getElementById('price--lstm')
var price__hybrid = document.getElementById('price--hybrid')


fetch(predictSESSS, {            
	method: 'GET',
}).then((response)=>{
	return response.json();
}).then((data)=>{
	price__ses.textContent = data.toString().substring(0, 4)
})

fetch(predictARIMASS, {            
	method: 'GET',
}).then((response)=>{
	return response.json();
}).then((data)=>{
	price__arima.textContent = data.toString().substring(0, 4)
})

fetch(predictCNNSS, {            
	method: 'GET',
}).then((response)=>{
	return response.json();
}).then((data)=>{
	price__cnn.textContent = data[Object.keys(data)[0]].toString().substring(0, 4)
})

fetch(predictLSTMSS, {            
	method: 'GET',
}).then((response)=>{
	return response.json();
}).then((data)=>{
	price__lstm.textContent = data[Object.keys(data)[0]].toString().substring(0, 4)
})

fetch(predictHybridSS, {            
	method: 'GET',
}).then((response)=>{
	return response.json();
}).then((data)=>{
	price__hybrid.textContent = data[Object.keys(data)[0]].toString().substring(0, 4)
})


fetch(historicalDaily, {            
	method: 'GET',
}).then((response)=>{
	return response.json();
}).then((data)=>{
	len = Object.keys(data).length
	var labs = Object.keys(data).splice(len-28).map(function(v) { return v.slice(6) }) ;
	var vals = Object.values(data).splice(len-28);
	const ctx = document.getElementById('chart--daily').getContext('2d');
	console.log(ctx)
	const chart__daily = new Chart(ctx, {
		type: 'line',
		data: {
			labels: labs,
			datasets: [{
				label: 'Spot Price',
				data: vals,
				backgroundColor: [
					'rgba(255, 99, 132, 0.2)',
					'rgba(54, 162, 235, 0.2)',
					'rgba(255, 206, 86, 0.2)',
					'rgba(75, 192, 192, 0.2)',
					'rgba(153, 102, 255, 0.2)',
					'rgba(255, 159, 64, 0.2)'
				],
				borderColor: [
					'rgba(255, 99, 132, 1)',
					'rgba(54, 162, 235, 1)',
					'rgba(255, 206, 86, 1)',
					'rgba(75, 192, 192, 1)',
					'rgba(153, 102, 255, 1)',
					'rgba(255, 159, 64, 1)'
				],
				borderWidth: 1
			}]
		},
		options: {
			legend:{
				display: false
			},
			responsive: false,
			scales: {
				x: {
					grid: {
					  display: false
					}
				  },
				  y: {
					grid: {
					  display: false
					}
				  }
			}
		}
	});
})


fetch(historicalWeekly, {            
	method: 'GET',
}).then((response)=>{
	return response.json();
}).then((data)=>{
	len = Object.keys(data).length
	var labs = Object.keys(data).splice(len-4).map(function(v) { return v.slice(6) }) ;
	var vals = Object.values(data).splice(len-4);
	const ctx = document.getElementById('chart--weekly').getContext('2d');
	console.log(ctx)
	const chart__weekly = new Chart(ctx, {
		type: 'line',
		data: {
			labels: labs,
			datasets: [{
				label: 'Spot Price',
				data: vals,
				backgroundColor: [
					'rgba(255, 99, 132, 0.2)',
					'rgba(54, 162, 235, 0.2)',
					'rgba(255, 206, 86, 0.2)',
					'rgba(75, 192, 192, 0.2)',
					'rgba(153, 102, 255, 0.2)',
					'rgba(255, 159, 64, 0.2)'
				],
				borderColor: [
					'rgba(255, 99, 132, 1)',
					'rgba(54, 162, 235, 1)',
					'rgba(255, 206, 86, 1)',
					'rgba(75, 192, 192, 1)',
					'rgba(153, 102, 255, 1)',
					'rgba(255, 159, 64, 1)'
				],
				borderWidth: 1
			}]
		},
		options: {
			legend:{
				display: false
			},
			responsive: false,
			scales: {
				x: {
					grid: {
					  display: false
					}
				  },
				  y: {
					grid: {
					  display: false
					}
				  }
			}
		}
	});
})


fetch(historicalMonthly, {            
	method: 'GET',
}).then((response)=>{
	return response.json();
}).then((data)=>{
	len = Object.keys(data).length
	var labs = Object.keys(data).splice(len-12).map(function(v) { return v.slice(4) }) ;
	console.log(labs)
	var vals = Object.values(data).splice(len-12);
	const ctx = document.getElementById('chart--monthly').getContext('2d');
	const chart__monthly = new Chart(ctx, {
		type: 'line',
		data: {
			labels: labs,
			datasets: [{
				label: 'Spot Price',
				data: vals,
				backgroundColor: [
					'rgba(255, 99, 132, 0.2)',
					'rgba(54, 162, 235, 0.2)',
					'rgba(255, 206, 86, 0.2)',
					'rgba(75, 192, 192, 0.2)',
					'rgba(153, 102, 255, 0.2)',
					'rgba(255, 159, 64, 0.2)'
				],
				borderColor: [
					'rgba(255, 99, 132, 1)',
					'rgba(54, 162, 235, 1)',
					'rgba(255, 206, 86, 1)',
					'rgba(75, 192, 192, 1)',
					'rgba(153, 102, 255, 1)',
					'rgba(255, 159, 64, 1)'
				],
				borderWidth: 1
			}]
		},
		options: {
			legend:{
				display: false
			},
			responsive: false,
			scales: {
				x: {
					grid: {
					  display: false
					}
				  },
				  y: {
					grid: {
					  display: false
					}
				  }
			}
		}
	});
})