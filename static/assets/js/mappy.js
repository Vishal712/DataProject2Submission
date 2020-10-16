// Creating our initial map object
// We set the longitude, latitude, and the starting zoom level
// This gets inserted into the div with an id of 'map'
var myMap = L.map("map", {
  center: [37.09, -95.71],
  zoom: 5
});
// Adding a tile layer (the background map image) to our map
// We use the addTo method to add objects to our map
L.tileLayer("https://api.mapbox.com/styles/v1/hyrum78/ckg9tsvf803p519pet1f9cbmk/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1IjoiaHlydW03OCIsImEiOiJja2c1bGdpZjQwdWIwMnJtc2dscmd0eHFzIn0.lEHm3LRxyN6_azwPjzIf5A", {
  attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
  tileSize: 512,
  maxZoom: 18,
  zoomOffset: -1,
  id: "mapbox/streets-v11",
  accessToken: API_KEY
}).addTo(myMap);


d3.csv("../static/assets/data/NBALocation.csv", function(data) {

  var markers = L.markerClusterGroup();
  for (i = 0; i < data.length; i++) {
    var location = [data[i].lat, data[i].lng]
    console.log(data)
    
    if (location) {
      markers.addLayer(L.marker([location[0], location[1]])
        .bindPopup(data[i].school));
    }
  }
myMap.addLayer(markers)
});