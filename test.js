
airlines = [{'YV':'Mesa Airlines', 'EV':'ExpressJet','AS':'Alaska Airlines',
'UA':'United Airlines','YX': 'Republic Airways','AA': 'American Airlines', 
'F9':'Fronteir Airlines','9E':'Endeavor Air','NK':'Spirit Airlines','OO':'SkyWest Airlines',
'DL':'Delta Airlines',"B6":'JetBlue',"OH":"PSA Airlines"}]; 

var abbrev= [];
var carrier = [];

// Iterate through each recipe object
airlines.forEach((airline) => {

  // Iterate through each key and value
  Object.entries(airline).forEach(([key, value]) => {
    carrier.push(value)
    abbrev.push(key)
   });
});


function onlyUnique(value, index, self) { 
    return self.indexOf(value) === index;
}  

  
  function initial1(){ 

    d3.csv("Project_3/data.csv").then((data)=>{
        console.log(data)
        var airlines = data.map(item=>item.Airline).filter( onlyUnique ); 
        var dropDown1 = d3.select("#dropdown1");


        carrier.forEach((sample) => {
        
        dropDown1
        .append("option")
        .text(sample)
        .property("value", sample);  

        });
        
        var dest_airports = data.map(item=>item.Destination_Airport).filter( onlyUnique ); 
        var dropDown2 = d3.select("#dropdown2");

        dest_airports.forEach((sample) => {
            dropDown2
            .append("option")
            .text(sample)
            .property("value", sample);   


        });

        
        
    });
   
         
  };
  
  
  function optionChanged(newSample) {

  };
  

  
initial1();
optionChanged();