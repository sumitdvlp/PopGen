$('#navbar').Stickyfill();	
var tabcounter=0;
var tabarray;
$("li").click(function(){
  // If this isn't already active
  if (!$(this).hasClass("active")) {
    // Remove the class from anything that is active

    // And make this active
    $(this).addClass("active");
  }
});
//function showNotice() {
//$.Notify({
//    caption: 'Warning',
//    content: 'Too many uncontrolled variables will result in long synthesis times',
//    type: 'warning'
//});
//	};
function moveSelected(from, to) {
        $('#'+from+' option:selected').remove().appendTo('#'+to); 
		//if (from == "aggrsynthfrom")
		//{
			
	//	}
    };
function show(elementID) {
                // try to find the requested page and alert if it's not found
                var ele = document.getElementById(elementID);
                if (!ele) {
                    alert("no such element");
                    return;
                }

                // get all pages, loop through them and hide them
                var pages = document.getElementsByClassName('page');
                for(var i = 0; i < pages.length; i++) {
                    pages[i].style.display = 'none';
                }

                // then show the requested page
                ele.style.display = 'block';
				$(this).addClass('active');
            };
function addTab() {    
	//showNotice();
	if (tabcounter < 10)
	{
		tabcounter = tabcounter + 1;	
		var txt3 = document.createElement("div");    // Create with DOM	 
		var txt4 = document.createElement("br");    // Create with DOM	 
		var heading1 = '<div class="cell size3" style="text-align: center"> <h4>';
		var heading2 = 'Tabulation&nbsp';
		var heading3 = '</h4> </div>';
		var name1 = 'name="v1multiTab' + tabcounter + '"';
		var name2 = 'name="v2multiTab' + tabcounter + '"';
		var fname = 'name="tabfname' + tabcounter + '"';
		heading = heading1 + heading2 + tabcounter + heading3;
		var tabval = heading + '<div class="cell size3"><p>Select First Variable</p><div class="input-control select"><select class="tabarray" '+ name1 +' ></select></div></div><div class="cell size3"><p>Select Second Variable</p><div class="input-control select"><select class="tabarray" '+ name2 + ' ></select></div></div><div class="cell size3"><div class="input-control modern text"><input type="text" '+ fname +' > <span class="label">File Name </span> <span class="informer">e.g., hhld_age </span> <span class="placeholder">File Name</span> </div></div>';
		txt3.innerHTML = tabval;
		var brid = "br" + tabcounter;
		var tabid = "tab" + tabcounter;
		$("#tab-add").after(txt4);
		$("#tab-add").after(txt3);          // Insert new elements after <img>
		$(txt3).prop('id', tabid);
		$(txt4).prop('id', brid);
		$(txt3).prop('class','row cells2');	
		$(txt3).prop('style','background-color:#60A917; border: 2px solid white; margin-bottom: 5px; color: #FFF;');	
		var seloption = "";
		$('.tabarray').find('option').remove();
		$('#'+'hhldaggrto'+' option').clone().appendTo('.tabarray');
		$('#'+'personaggrto'+' option').clone().appendTo('.tabarray');
		$('#'+'hhlddaggrto'+' option').clone().appendTo('.tabarray');
		$('#'+'persondaggrto'+' option').clone().appendTo('.tabarray');
		$('#'+'hhldgqto'+' option').clone().appendTo('.tabarray');
		$('#'+'persongqto'+' option').clone().appendTo('.tabarray');
	}
	else
	{
		$.Notify({
    caption: 'Warning',
    content: 'No more than 10 tabulations may be added',
    type: 'warning'
		});
	}
};
function addSingleTab() {    
	//showNotice();
	if (tabcounter < 10)
	{
		tabcounter = tabcounter + 1;	
		var txt3 = document.createElement("div");    // Create with DOM	 
		var txt4 = document.createElement("br");    // Create with DOM	 
		var heading1 = '<div class="cell size3" style="text-align: center"> <h4>';
		var heading2 = 'Tabulation&nbsp';
		var heading3 = '</h4> </div>';
		var name = 'name="singleTab' + tabcounter + '"';
		var fname = 'name="tabfname' + tabcounter + '"';
		heading = heading1 + heading2 + tabcounter + heading3;
		var tabval = heading + '<div class="cell size6"><p>Select Variable</p><div class="input-control select"><select class="tabarray" ' + name + ' ></select></div></div><div class="cell size3"><div class="input-control modern text"><input type="text" ' + fname + ' > <span class="label">File Name </span> <span class="informer">e.g., hhld_age </span> <span class="placeholder">File Name</span> </div></div>';
		txt3.innerHTML = tabval;
		var brid = "br" + tabcounter;
		var tabid = "tab" + tabcounter;
		$("#tab-add").after(txt4);
		$("#tab-add").after(txt3);          // Insert new elements after <img>
		$(txt3).prop('id', tabid);
		$(txt4).prop('id', brid);
		$(txt3).prop('class','row cells2');	
		$(txt3).prop('style','background-color:#60A917; border: 2px solid white; margin-bottom: 5px; color: #FFF;');	
		var seloption = "";
		$('.tabarray').find('option').remove();
		$('#'+'hhldaggrto'+' option').clone().appendTo('.tabarray');
		$('#'+'personaggrto'+' option').clone().appendTo('.tabarray');
		$('#'+'hhlddaggrto'+' option').clone().appendTo('.tabarray');
		$('#'+'persondaggrto'+' option').clone().appendTo('.tabarray');
		$('#'+'hhldgqto'+' option').clone().appendTo('.tabarray');
		$('#'+'persongqto'+' option').clone().appendTo('.tabarray');
	//	$.each(tabarray,function(i){
		//		seloption += '<option value="'+tabarray[i]+'">'+tabarray[i]+'</option>'; 
			//	});
				//$('.tabarray').append(seloption);
	}
	else
	{
		$.Notify({
    caption: 'Warning',
    content: 'No more than 10 tabulations may be added',
    type: 'warning'
		});
	}
};
function removeTab() {      
	var brid = "#br" + tabcounter;
	var tabid = "tab" + tabcounter;
	var elName = "#" + tabid;
    $(elName).remove();	
	$(brid).remove();	
	tabcounter = tabcounter -1;
};
$('#finalpg').submit(function() {  
	var fd = new FormData(document.getElementById("uploader"));
    var var_data = jQuery(document.forms['varassoc']).serializeArray();
    for (var i=0; i<var_data.length; i++)
    fd.append(var_data[i].name, var_data[i].value);
	var var_data = jQuery(document.forms['plabel']).serializeArray();
    for (var i=0; i<var_data.length; i++)
    fd.append(var_data[i].name, var_data[i].value);	

	var var_data = jQuery(document.forms['controlsform']).serializeArray();
    for (var i=0; i<var_data.length; i++)
    fd.append(var_data[i].name, var_data[i].value);	

	var var_data = jQuery(document.forms['selection1']).serializeArray();
    for (var i=0; i<var_data.length; i++)
    fd.append(var_data[i].name, var_data[i].value);	

	var var_data = jQuery(document.forms['selection2']).serializeArray();
    for (var i=0; i<var_data.length; i++)
    fd.append(var_data[i].name, var_data[i].value);

	var var_data = jQuery(document.forms['selection3']).serializeArray();
    for (var i=0; i<var_data.length; i++)
    fd.append(var_data[i].name, var_data[i].value);	

	var var_data = jQuery(document.forms['selection4']).serializeArray();
    for (var i=0; i<var_data.length; i++)
    fd.append(var_data[i].name, var_data[i].value);	

	var var_data = jQuery(document.forms['selection5']).serializeArray();
    for (var i=0; i<var_data.length; i++)
    fd.append(var_data[i].name, var_data[i].value);	

	var var_data = jQuery(document.forms['selection6']).serializeArray();
    for (var i=0; i<var_data.length; i++)
    fd.append(var_data[i].name, var_data[i].value);	

	var var_data = jQuery(document.forms['paramform']).serializeArray();
    for (var i=0; i<var_data.length; i++)
    fd.append(var_data[i].name, var_data[i].value);	

	var var_data = jQuery(document.forms['regionssynth']).serializeArray();
    for (var i=0; i<var_data.length; i++)
    fd.append(var_data[i].name, var_data[i].value);	

	var var_data = jQuery(document.forms['tabulations']).serializeArray();
    for (var i=0; i<var_data.length; i++)
    fd.append(var_data[i].name, var_data[i].value);	

	var var_data = jQuery(document.forms['finalpg']).serializeArray();
    for (var i=0; i<var_data.length; i++)
    fd.append(var_data[i].name, var_data[i].value);	

  //$.post('function/mainhandler.php', fd, function(data) {
	  $.ajax({
              url: "function/mainhandler.php",
              type: "POST",
              data: fd,
              processData: false,  // tell jQuery not to process the data
              contentType: false   // tell jQuery not to set contentType
            }).done(function( data ) {
				console.log (data);
				window.open('joutput.html');	
		});		
});
$('#uploader').submit(function submitForm() {
            
            var fd = new FormData(document.getElementById("uploader"));
            fd.append("label", "WEBUPLOAD");
            $.ajax({
              url: "function/fileproc.php",
              type: "POST",
              data: fd,
              processData: false,  // tell jQuery not to process the data
              contentType: false   // tell jQuery not to set contentType
            }).done(function( data ) {				
				var optionsarray = JSON.parse(data);
				var seloption = "";
				$.each(optionsarray,function(i){
				seloption += '<option value="'+optionsarray[i]+'">'+optionsarray[i]+'</option>'; 
				});
				$('.varopts').append(seloption);
            });		
			var filename = 'region_household_marginal.csv';
			$.post('function/controlvar.php', {data:filename}, function(data)  {				
				var optionsarray = JSON.parse(data);
				tabarray = optionsarray;
				var seloption = "";
				$.each(optionsarray,function(i){
				seloption += '<option value="'+optionsarray[i]+'">'+optionsarray[i]+'</option>'; 
				});
				$('#hhldaggrfrom').append(seloption);
			});    
			var filename = 'region_person_marginal.csv';
			$.post('function/controlvar.php', {data:filename}, function(data)  {				
				var optionsarray = JSON.parse(data);
				$.extend(tabarray, optionsarray);
				var seloption = "";
				$.each(optionsarray,function(i){
				seloption += '<option value="'+optionsarray[i]+'">'+optionsarray[i]+'</option>'; 
				});
				$('#personaggrfrom').append(seloption);
			}); 
			var filename = 'geo_household_marginal.csv';
			$.post('function/controlvar.php', {data:filename}, function(data)  {				
				var optionsarray = JSON.parse(data);
				var seloption = "";
				$.each(optionsarray,function(i){
				seloption += '<option value="'+optionsarray[i]+'">'+optionsarray[i]+'</option>'; 
				});
				$('#hhlddaggrfrom').append(seloption);
			});    
			var filename = 'geo_person_marginal.csv';
			$.post('function/controlvar.php', {data:filename}, function(data)  {				
				var optionsarray = JSON.parse(data);
				var seloption = "";
				$.each(optionsarray,function(i){
				seloption += '<option value="'+optionsarray[i]+'">'+optionsarray[i]+'</option>'; 
				});
				$('#persondaggrfrom').append(seloption);
			}); 
			var filename = 'region_groupquarter_marginal.csv';
			$.post('function/controlvar.php', {data:filename}, function(data)  {				
				var optionsarray = JSON.parse(data);
				var seloption = "";
				$.each(optionsarray,function(i){
				seloption += '<option value="'+optionsarray[i]+'">'+optionsarray[i]+'</option>'; 
				});
				$('#hhldgqfrom').append(seloption);
			});    
			var filename = 'geo_groupquarter_marginal.csv';
			$.post('function/controlvar.php', {data:filename}, function(data)  {				
				var optionsarray = JSON.parse(data);
				var seloption = "";
				$.each(optionsarray,function(i){
				seloption += '<option value="'+optionsarray[i]+'">'+optionsarray[i]+'</option>'; 
				});
				$('#persongqfrom').append(seloption);
			}); 
			var filename = 'region_geo_mapping.csv';
			$.post('function/regiongeo.php', {data:filename}, function(data)  {				
				var optionsarray = JSON.parse(data);
				var seloption = "";
				$.each(optionsarray,function(i){
				seloption += '<option value="'+optionsarray[i]+'">'+optionsarray[i]+'</option>'; 
				});
				$('#aggrsynthfrom').append(seloption);
			});
            return false;
});