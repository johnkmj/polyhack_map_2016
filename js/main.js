function search(){
    console.log("go!")
    $.ajax({
           type: "POST",
           url: "/map/",
           data: roommap($("#form").serialize()), 
           success: function(data)
           {
               getresults(data); 
               showmap()
           }
         });
}

alias={'Room+402':'RM_402', 'Room+401+A':'RM_401_a','Room+401+B':'RM_401_b', 'West+Stairwell': 'ST_WEST','Men\'s+Restroom':'RR_M1'}

function roommap(str){
    strs=str.split(/=|&/)
    return strs[0]+"="
        +((alias[strs[1]]!=undefined)? alias[strs[1]]:strs[1]) +"&"+strs[2]+"="
        +((alias[strs[3]]!=undefined)? alias[strs[3]]:strs[3])
}

locations=document.getElementById('locations')
function getresults(data){
    console.log(data)
    path=data.split(",")
    start=path[0]
    stop=path[path.length-1]
    locations.innerHTML= start+" to "+stop
    renderpath(path)
}

function showmap(){
    $("#form-container").animate({bottom: "100%"}, 700, false);
}




function showsearch(){
    $("#form-container").animate({bottom: "0"}, 700, false);
}



var floors = ['1F','2F','3F','4F']
var starting_floor=3 // (4th in floorlist)
var sel=document.getElementById('floor-selector')
var map=document.getElementById('map')
for(i=0; i<floors.length; i++){
    node=document.createElement("div")
    node.classList.add("level")
    node.innerHTML=floors[i]
    sel.appendChild(node)
}

sel.childNodes[starting_floor].classList.add("current")
map.innerHTML=svg[starting_floor]


levels=document.getElementsByClassName('level')
for(i=0; i<levels.length; i++){
    levels[i].addEventListener("click",updatemap,false)
}

function updatemap(){
    for(i=0; i<levels.length; i++){
        if(levels[i] == this){
            j=i
            break  
        } 
    }
    document.getElementsByClassName("current")[0].classList.remove("current")
    this.classList.add("current")
    console.log(map.innerHTML)
    map.innerHTML=svg[j]
}


function renderpath(path){
    for(i=0; i<path.length-1; i++){
        console.log(path[i]+'-'+path[i+1])
        e=document.getElementById(path[i]+'-'+path[i+1])
        if(e!==null){
            e.style.stroke="red"
        } else {
            e=document.getElementById(path[i+1]+'-'+path[i])
            e.style.stroke="red"
        }
        document.getElementById(path[0]).style.fill="red"
        document.getElementById(path[path.length-1]).style.fill="red"
    }
}