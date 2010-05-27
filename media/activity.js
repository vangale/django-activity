

function Activity(subject, value1, value2) {

    subject = subject || "";
    value1 = value1 || "";
    value2 = value2 || "";

    var parms = "subject=" + subject + "&value1=" + value1 + "&value2=" + value2;

    var xhr; 
    try {  xhr = new ActiveXObject('Msxml2.XMLHTTP');   }
    catch (e) 
	{
	    try {   xhr = new ActiveXObject('Microsoft.XMLHTTP');    }
	    catch (e2) 
		{
		    try {  xhr = new XMLHttpRequest();     }
		    catch (e3) {  xhr = false;   }
		}
	}
    
    xhr.onreadystatechange  = function()
	{ 
	    if(xhr.readyState  == 4)
		{
		    if(xhr.status  == 200) 
			if (console && console.log) { console.log('success!', xhr.responseText); }
		    else

			if (console && console.error) { console.error('xhr error', xhr.status); }
		}
	}; 
    
    xhr.open("GET", "/activity/record/?"+parms,  true); 
    xhr.send(null); 
    
}


