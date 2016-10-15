path=['RM_402','H1','H2','H3','H4','H5','RR_M1']

for(i=0; i<path.length-1; i++){
    console.log(path[i]+'-'+path[i+1])
    e=document.getElementById(path[i]+'-'+path[i+1])
    if(e!==null){
        e.style.stroke="red"
    } else {
        e=document.getElementById(path[i+1]+'-'+path[i])
        e.style.stroke="red"
    }
}