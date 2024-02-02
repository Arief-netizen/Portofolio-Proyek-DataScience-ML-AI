// const generateInputObject = (
//   gender,
//   age,
//   hypertension,
//   heart_disease,
//   ever_married,
//   work_type,
//   residence_type,
//   avg_glucose,
//   bmi,
//   smoking_status
// ) => {
//   return {
//     gender,
//     age,
//     hypertension,
//     heart_disease,
//     ever_married,
//     work_type,
//     residence_type,
//     avg_glucose,
//     bmi,
//     smoking_status,
//   };
// };

// const getInputData = () => {
//   const inputJenisKelamin = document.getElementById("gender");
//   const inputUsia = document.getElementById("age");
//   const inputRiwayatHipertensi = document.getElementById("hypertension");
//   const inputRiwayatJantung = document.getElementById("heart_disease");
//   const inputStatusPernikahan = document.getElementById("ever_married");
//   const inputPekerjaan = document.getElementById("work_type");
//   const inputTempatTinggal = document.getElementById("residence_type");
//   const inputGlukosa = document.getElementById("avg_glucose_level");
//   const inputMassaIndexTubuh = document.getElementById("bmi");
//   const inputStatusMerokok = document.getElementById("smoking_status");

//   let inputCekKesehatan = generateInputObject(
//     inputJenisKelamin.value,
//     inputUsia.value,
//     inputRiwayatHipertensi.value,
//     inputRiwayatJantung.value,
//     inputStatusPernikahan.value,
//     inputPekerjaan.value,
//     inputTempatTinggal.value,
//     inputGlukosa.value,
//     inputMassaIndexTubuh.value,
//     inputStatusMerokok.value
//   );

//   console.log(inputCekKesehatan);
// };
// document.addEventListener("DOMContentLoaded", function () {
//   const cekSubmit = document.getElementById("cekKesehatanSubmit");
//   cekSubmit.addEventListener("click", (e) => {
//     getInputData();
//     //biar gak reload
//     // e.preventDefault();
//   });
// });
