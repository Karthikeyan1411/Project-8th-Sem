<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            @import url('https://fonts.googleapis.com/css?family=Gothic+A1|Kaushan+Script|Libre+Baskerville|Lobster');
.body{
	font-family: 'Gothic A1', sans-serif;
	font-size:16px;
	}
	p{
	color:#6c6c6f;
	font-size:1em;
	}
	h1,h2,h3,h4,h5,h6{color:#323233;text-transform:uppercase;}
.navbar-brand  span{
	color: #fed136;
	font-size:25px;font-weight:700;letter-spacing:0.1em;
    font-family: 'Kaushan Script','Helvetica Neue',Helvetica,Arial,cursive;
}
.navbar-brand {
	color: #fff;
	font-size:25px;
    font-family: 'Kaushan Script','Helvetica Neue',Helvetica,Arial,cursive;
	font-weight:700;
	letter-spacing:0.1em;
}

.navbar-nav .nav-item .nav-link{
	padding: 1.1em 1em!important;
	font-size: 120%;
    font-weight: 500;
    letter-spacing: 1px;
    color: #fff;
   font-family: 'Gothic A1', sans-serif;
}
.navbar-nav .nav-item .nav-link:hover{color:#fed136;}
.navbar-expand-md .navbar-nav .dropdown-menu{
	border-top:3px solid #fed136;
}
.dropdown-item:hover{background-color:#fed136;color:#fff;}
nav{-webkit-transition: padding-top .3s,padding-bottom .3s;
    -moz-transition: padding-top .3s,padding-bottom .3s;
    transition: padding-top .3s,padding-bottom .3s;
    border: none;
	}
	
 .shrink {
    padding-top: 0;
    padding-bottom: 0;
    background-color: #212529;
}
.banner{
	/* background-image:url('http://www.hd-freewallpapers.com/latest-wallpapers/abstract-website-backgrounds.jpg'); */
    background-color:black;
	text-align: left;
    color: #fff;
    height: 80px;
   
    background-repeat: no-repeat;
    background-attachment: scroll;
    background-position: center center;
    -webkit-background-size: cover;
    -moz-background-size: cover;
    -o-background-size: cover;
    background-size: cover;
}
.banner-text{
	padding:200px 0 150px 0;
}
.banner-heading{
	font-family: 'Lobster', cursive;
	font-size: 75px;
    font-weight: 700;
    line-height: 100px;
    margin-bottom: 30px;
	color:#fff;
}
.banner-sub-heading{
	font-family: 'Libre Baskerville', serif;
	font-size: 30px;
    font-weight: 300;
    line-height: 30px;
    margin-bottom: 50px;
	color:#fff;
}

.btn-banner{
	padding:5px 20px;
	border-radius:10px;
	font-weight:700;
	line-height:1.5;
	text-align:center;
	color:#fff;
	text-transform:uppercase;
}
.text-intro{
	width:90%;
	margin:auto;
	text-align:center;
	padding-top:30px;
}


.card {
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  transition: 0.3s;
  width: 40%;
  border-radius: 5px;
}

.card:hover {
  box-shadow: 0 8px 6px 0 rgba(0,0,0,0.2);
}


/* mobile view */
@media (max-width:500px)
{
	.navbar-nav{
		background-color:#000;
		border-top:3px solid #fed136;
		color:#fff;
		z-index:1;
		margin-top:5px;
		}
	.navbar-nav .nav-item .nav-link{
	padding: 0.7em 1em!important;
	font-size: 100%;
    font-weight: 500;
    }
	.banner-text{
	padding:150px 0 150px 0;
}
.banner-heading{
	font-size: 30px;
    line-height: 30px;
    margin-bottom: 20px;
}
.banner-sub-heading{
	font-size: 10px;
    font-weight: 200;
    line-height: 10px;
    margin-bottom: 40px;
}

.imageView{
    width:20%;
}

}

@media (max-width:768px){
	.banner-text{
	padding:150px 0 150px 0;
}
	.banner-sub-heading{
	font-size: 23px;
    font-weight: 200;
    line-height: 23px;
    margin-bottom: 40px;
}
}
        </style>
        <script>
            $(document).on("scroll", function(){
		if
      ($(document).scrollTop() > 86){
		  $("#banner").addClass("shrink");
		}
		else
		{
			$("#banner").removeClass("shrink");
		}
	});

    function myFunction() {
  var x = document.getElementById("collapsibleNavbar");
  if (x.style.display === "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
}
    <?php
          $path = "Testing/Training_images/Criminal";
          $files = scandir($path);
          $arr=[];
          foreach ($files as &$value) {
            if(strpos($value,'.')||strpos($value,'..')){
              array_push($arr,$value);
            }else{
              continue;
            }
          }
          ?>
    <?php
          $path2 = "Testing/Training_images/Missing";
          $files2 = scandir($path2);
          $arr2=[];
          foreach ($files2 as &$value) {
            if(strpos($value,'.')||strpos($value,'..')){
              array_push($arr2,$value);
            }else{
              continue;
            }
          }
          ?>
        </script>
    </head>
    <body>
        <link href="//maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
        <script src="//maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
        <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
        <!------ Include the above in your HEAD tag ---------->

        <nav class="navbar navbar-expand-md navbar-dark fixed-top" id="banner">
            <div class="container">
        <!-- Brand -->
        <!-- <a class="navbar-brand" href="#"><span><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Sona_College_of_Teachnology.jpg/1920px-Sona_College_of_Teachnology.jpg" width="120px" height="50px"></span>??</a> -->

        <!-- Toggler/collapsibe Button -->
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
            <span class="navbar-toggler-icon" onclick="myFunction()"></span>
        </button>

        <!-- Navbar links -->
        <div class="collapse navbar-collapse" id="collapsibleNavbar">
            <ul class="navbar-nav ml-auto">
            <li class="nav-item">
                <a class="nav-link" href="http://localhost/Search-Portal/home.php">Home</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="http://localhost/Search-Portal/imageSlide.php">Match</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="http://localhost/Search-Portal/upload.php">Upload</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="http://localhost/Search-Portal/database.php">Dataset</a>
            </li>

            </ul>
        </div>
            </div>
        </nav>

        <div class="banner">
            <div class="container" >
            <div class="banner-text">
            </div>
        </div>
        </div>
        <center>
        <div>
        <input style="margin-bottom:15px;margin-top:15px;" type="text" id="myInput" class="input" onkeyup="search()" placeholder="Search for names.." title="Type in a name">
        </div>
        <h1>Criminal</h1>
        <div id="results"></div>
        </center>
        <script>
            var questionArray=<?php echo json_encode($arr) ?>;
            var len=questionArray.length;
            var count=0;
            for(var i=0;i<len;i++){
                $('#results').append("<div class=card>");
                $('#results').append("<img id=img_"+i+" src=./Testing/Training_images/Criminal/"+questionArray[i]+">");
                $('#results').append("<div class=container>");
                $('#results').append("<p id=p_"+i+" >"+questionArray[i]+"</p>");
                $('#results').append('<button onClick=dele('+i+') id=del_'+i+'>Delete</button>');
                $('#results').append('</div>');
                $('#results').append('</div>');
                // J('.filterToggle').append(' <a href="#" onClick="J("table td:nth-child('+ num +'),th:nth-child('+ num +')").show();"> Show "thName" </a>');}
                $('#results img').css({"width":"8%","margin-left":"5%"});
                $('#results p').css({"width":"8%","margin-left":"5%"});
                $('#results button').css({"width":"8%","margin-left":"5%"});
                // $('#results').css({"display": "flex"});
                // count++;
                // if(count==4){
                //     $('#results').append("<br>");
                //     $('#results').css({"display": "block"});
                //     count=0;
                // }
                function dele(x){
                    var imgElement_src = $('#img_'+x).attr("src");
                    console.log(imgElement_src);
                    $.ajax({
                        url: 'delete.php',
                        type: 'post',
                        data: {path: imgElement_src},
                    });
                    $("#img_"+x).remove();
                    $("#p_"+x).remove();
                    $("#del_"+x).remove();
                }
            }

            var questionArray2=<?php echo json_encode($arr2) ?>;
            var len=questionArray2.length;
            var count=0;
            $('#results').append("<h1>Missing</h1>");
            for(var i=0;i<len;i++){
                $('#results').append("<div class=card>");
                $('#results').append("<img id=img_"+i+" src=./Testing/Training_images/Missing/"+questionArray2[i]+">");
                $('#results').append("<div class=container>");
                $('#results').append("<p id=p_"+i+" >"+questionArray2[i]+"</p>");
                $('#results').append('<button onClick=dele('+i+') id=del_'+i+'>Delete</button>');
                $('#results').append('</div>');
                $('#results').append('</div>');
                // J('.filterToggle').append(' <a href="#" onClick="J("table td:nth-child('+ num +'),th:nth-child('+ num +')").show();"> Show "thName" </a>');}
                $('#results img').css({"width":"8%","margin-left":"5%"});
                $('#results p').css({"width":"8%","margin-left":"5%"});
                $('#results button').css({"width":"8%","margin-left":"5%"});
                // $('#results').css({"display": "flex"});
                // count++;
                // if(count==4){
                //     $('#results').append("<br>");
                //     $('#results').css({"display": "block"});
                //     count=0;
                // }
                function dele(x){
                    var imgElement_src = $('#img_'+x).attr("src");
                    console.log(imgElement_src);
                    $.ajax({
                        url: 'delete.php',
                        type: 'post',
                        data: {path: imgElement_src},
                    });
                    $("#img_"+x).remove();
                    $("#p_"+x).remove();
                    $("#del_"+x).remove();
                }
            }
            function search() {
                var input=document.querySelector('#myInput');
                var images=document.querySelectorAll('#results > img');
                var img_title=document.querySelectorAll('#results > p');
                var img_btn=document.querySelectorAll('#results > button');

                input.addEventListener('keydown',function(){
                    for(var i=0; i<images.length;i++)
                {
                        if(new RegExp(this.value).test(images[i].src))
                    {      
                        images[i].style.display ='block'
                        img_title[i].style.display ='block'
                    }
                    else
                    {
                        images[i].style.display ='none'
                        img_title[i].style.display ='none'
                        img_btn[i].style.display ='none'
                    }
                    // console.log(images[i].src)
                }
                
                })
            }

            // $(function() {

            //     $("#results button").click(function() {
            //     $(this).parent().remove();
            //     });

            //     });

        </script>
    </body>
</html>