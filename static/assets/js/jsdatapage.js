//First Getting the list of options for the awesomplete options
var inputlist = d3.select("#player_dropdown")
var names_list = ["De'Andre Hunter", "Trae Young", "Vince Carter", "Cam Reddish", "Kevin Huerter", "Bruno Fernando", "Damian Jones", "DeAndre' Bembry", "John Collins", 
"Brandon Goodwin", "Jeff Teague", "Treveon Graham", "Dewayne Dedmon", "Jarrett Allen", "Joe Harris", "Spencer Dinwiddie", "Taurean Prince", "Garrett Temple", "DeAndre Jordan", "Caris LeVert", "Wilson Chandler", "Kyrie Irving", "Chris Chiozza", "Nicolas Claxton", "Justin Anderson", "Jeremiah Martin", "Tyler Johnson", "Lance Thomas", "Jamal Crawford", "Kevin Durant", "Brad Wanamaker", "Grant Williams", "Semi Ojeleye", "Jayson Tatum", "Marcus Smart", "Jaylen Brown", "Kemba Walker", "Gordon Hayward", "Javonte Green", "Carsen Edwards", "Romeo Langford", "Tremont Waters", "Miles Bridges", "Devonte' Graham", "Terry Rozier", "P.J. Washington", "Cody Zeller", "Malik Monk", "Cody Martin", "Dwayne Bacon", "Caleb Martin", "Jalen McDaniels", "Kobi Simmons", "Coby White", "Thaddeus Young", "Zach LaVine", "Ryan Arcidiacono", "Kris Dunn", "Lauri Markkanen", "Wendell Carter Jr.", "Shaquille Harrison", "Denzel Valentine", "Luke Kornet", "Chandler Hutchison", "Otto Porter", "Max Strus", "Collin Sexton", "Darius Garland", "Tristan Thompson", "Matthew Dellavedova", "Kevin Love", "Larry Nance Jr.", "Kevin Porter Jr.", "Alfonzo McKinnie", "Dean Wade", "Andre Drummond", "Jordan Bell", "Delon Wright", "Tim Hardaway Jr.", "Dorian Finney-Smith", "Justin Jackson", "Seth Curry", "Jalen Brunson", "Dwight Powell", "Courtney Lee", "Willie Cauley-Stein", "Michael Kidd-Gilchrist", "Antonius Cleveland", "Trey Burke", "Josh Reaves", "Monte Morris", "Jerami Grant", "Mason Plumlee", "Jamal Murray", "Will Barton", "Torrey Craig", "Gary Harris", "Michael Porter Jr.", "Paul Millsap", "PJ Dozier", "Bol Bol", "Keita Bates-Diop", "Noah Vonleh", "Troy Daniels", "Langston Galloway", "Christian Wood", "Tony Snell", "Bruce Brown", "Sviatoslav Mykhailiuk", "Derrick Rose", "Luke Kennard", "Blake Griffin", "John Henson", "Louis King", "Brandon Knight", "Khyri Thomas", "Jordan McRae", "Justin Patton", "Eric Paschall", "Marquese Chriss", "Jordan Poole", "Damion Lee", "Ky Bowman", "Draymond Green", "Kevon Looney", "Andrew Wiggins", "Mychal Mulder", "Stephen Curry", "Klay Thompson", "P.J. Tucker", "Ben McLemore", "James Harden", "Austin Rivers", "Danuel House", "Russell Westbrook", "Eric Gordon", "Chris Clemons", "Robert Covington", "Jeff Green", "Michael Frazier", "DeMarre Carroll", "David Nwaba", "Justin Holiday", "T.J. McConnell", "Doug McDermott", "T.J. Warren", "Aaron Holiday", "Domantas Sabonis", "Myles Turner", "Malcolm Brogdon", "Jeremy Lamb", "JaKarr Sampson", "Edmond Sumner", "T.J. Leaf", "Victor Oladipo", "Alize Johnson", "Lou Williams", "Montrezl Harrell", "JaMychal Green", "Patrick Patterson", "Kawhi Leonard", "Rodney McGruder", "Landry Shamet", "Patrick Beverley", "Paul George", "Terance Mann", "Marcus Morris", "Amir Coffey", "Reggie Jackson", "Johnathan Motley", "Mfiondu Kabengele", "Joakim Noah", "Kentavious Caldwell-Pope", "Danny Green", "JaVale McGee", "Alex Caruso", "Anthony Davis", "Kyle Kuzma", "Avery Bradley", "Rajon Rondo", "Jared Dudley", "Quinn Cook", "Markieff Morris", "Dion Waiters", "Talen Horton-Tucker", "Dillon Brooks", "Tyus Jones", "De'Anthony Melton", "Brandon Clarke", "Jaren Jackson Jr.", "Grayson Allen", "Josh Jackson", "John Konchar", "Yuta Watanabe", "Gorgui Dieng", "Anthony Tolliver", "Justise Winslow", "Duncan Robinson", "Kendrick Nunn", "Kelly Olynyk", "Derrick Jones Jr.", "Jimmy Butler", "Tyler Herro", "Meyers Leonard", "Chris Silva", "Andre Iguodala", "Jae Crowder", "Solomon Hill", "Udonis Haslem", "Brook Lopez", "Wesley Matthews", "Pat Connaughton", "Donte DiVincenzo", "Robin Lopez", "Khris Middleton", "Eric Bledsoe", "George Hill", "Kyle Korver", "Sterling Brown", "D.J. Wilson", "Marvin Williams", "Frank Mason III", "Cameron Reynolds", "Jarrett Culver", "Josh Okogie", "Karl-Anthony Towns", "Kelan Martin", "Naz Reid", "Jordan McLaughlin", "Jake Layman", "Jaylen Nowell", "Malik Beasley", "James Johnson", "D'Angelo Russell", "Jarred Vanderbilt", "Jacob Evans", "Evan Turner", "Omari Spellman", "Josh Hart", "Jaxson Hayes", "Lonzo Ball", "Brandon Ingram", "Jrue Holiday", "J.J. Redick", "Frank Jackson", "E'Twaun Moore", "Derrick Favors", "Nickeil Alexander-Walker", "Kenrich Williams", "Jahlil Okafor", "Zion Williamson", "Sindarius Thornwell", "Josh Gray", "Darius Miller", "Bobby Portis", "Kevin Knox", "Julius Randle", "Taj Gibson", "RJ Barrett", "Damyean Dotson", "Elfrid Payton", "Wayne Ellington", "Dennis Smith Jr.", "Reggie Bullock", "Maurice Harkless", "Ignas Brazdeikis", "Theo Pinson", "Shai Gilgeous-Alexander", "Chris Paul", "Steven Adams", "Nerlens Noel", "Abdel Nader", "Mike Muscala", "Hamidou Diallo", "Deonte Burton", "Luguentz Dort", "Devon Hall", "Andre Roberson", "Markelle Fultz", "Terrence Ross", "Aaron Gordon", "D.J. Augustin", "Wesley Iwundu", "Khem Birch", "Michael Carter-Williams", "Jonathan Isaac", "Gary Clark", "James Ennis", "Melvin Frazier", "Al-Farouq Aminu", "B.J. Johnson", "Vic Law", "Tobias Harris", "Mike Scott", "Al Horford", "Matisse Thybulle", "Ben Simmons", "Josh Richardson", "Joel Embiid", "Kyle O'Quinn", "Alec Burks", "Glenn Robinson III", "Zhaire Smith", "Marial Shayok", "Ryan Broekhoff", "Mikal Bridges", "Devin Booker", "Jevon Carter", "Cameron Johnson", "Kelly Oubre Jr.", "Cheick Diallo", "Aron Baynes", "Frank Kaminsky", "Deandre Ayton", "Ty Jerome", "Cameron Payne", "Tariq Owens", "CJ McCollum", "Hassan Whiteside", "Damian Lillard", "Gary Trent Jr.", "Carmelo Anthony", "Nassir Little", "Trevor Ariza", "Rodney Hood", "Caleb Swanigan", "Wenyen Gabriel", "Jaylen Hoard", "Zach Collins", "Jaylen Adams", "Buddy Hield", "Harrison Barnes", "Cory Joseph", "De'Aaron Fox", "Harry Giles", "Richaun Holmes", "Justin James", "Kent Bazemore", "Alex Len", "DaQuan Jeffries", "Jabari Parker", "Corey Brewer", "DeMar DeRozan", "Derrick White", "Rudy Gay", "Dejounte Murray", "Jakob Poeltl", "Bryn Forbes", "Trey Lyles", "LaMarcus Aldridge", "Drew Eubanks", "Chimezie Metu", "Keldon Johnson", "Quinndary Weatherspoon", "Tyler Zeller", "Terence Davis", "OG Anunoby", "Chris Boucher", "Pascal Siakam", "Rondae Hollis-Jefferson", "Kyle Lowry", "Norman Powell", "Matt Thomas", "Patrick McCaw", "Malcolm Miller", "Stanley Johnson", "Oshae Brissett", "Paul Watson", "Royce O'Neale", "Donovan Mitchell", "Georges Niang", "Tony Bradley", "Mike Conley", "Jordan Clarkson", "Ed Davis", "Juwan Morgan", "Rayjon Tucker", "Miye Oni", "Nigel Williams-Goss", "Jarrell Brantley", "Justin Wright-Foreman", "Troy Brown Jr.", "Bradley Beal", 
"Rui Hachimura", "Thomas Bryant", "Moritz Wagner", "Admiral Schofield", "Gary Payton II", 
"Jerome Robinson", "Shabazz Napier", "Johnathan Williams", "Jerian Grant", "Jarrod Uthoff", "John Wall"]
for (var j = 0; j < names_list.length; j++){
    inputlist.append("option").text(names_list[j])
  }

