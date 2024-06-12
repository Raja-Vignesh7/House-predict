function submit(){
    var area = parseInt(document.getElementById('area').value);
    if(isNaN(area)){
        document.getElementById('outPut').innerText = "please enter a valid value";
    }
    else{
        fetch(`/get_price?area=${area}`)
        .then(response => response.json())
        .then(data =>{
            if(data.price){
                document.getElementById('outPut').innerText = `Price: ${data.price}`;
            }
            else {
                document.getElementById('outPut').textContent = 'Error data: ' + data.error;
            }
        })
        .catch(error =>{
            document.getElementById('outPut').innerText = 'Error: ' + error;
        });
    }
}