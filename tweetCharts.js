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

var total = getUrlParam("total", 1);
var remaining = getUrlParam("remain", 1);
var replies = getUrlParam("reply", 1);
var reTweets = getUrlParam("retweets", 1);
var hashtagged = getUrlParam("hashed", 1);
var mentions = getUrlParam("mentions", 1);
var images = getUrlParam("img", 1);
var titles = getUrlParam("titles", "Twitter, Flamingo, Tweedle").split(",");
var values = getUrlParam("vals", "1,1,1").split(",");
