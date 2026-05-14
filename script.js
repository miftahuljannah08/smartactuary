function showMenu(menuId){

let menus =
document.querySelectorAll('.menu');

menus.forEach(menu => {
  menu.classList.add('hidden');
});

document.getElementById(menuId)
.classList.remove('hidden');

}

let chart;

function hitung(){

let modal =
parseFloat(document.getElementById("modal").value);

let bunga =
parseFloat(document.getElementById("bunga").value);

let tahun =
parseFloat(document.getElementById("tahun").value);

let hasil =
modal * (1 + bunga/100) ** tahun;

let keuntungan =
hasil - modal;

document.getElementById("hasil").innerHTML =
"Total akhir: Rp " +
Math.round(hasil).toLocaleString('id-ID');

document.getElementById("profit").innerHTML =
"Keuntungan investasi: Rp " +
Math.round(keuntungan).toLocaleString('id-ID');

let data = [];
let label = [];

for(let i = 0; i <= tahun; i++){

let total =
modal * (1 + bunga/100) ** i;

data.push(total);

label.push("Tahun " + i);

}

const ctx =
document.getElementById('grafik');

if(chart){
chart.destroy();
}

chart = new Chart(ctx, {

type: 'line',

data: {

labels: label,

datasets: [{

label: 'Pertumbuhan Investasi',

data: data,

borderWidth: 3,

tension: 0.4,

fill: true

}]

},

options: {
responsive: true
}

});

}

function hitungSimple(){

let modal =
parseFloat(document.getElementById("modalSimple").value);

let bunga =
parseFloat(document.getElementById("bungaSimple").value);

let tahun =
parseFloat(document.getElementById("tahunSimple").value);

let hasil =
modal * (1 + (bunga/100 * tahun));

let keuntungan =
hasil - modal;

document.getElementById("hasilSimple").innerHTML =
"Total akhir: Rp " +
Math.round(hasil).toLocaleString('id-ID');

document.getElementById("profitSimple").innerHTML =
"Keuntungan investasi: Rp " +
Math.round(keuntungan).toLocaleString('id-ID');

}