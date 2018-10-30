pop=0;

function popup(x){
	var v = document.getElementById('textbox1').value;
	if(v.includes("fred")){
	pop++;
	alert(x+" "+pop);
	}
}

function countp(){
	pop++;
	alert("count is :"+pop)
}

function textgetset(){
	
    var v = document.getElementById('textbox1').value;
    v=(v.includes("fred"))?"FRED":v;
    document.getElementById('text').innerHTML = v;
    
}