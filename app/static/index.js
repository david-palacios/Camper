window.onload = alert("hello!");


function getJSON()
{
    var url = "https://api.nps.gov/api/v1/campgrounds?parkCode=&q=fire";

    var request = new XMLHttpRequest();
    
    request.onload = function(){
        onJSONLoad(request.responseText);
    };
    
    //opening asyn
    request.open('GET', url, true);
    request.send();
    
}
function onJSONLoad(data)
{
    console.log(data);
}