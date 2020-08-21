
function scrollToTheEndOrToMax(opts = {}) {
    const {
        onFinish,
        onError,
        scrollDownClass = "mye4qd",
        scrollEndClass = "OuJzKb Yu2Dnd",
        interval = 100,
        maxIntervals = 0,
    } = opts;
    let intervalId;
    let currentInterval = 0;
    // function that clear the interval
    function clearScrollInterval() {
        if (intervalId) {
            clearInterval(intervalId);
            onFinish && onFinish();
        }
    }

    // function that scrolls down to the page
    function scrollDown() {
        try {
            // return if the limit of attemps to reach the bottom reach the max of intervals value
            if (maxIntervals > 0 && currentInterval > maxIntervals) return clearScrollInterval();

            // Otherwise Scroll the body height to reach the end
            window.scrollTo(0, document.body.scrollHeight);

            // Retreive the elements to check if the bottom was reached
            const btnToScrollDown = document.getElementsByClassName(scrollDownClass)[0]
            const labelEndOfThePage = document.getElementsByClassName(scrollEndClass)[0]

            // If this element is showed, then return and clear the interval
            if (labelEndOfThePage && window.getComputedStyle(labelEndOfThePage, null).display !== "none") {
                return clearScrollInterval();
            } else if (btnToScrollDown) {
                // otherwise click on the load more button
                btnToScrollDown.click();
            }

            // add one to current interval
            currentInterval++;
        } catch (e) {
            // handle errors if exist.
            onError && onError();
            clearScrollInterval()
        }
    }

    intervalId = setInterval(scrollDown, interval)
}


function getFunctionToExtractFullResImages(opts = {},) {

    const {
        onNext,
        onFinish,
        onError,
        maxImageToProcess,
        interval = 1000,
        singleImageClassName = "PNCib MSM1fd BUooTd",
        selectedImageClassName = "n3VNCb",
    } = opts;

    return function () {
        const arrayOfUlrs = [];
        const arrayOfImageElements = Array.from(document.getElementsByClassName(singleImageClassName))
        const limit = maxImageToProcess
            ? maxImageToProcess + 1
            : arrayOfImageElements.length;
        const arrayOfImages = arrayOfImageElements
            .slice(0, limit)
            .map(div => div.getElementsByTagName("a"));
        let index = 0;
        const fetchUrlIntervalId = setInterval(function () {
            try {
                if (index < arrayOfImages.length) {
                    const thumbImgEl = arrayOfImages[index++][0]
                    thumbImgEl.click();

                    const el = Array.from(document.getElementsByClassName(selectedImageClassName));
                    const imgEl = el.find(({ src }) => !(src.startsWith("data:") || src.indexOf("encrypted-tbn") >= 0))

                    if (!imgEl) return;

                    const url = imgEl.src;
                    arrayOfUlrs.push(url)
                    onNext && onNext({ url, thumbImgEl, imgEl })

                } else {
                    clearInterval(fetchUrlIntervalId);
                    onFinish && onFinish(arrayOfUlrs)
                }
            } catch (e) {
                onError && onError(e)
            }

        }, interval)
    }
}



// scrollToTheEndOrToMax({
//     onFinish: getFunctionToExtractFullResImages({
//         onNext: console.log,
//         onFinish: results => window.__GoogleImagesFullRessImages__ = results,
//         onError: console.log,
//         maxImageToProcess: 5,
//     }),
//     onError: console.log,
// });


