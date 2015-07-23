import java.util.ArrayList;
import edu.princeton.cs.introcs.In;
import java.util.HashMap;
import java.lang.*;
import java.util.Collections;

public class OscarDataAnalyzer {
	/* Main method */
	public static void main(String[] args) {
		long startTime = System.currentTimeMillis();
		
		OscarDataAnalyzer oscarAnalyzer = new OscarDataAnalyzer("oscar_tweets.csv");
		oscarAnalyzer.rankPopularity();
		System.out.println();
		
		oscarAnalyzer.printWinnerPredictionTime();
		System.out.println();
		
		oscarAnalyzer.rankLocationActivity();
		System.out.println();
		
		long endTime = System.currentTimeMillis();
		long totalTime = endTime - startTime;
		System.out.println("Runtime: " + totalTime/1000.0 + " seconds.");
	}

	private String[] bestPictureNominees = new String[]{"americansniper", "american sniper", "birdman", "birdman", "boyhood", "boyhood", "thegrandbudapesthotel", "the grand budapest hotel",
														 "theimitationgame", "the imitation game", "selma", "selma", "thetheoryofeverything", "the theory of everything", "whiplash", "whiplash"};
	private HashMap<String, Integer> timeCounts = new HashMap<String, Integer>();
	private HashMap<String, Integer> locationCounts = new HashMap<String, Integer>();
	private HashMap<String[], String> locationFinder = new HashMap<String[], String>();
	private HashMap<String, Integer> nomineeCounts = new HashMap<String, Integer>();
	private String cityData = "biggest_cities.csv"; //file containing state abbreviations/biggest cities in each state to track location
	private String maxTime;
	private int maxCount;

	/* Creates a DataAnalyzer using files from CSVFILENAME */
	public OscarDataAnalyzer(String csvFilename) {
		In csvReader = new In(csvFilename);
		initializeLocationFinder();
		initializeNomineeCounts();
		maxCount = 0;

		while (csvReader.hasNextLine()) {
			String[] data = separateData(csvReader.readLine());
			boolean birdmanMentioned = containsBirdman(data);
			
			//part1
			if (birdmanMentioned) { 
				String time = getHourAndMinute(data);
				if (time != "") {
					updateCounts(time);
				}
			}

			//part2
			mapLocations(data);

			//part3
			analyzeMoviePopularity(data);

		}
	}

	/* Initializes HashMap containing counts of tweet mentions of Best Picture Nominees */
	private void initializeNomineeCounts() {
		nomineeCounts.put("American Sniper", new Integer(0));
		nomineeCounts.put("Birdman", new Integer(0));
		nomineeCounts.put("Boyhood", new Integer(0));
		nomineeCounts.put("The Grand Budapest Hotel", new Integer(0));
		nomineeCounts.put("The Imitation Game", new Integer(0));
		nomineeCounts.put("Selma", new Integer(0));
		nomineeCounts.put("The Theory of Everything", new Integer(0));
		nomineeCounts.put("Whiplash", new Integer(0));
	}

	/* Using tweet form of text (e.g. AmericanSniper as opposed to American Sniper), simply returns full written form of movie */
	private String findMovie(String movie) {
		if (movie.equals(bestPictureNominees[0]) || movie.equals(bestPictureNominees[1])) {
			return "American Sniper";
		} else if (movie.equals(bestPictureNominees[2]) || movie.equals(bestPictureNominees[3])) {
			return "Birdman";
		} else if (movie.equals(bestPictureNominees[4]) || movie.equals(bestPictureNominees[5])) {
			return "Boyhood";
		} else if (movie.equals(bestPictureNominees[6]) || movie.equals(bestPictureNominees[7])) {
			return "The Grand Budapest Hotel";
		} else if (movie.equals(bestPictureNominees[8]) || movie.equals(bestPictureNominees[9])) {
			return "The Imitation Game";
		} else if (movie.equals(bestPictureNominees[10]) || movie.equals(bestPictureNominees[11])) {
			return "Selma";
		} else if (movie.equals(bestPictureNominees[12]) || movie.equals(bestPictureNominees[13])) {
			return "The Theory of Everything";
		} else if (movie.equals(bestPictureNominees[14]) || movie.equals(bestPictureNominees[15])) {
			return "Whiplash";
		} return "";
	}

	/* Hashes the number of times each Best Picture nominee is mentioned in the input dataset */
	private void analyzeMoviePopularity(String[] data) {
		for (String movie : bestPictureNominees) {
			if ((data[2].toLowerCase().indexOf(movie) != -1) || (data[15].toLowerCase().indexOf(movie) != -1) || (data[16].toLowerCase().indexOf(movie) != -1)) {
				String nominee = findMovie(movie);
				Integer i = nomineeCounts.get(nominee);
				nomineeCounts.remove(nominee);
				nomineeCounts.put(nominee, new Integer(i.intValue() + 1));
			}
		}
	}

	/* Returns an array whose elements are the various fields of the line of input */
	private String[] separateData(String line) {
		String[] data = new String[17];
		int index = 0;
		int nextComma = line.indexOf(",");
		while (nextComma != -1 && index < 17) {
			if (line.charAt(0) == "\"".charAt(0)) {
				int endQuote = line.indexOf("\"", 1);
				try {
					data[index] = line.substring(0, endQuote);
				} catch (StringIndexOutOfBoundsException e) {
					return new String[]{"", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""};
				}
				try {
					line = line.substring(endQuote + 2);
				} catch (StringIndexOutOfBoundsException e) {
					line = "";
				}
			} else {
				try {
					data[index] = line.substring(0, nextComma);
				} catch (StringIndexOutOfBoundsException e) {
					return new String[]{"", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""};
				}
				try {
					line = line.substring(nextComma + 1);
				} catch (StringIndexOutOfBoundsException e) {
					line = "";
				}
			}
			index++;
			nextComma = line.indexOf(",");
		}

		//protects against NULLPOINTEREXCEPTIONs
		while (index < 17) {
			data[index] = "";
			index++;
		}
		return data;
	}

