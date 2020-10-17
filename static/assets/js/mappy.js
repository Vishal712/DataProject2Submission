// Creating map object
var myMap = L.map("map", {
  center: [38.5, -97.6],
  zoomSnap: 0.25,
  zoom: 5
});

// Adding tile layer to the map
L.tileLayer("https://api.mapbox.com/styles/v1/hyrum78/ckg9tsvf803p519pet1f9cbmk/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1IjoiaHlydW03OCIsImEiOiJja2c1bGdpZjQwdWIwMnJtc2dscmd0eHFzIn0.lEHm3LRxyN6_azwPjzIf5A", {
  attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
  tileSize: 512,
  maxZoom: 18,
  zoomOffset: -1,
  id: "mapbox/streets-v11",
  accessToken: API_KEY
  }).addTo(myMap);

  // pull icon
  var ballIcon = L.icon({
    iconUrl: '../static/images/ballicon.png',
    iconSize: [30,30],
    popupAnchor: [-10, -30],
  }); 

d3.json("/NBALocation", function(data) {
  d3.json("/Averages", function(averageData){

  // Create a new marker cluster group
  var markers = L.markerClusterGroup(

  );
  // Loop through data
  for (var i = 0; i < data.length; i++) {

    // Set the data location property to a variable
    var location = [data[i].lat, data[i].lng];

    // Check for location property
    if (location) {
      var filteredAvg = averageData.filter(playername => playername.school == data[i].school)[0];
      
      //there are a couple of players with no listed school, so if there data is undefined, it will count that player's average
      if(filteredAvg == null){
        filteredAvg = data[i]
      }
      // Add a new marker to the cluster group and bind a pop-up
      markers.addLayer(L.marker([location[0], location[1]],{icon: ballIcon})
        .bindPopup("School: " + data[i].school + "<br>" +
                    "Avg NBA Player Stats:" + "<br>" + 
                    "PPG " + filteredAvg.PPG + "<br>" + 
                    "APG " + filteredAvg.APG + "<br>" + 
                    "RPG " + filteredAvg.RPG));
    }

  }

  // Add our marker cluster layer to the map
  myMap.addLayer(markers);
  
 
})
})