/*Thanks to https://html-online.com/articles/get-url-parameters-javascript/ */
function getUrlVars() {
	var vars = {};
	var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(
		m,
		key,
		value
	) {
		vars[key] = value;
	});
	return vars;
}

function getUrlParam(parameter, defaultvalue) {
	var urlparameter = defaultvalue;
	if (window.location.href.indexOf(parameter) > -1) {
		urlparameter = getUrlVars()[parameter];
	}
	return urlparameter;
}
/* Data */
var total = getUrlParam("total", 1);
var remaining = getUrlParam("remain", 1);
var replies = getUrlParam("reply", 1);
var reTweets = getUrlParam("retweets", 1);
var hashtagged = getUrlParam("hashed", 1);
var mentions = getUrlParam("mentions", 1);
var images = getUrlParam("img", 1);
var titles = getUrlParam("titles", "Twitter, Flamingo, Tweedle").split(",");
var values = getUrlParam("vals", "1,1,1").split(",");

/* Charts */
var ctxDeleted = document.getElementById("deleted");
var ctxReplies = document.getElementById("replies");
var ctxRetweets = document.getElementById("reTweets");
var ctxHashtagged = document.getElementById("hashtagged");
var ctxMentions = document.getElementById("mentions");
var ctxImages = document.getElementById("images");
var ctxPlatform = document.getElementById("platform");

var deletedPie = new Chart(ctxDeleted, {
	type: "pie",
	data: {
		datasets: [
			{
				data: [remaining, total - remaining],
			},
		],
		labels: ["Tweets", "Deleted Tweets"],
		options: {},
	},
});

var repliesPie = new Chart(ctxReplies, {
	type: "pie",
	data: {
		datasets: [
			{
				data: [replies, total - replies],
			},
		],
		labels: ["Replies", "Other Tweets"],
		options: {},
	},
});

var reTweetsPie = new Chart(ctxRetweets, {
	type: "pie",
	data: {
		datasets: [
			{
				data: [reTweets, total - reTweets],
			},
		],
		labels: ["Retweets", "Other Tweets"],
		options: {},
	},
});

var hashtaggedPie = new Chart(ctxHashtagged, {
	type: "pie",
	data: {
		datasets: [
			{
				data: [hashtagged, total - hashtagged],
			},
		],
		labels: ["Tweets w/ a hashtag", "Tweets w/o a hashtag"],
		options: {},
	},
});

var mentionsPie = new Chart(ctxMentions, {
	type: "pie",
	data: {
		datasets: [
			{
				data: [mentions, total - mentions],
			},
		],
		labels: ["Tweets w/ a mention", "Tweets w/o a mention"],
		options: {},
	},
});

var imagesPie = new Chart(ctxImages, {
	type: "pie",
	data: {
		datasets: [
			{
				data: [images, total - images],
			},
		],
		labels: ["Tweets w/ an image", "Tweets w/o an image"],
		options: {},
	},
});

var platformPie = new Chart(ctxPlatform, {
	type: "pie",
	data: {
		datasets: [
			{
				data: values,
			},
		],
		labels: titles,
		options: {},
	},
});
