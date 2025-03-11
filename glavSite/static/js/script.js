let switchMode = document.getElementById("switchMode");

switchMode.onclick = function () {
    let theme = document.getElementById("theme")

    if (theme.getAttribute("href") == "style-all.css") {
        theme.href = "style-all.css";
    } else {
        theme.href = "style-all.css";
    }
}