const bt1=document.getElementById("bt1");
const bt2=document.getElementById("bt2");
const year =document.getElementById("year");
const km =document.getElementById("km");
const fuel =document.getElementById("fuel");
const seller =document.getElementById("seller");
const tranmission =document.getElementById("tranmission");
const owner =document.getElementById("owner");
const mileage =document.getElementById("mileage");
const engine =document.getElementById("engine");
const speed =document.getElementById("speed");
const seat =document.getElementById("seat");
const p = document.getElementsByTagName("p");
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
const change = document.getElementsByClassName("input");

bt1.addEventListener("click",()=>{
    p[0].style.visibility = "hidden";
    const data = new FormData();
    data.append("a2",year.value);
    data.append("a3",km.value);
    data.append("a4",fuel.value);
    data.append("a5",seller.value);
    data.append("a6",tranmission.value);
    data.append("a7",owner.value);
    data.append("a8",mileage.value);
    data.append("a9",engine.value);
    data.append("a10",speed.value);
    data.append("a11",seat.value);
    if(km.value < 10 || km.value > 2000000 || fuel.value == "none" || seller.value == "none" || tranmission.value == "none" || owner.value == "none" || mileage.value < 10 || mileage.value > 40 || engine.value < 700 || engine.value > 5000 || speed.value < 80 || speed.value > 400 || seat.value < 5 || seat.value > 10 ){
        alert("Invalid input");
    }else{
        fetch("/pred/",{
            method:"POST",
            body:data,
            headers: {
                "X-CSRFToken": csrftoken
            }
        }).then((Response)=>{
            return Response.json();
        }).then((data)=>{
            p[0].textContent="Predicted price : "+" "+data.result;
            p[0].style.visibility = "visible"; 
        }).catch((error)=>{
            p[0].textContent="Predicted price : "+" API error";
            p[0].style.visibility = "visible"; 
        })
    }
});

bt2.addEventListener("click",()=>{
    year.value=2024;
    km.value = "";
    fuel.value="none";
    seller.value="none";
    tranmission.value="none";
    owner.value="none";
    mileage.value="";
    engine.value="";
    speed.value="";
    seat.value="";
    p[0].style.visibility = "hidden";
});

for(let i=0;i<change.length;i++){
    change[i].addEventListener("change",()=>{
        p[0].style.visibility = "hidden";
    });
}