	/* References user input location with largest cities/state abbreviation of states to estimate actual location */
	private void mapLocations(String[] data) {
		for (String[] locations : locationFinder.keySet()) {
			boolean foundLocation = false;
			for (int i = 0; i < locations.length; i++) {
				if (i == 6) {
					if ((data[5].indexOf(locations[i]) != -1) || (data[8].indexOf(locations[i]) != -1)) {
						foundLocation = true;
					}
				} else {
					if ((data[5].toLowerCase().indexOf(locations[i]) != -1) || (data[8].toLowerCase().indexOf(locations[i]) != -1)) {
						foundLocation = true;
					}
				}
			}

			if (foundLocation) {
				String location = locationFinder.get(locations);
				Integer count = locationCounts.get(location);
				locationCounts.remove(location);
				locationCounts.put(location, new Integer(count.intValue() + 1));
			}
		}
	}

	/* Initializes a hash map mapping cities to an array of their 5 largest cities and state abbreviation */
	private void initializeLocationFinder() {
		In cityReader = new In(cityData);
		while (cityReader.hasNextLine()) {
			String[] stateToCities = cityReader.readLine().split(","), cities = new String[7];
			String state = stateToCities[0];
			for (int i = 1; i < stateToCities.length; i++) {
				cities[i-1] = stateToCities[i].toLowerCase(); 
			}
			locationFinder.put(cities, state);
			locationCounts.put(state, new Integer(0));
		}
	}

	/* If birdman is mentioned within a tweet, updates timeCounts, maxTime, and maxCount appropriately. */
	private void updateCounts(String time) {	
		Integer i = timeCounts.get(time);
		if (i == null) {
			timeCounts.put(time, new Integer(1));
		} else {
			int newCount = i.intValue() + 1;
			i = new Integer(newCount);
			timeCounts.remove(time);
			timeCounts.put(time, i);
			if (newCount > maxCount) {
				maxCount = newCount;
				maxTime = time;
			}
		}
	}

	/* Given a String[] of data about a tweet, returns the time (hour and minute) of tweeting */
	private String getHourAndMinute(String[] data) {
		try {
			String time = data[0].split(" ")[3];
			try {
				int timeDifference = (Integer.parseInt(data[10])/3600);
				char hour = time.charAt(1);
				StringBuilder myTime = new StringBuilder(time);
				if (-8 <= timeDifference && timeDifference <= -5) {
					int newHour = 4 + Integer.parseInt(Character.toString(hour));
					myTime.setCharAt(1, Integer.toString(newHour).charAt(0));
					return myTime.toString().substring(0, time.lastIndexOf(":"));
				}
			} catch (NumberFormatException e) {}
		} catch (ArrayIndexOutOfBoundsException e) {}
		return "";
	}

	/* Returns true if a tweet's text or tags contain "birdman" (case is irrelvant), false otherwise */
	private boolean containsBirdman(String[] data) {
		boolean inText = data[2].toLowerCase().indexOf("birdman") != -1;
		if (inText)
			return true;
		boolean hashtagged = data[data.length - 2].toLowerCase().indexOf("birdman") != -1;
		if (hashtagged) 
			return true;
		boolean userMentioned = data[data.length - 1].toLowerCase().indexOf("birdman") != -1;
		if (userMentioned)
			return true;
		return false;
	}

	/* Returns a list of the most tweeted about best picture nominees (ranked from 1-8) */
	public void rankPopularity() {
		ArrayList<Integer> mapValues = new ArrayList<Integer>(nomineeCounts.values());
		Collections.sort(mapValues);
		int rank = 1;
		System.out.println("Most tweeted about best picture nominees: ");
		for (int i = mapValues.size() - 1; i >= 0; i--) {
			int count = (mapValues.get(i)).intValue();
			for (String key : nomineeCounts.keySet()) {
				if (nomineeCounts.get(key).intValue() == count) {
					System.out.println(rank + ") " + key);
					rank += 1;
				}
			}
		}
	}

	/* Prints the time (hour and minute) when the winner (Birdman) was mentioned on Twitter most frequently */
	public void printWinnerPredictionTime() {
		System.out.println("Birdman was mentioned most frequently on twitter at " + maxTime + " PST on January 23rd during the Oscars.");
	}

	/* Prints a list of states by activity (in descending order) in tweeting about #Oscars2015 */
	public void rankLocationActivity() {
		ArrayList<Integer> mapValues = new ArrayList<Integer>(locationCounts.values());
		Collections.sort(mapValues);
		int rank = 1;

		System.out.println("State rankings by activity in tweeting about #Oscars2015: ");
		for (int i = mapValues.size() - 1; i >= 0; i--) {
			int count = (mapValues.get(i)).intValue();
			for (String key : locationCounts.keySet()) {
				if (locationCounts.get(key).intValue() == count) {
					if (!key.equals("State")) {
						System.out.println(rank + ") " + key);
						rank += 1;
					}
				}
			}
		}
	}
}