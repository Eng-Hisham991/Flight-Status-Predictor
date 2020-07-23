// d3.selectAll("body").on("change", updatePage);

// function updatePage() {
//   // Use D3 to select the dropdown menu
//   var dropdownMenu1 = d3.selectAll("#selDataset").node();
//   var dropdownMenu2 = d3.selectAll("#selDataset1").node();
//   // Assign the dropdown menu item ID to a variable
//   var dropdownMenuID = dropdownMenu1.id;
//   var dropdownMenuID2 = dropdownMenu2.id;
//   // Assign the dropdown menu option to a variable
//   var selectedOption = dropdownMenu1.value;
//   var selectedOption1 = dropdownMenu2.value;

//   console.log(dropdownMenuID);
//   console.log(dropdownMenuID2);
//   console.log(selectedOption);
//   console.log(selectedOption1);
// }
// airlines = [{'YV':'Mesa Airlines', 'EV':'ExpressJet','AS':'Alaska Airlines',
// 'UA':'United Airlines','YX': 'Republic Airways','AA': 'American Airlines', 
// 'F9':'Fronteir Airlines','9E':'Endeavor Air','NK':'Spirit Airlines','OO':'SkyWest Airlines',
// 'DL':'Delta Airlines',"B6":'JetBlue',"OH":"PSA Airlines"}]; 

// var abbrev= [];
// var carrier = [];

// // Iterate through each recipe object
// airlines.forEach((airline) => {

//   // Iterate through each key and value
//   Object.entries(airline).forEach(([key, value]) => {
//     carrier.push(value)
//     abbrev.push(key)
//    });
// });


// function onlyUnique(value, index, self) { 
//     return self.indexOf(value) === index;
// }  

  
// function initial1(){ 

//   d3.csv("/data").then((data)=>{
//     console.log(data)
//     var airlines = data.map(item=>item.Airline).filter( onlyUnique ); 
//     var dropDown1 = d3.select("#dropdown1");

//     ('.dropdown-menu').dropDown1('toggle');
//     // carrier.forEach((sample) => {
      
//     // dropDown1
//     // .append("option")
//     // .text(sample)
//     // .property("value", sample);  

//     // });
      
//     var dest_airports = data.map(item=>item.Destination_Airport).filter( onlyUnique ); 
//     ('.dropdown-menu').dropdown2('toggle');
//     var dropDown2 = d3.select("#dropdown2");
//     console.log(dest_airports)
//     // dest_airports.forEach((sample) => {
//     //     dropDown2
//     //     .append("option")
//     //     .text(sample)
//     //     .property("value", sample);   


//     //   });

      
      
//   });
  
        
// };


// function optionChanged(newSample) {

// };
// function optionChanged1(newSample) {

// };

  
// initial1();
// optionChanged();

// // function initial1(){ 

// //   d3.csv("/data").then((data)=>{
// //     console.log(data) 
// //     airlines = [{'YV':'Mesa Airlines', 'EV':'ExpressJet','AS':'Alaska Airlines',
// //                 'UA':'United Airlines','YX': 'Republic Airways','AA': 'American Airlines', 
// //                 'F9':'Fronteir Airlines','9E':'Endeavor Air','NK':'Spirit Airlines','OO':'SkyWest Airlines',
// //                 'DL':'Delta Airlines',"B6":'JetBlue',"OH":"PSA Airlines"}]; 
    
// //     var abbrev= [];
// //     var carrier = [];
    
// //     // Iterate through each recipe object
// //     airlines.forEach((airline) => {
    
// //       // Iterate through each key and value
// //       Object.entries(airline).forEach(([key, value]) => {
// //         carrier.push(value)
// //         abbrev.push(key)
// //         });
// //     });
// //     function onlyUnique(value, index, self) { 
// //       return self.indexOf(value) === index;
// //   }  
// //     console.log(airlines)
// //     var dropDown1 = d3.select("#selDataset");
// //     var firstSample = dropDown1.property('value')        
// //     var dropDown2 = d3.select("#selDataset1");
// //     var firstSample = dropDown2.property('value')

    
      
// //   });
  
        
// // };


// // // function optionChanged(newSample) {

// // //   };
  

  
// // initial1();
// // // optionChanged();