const opentab = (event,tabname) => {
    let links=document.getElementsByClassName("tab")
    let contents=document.getElementsByClassName("tab-contents")
    for(let link of links){
        link.classList.remove("active-link");
    }
    for(let content of contents){
        content.classList.remove("active-tab");
    }
    event.currentTarget.classList.add("active-link");
    document.getElementById(tabname).classList.add("active-tab");
}
document.addEventListener("DOMContentLoaded", function () {
    let links = document.getElementsByClassName("tab");
    for (let i = 0; i < links.length; i++) {
        links[i].addEventListener("click", function (event) {
            opentab(event, this.getAttribute("data-tab"));
        });
    }
});