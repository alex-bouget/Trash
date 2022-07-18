KromBlast.set_event("initialized", async () => {
    var p = document.getElementById("p");
    var data = await KromBlast.File.listdir(".");
    for (var i of Object.values(data)) {
        var li = document.createElement("li");
        li.innerText = i;
        p.appendChild(li);
    }
})