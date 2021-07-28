// POST request on Date Range change selector
// https://api.jquery.com/change/

$(window).on('load', function () {
    let value = 'Weekly'
    console.log(`Date Range load: ${value}`);
});

$("#dateRange").change(function (value) {
    console.log(`Date Range change: ${value.target.value}`);
});

//  Request: {
//     "date_range": {
//         "type": "monthly",
//         "year": 2021,
//         "month": 5,
//         "day": 12,
//         "hour": 0
//     },
//     "cid": "8546546546146"
// }
//
// Response: {
//     "nlinks": 10,
//     "hits": [12, 10, 7, ..., 40],
//     "top_ref": [
//                   {"n": "LinkedIn", "h": 12, ... , {"n": "others", "h": 20}}
//                 ],
//     "top_cntr": [
//                   {"n": "Ukraine", "h": 12, ... , {"n": "others", "h": 20}}
//                 ]
// }
//
//  Plotly EXPRESS Sample #3
// Selector options:
// Weekly - Display last 7 days
// Monthly - Display last 1 - 31 days (we need to know what is the current year + month)
// Yearly - Display all * days (we need to know what is the current year)