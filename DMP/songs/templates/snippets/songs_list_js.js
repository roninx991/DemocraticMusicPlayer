{% load static %}
document.getElementById("SongImage").src="{% static 'images/' %}"+playlist[counter]+".jpg";
document.getElementById("track").innerHTML=names[counter]+"<br><small>"+singers[counter]+"</small>";
function previous()
{
	counter=counter-1;
	if(counter<0)
	{
		counter=playlist.length-1;
	}	
	msource.src="{% static 'songs/' %}"+playlist[counter]+".mp3";
	music.load();
	document.getElementById("SongImage").src="{% static 'images/' %}"+playlist[counter]+".jpg";
	document.getElementById("track").innerHTML=names[counter]+"<br><small>"+singers[counter]+"</small>";

	return;
}
function next()
{
	counter=counter+1;
	if(counter>playlist.length-1)
	{
		counter=0;
	}
	msource.src="{% static 'songs/' %}"+playlist[counter]+".mp3";
	music.load();
	document.getElementById("SongImage").src="{% static 'images/' %}"+playlist[counter]+".jpg";
	document.getElementById("track").innerHTML=names[counter]+"<br><small>"+singers[counter]+"</small>";
	return;
}
function pauseplay()
{
	if(pause_play==0)
	{
		document.getElementById("pandp").innerHTML="<i class='fa fa-play' aria-hidden='true'></i>";
		pause_play=1;
		music.pause();
	}
	else
	{
		document.getElementById("pandp").innerHTML="<i class='fa fa-pause' aria-hidden='true'></i>";
		pause_play=0;
		music.play();
	}
	return;
}
window.setInterval(check,1000);

function check()
{
	if(music.ended)
	{
		next();
	}
	slider.value = music.currentTime;
	slider.min = 0;
	slider.max = music.duration;
	time(slider.value);
}
function time(num)
{
	var minutes = Math.floor(num/60);
	var seconds = num%60;
	if(seconds<10)
		document.getElementById("time").innerHTML=minutes+":0"+seconds;
	else
		document.getElementById("time").innerHTML=minutes+":"+seconds;
}

function volume()
{
	if(vol_btn == 0)
	{
		document.getElementById("volumecontainer").style.display = "block";
		vol_btn=1;
	}
	else
	{
		document.getElementById("volumecontainer").style.display = "none";
		vol_btn=0;
	}	
}
var slider = document.getElementById("myRange");
var vol = document.getElementById("myVolume");

vol.value = music.volume;
vol.min = 0;
vol.max = 100;

slider.value = music.currentTime;
slider.min = 0;
slider.max = music.duration;


// Update the current slider value (each time you drag the slider handle)
slider.oninput = function() {
    music.currentTime = this.value;
} 
vol.oninput = function() {
	music.volume = this.value;
}