//When the button is clicked, the runform function is ran to get the selected player's data and put it in the table and plot a Plotly chart
var button = d3.select("#filter-btn");
button.on("click", runForm);

function runForm(){
    //prevent page from reloading
    d3.event.preventDefault();


    //Select input
    var inputAwesome = d3.select("#playerchosen")
    var awesomeValue = inputAwesome.property("value")
    var player_title = d3.select("#selectedplayername")
    player_title.text(awesomeValue)
    d3.json("/NBAData", function(nba_data){
        d3.json("/NCAAData", function(ncaa_data){
        
            console.log(nba_data)
            console.log(ncaa_data)
            var filteredNBA = nba_data.filter(playername => playername.Name == awesomeValue)[0];
            var filteredNCAA = ncaa_data.filter(playername => playername.Name == awesomeValue)[0];
            console.log(filteredNBA)
            console.log(filteredNCAA)
            var collegePPG = d3.select("#CollegePPG").text(filteredNCAA.PPG)
            var nbaPPG = d3.select("#NBAPPG").text(filteredNBA.PPG)
            var collegeAPG = d3.select("#CollegeAPG").text(filteredNCAA.APG)
            var nbaAPG = d3.select("#NBAAPG").text(filteredNBA.APG)
            var collegeRPG = d3.select("#CollegeRPG").text(filteredNCAA.RPG)
            var nbaRPG = d3.select("#NBARPG").text(filteredNBA.RPG)
            var collegeBPG = d3.select("#CollegeBPG").text(filteredNCAA.BPG)
            var nbaBPG = d3.select("#NBABPG").text(filteredNBA.BPG)
            var collegeSPG = d3.select("#CollegeSPG").text(filteredNCAA.SPG)
            var nbaSPG = d3.select("#NBASPG").text(filteredNBA.SPG)
            var collegeFG = d3.select("#CollegeFG").text((filteredNCAA.FGP) * 100)
            var nbaFG = d3.select("#NBAFG").text((filteredNBA.FGP) * 100)
            var college3P = d3.select("#College3P").text((filteredNCAA["3PG"]) * 100)
            var nba3P = d3.select("#NBA3P").text((filteredNBA["3PG"]) * 100)
            
            var xCategories = ["PPG", "APG", "RPG", "BPG", "SPG"]
            var percentageCategories = [ "FG%", "3P%"]
            
            var collegevalues = [filteredNCAA.PPG, filteredNCAA.APG, filteredNCAA.RPG, filteredNCAA.BPG, filteredNCAA.SPG] 
            var collegepercentages = [filteredNCAA["FGP"]*100, filteredNCAA["3PG"] * 100]
            var nbavalues = [filteredNBA.PPG, filteredNBA.APG, filteredNBA.RPG, filteredNBA.BPG, filteredNBA.SPG] 
            var nbapercentages = [filteredNBA["FGP"]*100, filteredNBA["3PG"] * 100]

            var trace1 = {
                x: xCategories,
                y: collegevalues,
                name: 'College',
                type: 'bar',
                marker: {
                    color: 'rgb(8,48,107)'
                }
            };
            var trace2 = {
                x: xCategories,
                y: nbavalues,
                name: 'NBA',
                type: 'bar',
                marker: {
                    color: 'rgb(141, 130, 196)'
                }
            }
            var data = [trace1, trace2]
            var layout = {title: 'Per Game Statistics', barmode: 'group'}
            Plotly.newPlot('bar-plot', data, layout)

            //percentage plotted
            var trace3 = {
                x: percentageCategories,
                y: collegepercentages,
                name: 'College',
                type: 'bar',
                marker: {
                    color: 'rgb(8,48,107)'
                }
            }
            var trace4 = {
                x: percentageCategories,
                y: nbapercentages,
                name: 'NBA',
                type: 'bar',
                marker: {
                    color: 'rgb(141, 130, 196)'
                }
            }
            var pdata = [trace3, trace4]
            var playout = {title: 'Percentages', barmode: 'group'}
            Plotly.newPlot('percentages-plot', pdata, playout)

        })
    })

}




