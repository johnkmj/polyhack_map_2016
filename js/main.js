function search(){
    console.log("go!")
    $.ajax({
           type: "GET",
           url: "http://httpbin.org/get",
           data: $("#form").serialize(), 
           success: function(data)
           {
               getresults(data); 
               showmap()
           }
         });
}

function getresults(data){
    console.log(data)
}

function showmap(){
    $("#form-container").animate({bottom: "100%"}, 700, false);
}


floors = ['1F','2F','3F','4F']
starting_floor=3 // (4th in floorlist)
sel=document.getElementById('floor-selector')
map=document.getElementById('map')
for(i=0; i<floors.length; i++){
    node=document.createElement("div")
    node.classList.add("level")
    node.innerHTML=floors[i]
    sel.appendChild(node)
}

sel.childNodes[starting_floor].classList.add("current")



levels=document.getElementsByClassName('level')
for(i=0; i<levels.length; i++){
    levels[i].addEventListener("click",changeLevel,false)
}

function changeLevel(){
    document.getElementsByClassName("current")[0].classList.remove("current")
    console.log(this.classList.add("current"))
    map.src="img/"+this.innerHTML+"_path.svg"
}