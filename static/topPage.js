// ドラッグ&ドロップをさせる処理
var fileArea = document.getElementById('dragDropArea');
var fileInput = document.getElementById('fileInput');
fileArea.addEventListener('dragover', function(evt){
  evt.preventDefault();
  fileArea.classList.add('dragover');
});
fileArea.addEventListener('dragleave', function(evt){
    evt.preventDefault();
    fileArea.classList.remove('dragover');
});
fileArea.addEventListener('drop', function(evt){
    evt.preventDefault();
    fileArea.classList.remove('dragenter');
    var files = evt.dataTransfer.files;
    console.log("DRAG & DROP");
    console.table(files);
    fileInput.files = files;
    console.log(fileInput.files[1]);
    photoPreview('onChenge',files[0]);
});
function photoPreview(event, f = null) {
  var file = f;
  if(file === null){
      file = event.target.files[0];
  }
  var reader = new FileReader();
  var preview = document.getElementById("previewArea");
  var previewImage = document.getElementById("previewImage");

  if(previewImage != null) {
    preview.removeChild(previewImage);
  }
  reader.onload = function(event) {
    var img = document.createElement("img");
    img.setAttribute("src", reader.result);
    img.setAttribute("id", "previewImage");
    preview.appendChild(img);
  };

  reader.readAsDataURL(file);
}

// 追加
const ab = document.querySelector("#add-submit")
ab.addEventListener("click", (ev) => {
    ev.preventDefault(); // HTMLが本来持っている他の正常なボタン処理を無かったことにする

    console.log("登録ボタンが押された")
    const drp = document.getElementById("#dragDropArea")
    console.log(drp)
    console.log(fileInput.files[0]["name"]);

    fetch("/toppage",{
        method:'POST',
    }).then((response) => {

    });
})

