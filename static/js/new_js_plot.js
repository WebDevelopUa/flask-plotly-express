// Initialize new plot on Dashboard template
// https://plotly.com/javascript/getting-started/
// https://plotly.com/javascript/reference/layout/#layout-modebar-remove
// https://plotly.com/javascript/configuration-options/

void function addPlot() {
    console.log('... add new Plot with params ...')

    let myPlot = document.getElementById('myPlot');
    let layout = {
        title: 'Hide the Plotly Logo on the Modebar',
        showlegend: false
    };

    Plotly.newPlot(myPlot,
        [
            {
                x: [1, 2, 3, 4, 5],
                y: [10, 20, 40, 80, 160]
            }
        ], {
            // margin: {t: 0, b: 0, l: 10, r: 10}
            margin: {t: 10}
        }
    )


    // document.getElementsByClassName('modebar-container')[0].style.display = "none";
}()

